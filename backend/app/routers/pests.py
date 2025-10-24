"""
Pest Detection API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app.ml_models.pest_detection import PestDetectionModel
from app.schemas.pest import PestDetectionResponse, PestDetectionCreate
from app.services.pest_service import PestService
from app.core.config import settings
import os
import uuid
from typing import Optional

router = APIRouter()

# Initialize ML model
pest_model = PestDetectionModel(settings.PEST_DETECTION_MODEL_PATH)

@router.post("/detect", response_model=PestDetectionResponse)
async def detect_pest(
    file: UploadFile = File(...),
    location: Optional[str] = Form(None),
    crop_affected: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    """Detect pest/disease from uploaded image"""
    
    # Validate file
    if not file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(
            status_code=400,
            detail="Only JPEG and PNG images are allowed"
        )
    
    # Save uploaded file
    file_extension = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = f"uploads/pest_detection/{filename}"
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    try:
        # Run ML prediction
        prediction_result = pest_model.predict(file_path)
        
        # Get treatment recommendations
        pest_class = prediction_result["primary_prediction"]["class"]
        treatment_recommendations = pest_model.get_treatment_recommendations(pest_class)
        
        # Save detection to database
        pest_service = PestService(db)
        detection = pest_service.create_detection({
            "image_path": file_path,
            "detected_pest": pest_class,
            "confidence_score": prediction_result["primary_prediction"]["confidence"],
            "location": location,
            "crop_affected": crop_affected,
            "severity": "High" if prediction_result["primary_prediction"]["confidence"] > 0.8 else "Medium"
        })
        
        return {
            "detection_id": detection.id,
            "image_path": file_path,
            "primary_prediction": prediction_result["primary_prediction"],
            "all_predictions": prediction_result["all_predictions"],
            "treatment_recommendations": treatment_recommendations,
            "is_healthy": prediction_result["is_healthy"],
            "confidence_threshold": prediction_result["confidence_threshold"]
        }
        
    except Exception as e:
        # Clean up uploaded file on error
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@router.get("/detections")
async def get_user_detections(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get user's pest detection history"""
    pest_service = PestService(db)
    detections = pest_service.get_user_detections(skip=skip, limit=limit)
    
    return {
        "detections": detections,
        "total": len(detections)
    }

@router.get("/detections/{detection_id}")
async def get_detection_details(
    detection_id: int,
    db: Session = Depends(get_db)
):
    """Get detailed information about a specific detection"""
    pest_service = PestService(db)
    detection = pest_service.get_detection_by_id(detection_id)
    
    if not detection:
        raise HTTPException(status_code=404, detail="Detection not found")
    
    return detection

@router.get("/pests")
async def get_pests_list(
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get list of known pests and diseases"""
    pest_service = PestService(db)
    pests = pest_service.get_pests(category=category)
    
    return {
        "pests": pests,
        "total": len(pests)
    }

@router.get("/pests/{pest_id}")
async def get_pest_details(
    pest_id: int,
    db: Session = Depends(get_db)
):
    """Get detailed information about a specific pest"""
    pest_service = PestService(db)
    pest = pest_service.get_pest_by_id(pest_id)
    
    if not pest:
        raise HTTPException(status_code=404, detail="Pest not found")
    
    return pest
