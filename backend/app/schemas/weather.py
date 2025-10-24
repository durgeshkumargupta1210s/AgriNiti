"""
Weather schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class WeatherDataResponse(BaseModel):
    location: str
    temperature: float
    humidity: float
    wind_speed: float
    wind_direction: float
    pressure: float
    rainfall: float
    uv_index: float
    visibility: float
    weather_condition: str
    recorded_at: datetime

class WeatherForecast(BaseModel):
    date: str
    temperature_min: float
    temperature_max: float
    humidity: float
    rainfall_probability: float
    weather_condition: str

class WeatherAlertResponse(BaseModel):
    id: int
    location: str
    alert_type: str
    severity: str
    message: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    is_active: bool
    created_at: datetime
