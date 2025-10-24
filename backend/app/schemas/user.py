"""
User schemas
"""

from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class UserProfile(BaseModel):
    id: int
    email: EmailStr
    username: str
    full_name: Optional[str]
    phone: Optional[str]
    location: Optional[str]
    farm_size: Optional[str]
    bio: Optional[str]
    experience_years: int
    primary_crops: Optional[str]
    farming_method: Optional[str]
    is_verified: bool
    created_at: datetime

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    farm_size: Optional[str] = None
    bio: Optional[str] = None
    experience_years: Optional[int] = None
    primary_crops: Optional[str] = None
    farming_method: Optional[str] = None

class DashboardData(BaseModel):
    user_profile: UserProfile
    farm_statistics: Dict[str, Any]
    recent_activities: List[Dict[str, Any]]
    weather_alerts: List[Dict[str, Any]]
    market_updates: List[Dict[str, Any]]

class FarmStatistics(BaseModel):
    total_crops: int
    active_crops: int
    total_area: float
    recent_detections: int
    forum_posts: int
    advisory_queries: int
