"""
Market data schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class MarketPriceResponse(BaseModel):
    prices: List[Dict[str, Any]]
    total: int
    location: Optional[str]

class MarketPrice(BaseModel):
    id: int
    crop_id: int
    location: str
    price_per_quintal: float
    price_per_kg: Optional[float]
    market_name: Optional[str]
    quality_grade: Optional[str]
    trend: Optional[str]
    price_change_percent: Optional[float]
    recorded_at: datetime

class MarketNewsResponse(BaseModel):
    news: List[Dict[str, Any]]
    total: int
    filters: Dict[str, Optional[str]]

class MarketAnalysis(BaseModel):
    location: str
    analysis: Dict[str, Any]
    prices_summary: Dict[str, Any]
    demand_summary: Dict[str, Any]
    news_summary: Dict[str, Any]
