"""
Pest detection schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class PestDetectionCreate(BaseModel):
    image_path: str
    location: Optional[str] = None
    crop_affected: Optional[str] = None
    user_id: int

class PestDetectionResponse(BaseModel):
    detection_id: int
    image_path: str
    primary_prediction: Dict[str, Any]
    all_predictions: List[Dict[str, Any]]
    treatment_recommendations: Dict[str, List[str]]
    is_healthy: bool
    confidence_threshold: float

class PestInfo(BaseModel):
    id: int
    name: str
    scientific_name: Optional[str]
    category: str
    symptoms: Optional[str]
    prevention_methods: Optional[str]
    treatment_methods: Optional[str]
    severity_level: Optional[str]
