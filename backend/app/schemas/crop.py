"""
Crop recommendation schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class CropRecommendationRequest(BaseModel):
    user_id: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    soil_type: str
    season: str
    region: str
    water_requirement: str

class CropRecommendation(BaseModel):
    crop_name: str
    confidence: float
    yield_per_hectare: float
    market_price: float
    water_requirement: str
    season: str
    suitability_score: float

class CropRecommendationResponse(BaseModel):
    recommendation_id: int
    recommendations: List[CropRecommendation]
    input_parameters: Dict[str, Any]
    total_crops_analyzed: int

class CropInfo(BaseModel):
    id: int
    name: str
    scientific_name: Optional[str]
    category: str
    season: str
    duration_days: int
    water_requirement: Optional[str]
    soil_type: Optional[str]
    yield_per_hectare: Optional[float]
    market_price: Optional[float]
