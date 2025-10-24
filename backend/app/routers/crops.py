"""
Crop Recommendation API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.ml_models.crop_recommendation import CropRecommendationModel
from app.schemas.crop import CropRecommendationRequest, CropRecommendationResponse
from app.services.crop_service import CropService
from app.core.config import settings
from typing import Optional

router = APIRouter()

# Initialize ML model
crop_model = CropRecommendationModel(settings.CROP_RECOMMENDATION_MODEL_PATH)

@router.post("/recommend", response_model=CropRecommendationResponse)
async def recommend_crops(
    request: CropRecommendationRequest,
    db: Session = Depends(get_db)
):
    """Get crop recommendations based on farm conditions"""
    
    try:
        # Prepare input data for ML model
        input_data = {
            "temperature": request.temperature,
            "humidity": request.humidity,
            "ph": request.ph,
            "rainfall": request.rainfall,
            "soil_type": request.soil_type,
            "season": request.season,
            "region": request.region,
            "water_requirement": request.water_requirement
        }
        
        # Get ML recommendations
        recommendations = crop_model.recommend_crops(input_data)
        
        # Save recommendation request to database
        crop_service = CropService(db)
        recommendation_record = crop_service.create_recommendation({
            "user_id": request.user_id,
            "input_parameters": input_data,
            "recommendations": recommendations["recommendations"]
        })
        
        return {
            "recommendation_id": recommendation_record.id,
            "recommendations": recommendations["recommendations"],
            "input_parameters": recommendations["input_parameters"],
            "total_crops_analyzed": recommendations["total_crops_analyzed"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@router.get("/crops")
async def get_crops_list(
    category: Optional[str] = None,
    season: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get list of available crops"""
    crop_service = CropService(db)
    crops = crop_service.get_crops(category=category, season=season)
    
    return {
        "crops": crops,
        "total": len(crops)
    }

@router.get("/crops/{crop_id}")
async def get_crop_details(
    crop_id: int,
    db: Session = Depends(get_db)
):
    """Get detailed information about a specific crop"""
    crop_service = CropService(db)
    crop = crop_service.get_crop_by_id(crop_id)
    
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")
    
    return crop

@router.get("/crops/{crop_id}/details")
async def get_crop_ml_details(
    crop_id: int,
    db: Session = Depends(get_db)
):
    """Get ML-based crop details and growing information"""
    crop_service = CropService(db)
    crop = crop_service.get_crop_by_id(crop_id)
    
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")
    
    # Get ML model details for the crop
    ml_details = crop_model.get_crop_details(crop.name)
    
    return {
        "crop_info": crop,
        "ml_details": ml_details
    }

@router.post("/user-crops")
async def add_user_crop(
    user_id: int,
    crop_id: int,
    planting_date: Optional[str] = None,
    area_planted: Optional[float] = None,
    notes: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Add a crop to user's farm"""
    crop_service = CropService(db)
    user_crop = crop_service.add_user_crop({
        "user_id": user_id,
        "crop_id": crop_id,
        "planting_date": planting_date,
        "area_planted": area_planted,
        "notes": notes
    })
    
    return user_crop

@router.get("/user-crops/{user_id}")
async def get_user_crops(
    user_id: int,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get user's planted crops"""
    crop_service = CropService(db)
    user_crops = crop_service.get_user_crops(user_id, status=status)
    
    return {
        "user_crops": user_crops,
        "total": len(user_crops)
    }

@router.put("/user-crops/{user_crop_id}")
async def update_user_crop(
    user_crop_id: int,
    status: Optional[str] = None,
    notes: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Update user crop information"""
    crop_service = CropService(db)
    updated_crop = crop_service.update_user_crop(
        user_crop_id, 
        status=status, 
        notes=notes
    )
    
    if not updated_crop:
        raise HTTPException(status_code=404, detail="User crop not found")
    
    return updated_crop
