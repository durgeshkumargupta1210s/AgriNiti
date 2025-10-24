"""
Market data models for crop prices and market information
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.database.connection import Base

class MarketPrice(Base):
    __tablename__ = "market_prices"
    
    id = Column(Integer, primary_key=True, index=True)
    crop_id = Column(Integer, nullable=False, index=True)
    location = Column(String(255), nullable=False, index=True)
    price_per_quintal = Column(Float, nullable=False)
    price_per_kg = Column(Float, nullable=True)
    market_name = Column(String(255), nullable=True)
    quality_grade = Column(String(50), nullable=True)  # A, B, C grade
    trend = Column(String(20), nullable=True)  # up, down, stable
    price_change_percent = Column(Float, nullable=True)
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
    source = Column(String(100), nullable=True)  # API source

class MarketDemand(Base):
    __tablename__ = "market_demand"
    
    id = Column(Integer, primary_key=True, index=True)
    crop_id = Column(Integer, nullable=False, index=True)
    location = Column(String(255), nullable=False, index=True)
    demand_level = Column(String(20), nullable=False)  # Low, Medium, High
    demand_trend = Column(String(20), nullable=True)  # increasing, decreasing, stable
    seasonal_factor = Column(Float, nullable=True)  # Seasonal demand multiplier
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())

class MarketNews(Base):
    __tablename__ = "market_news"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    content = Column(String(2000), nullable=True)
    crop_related = Column(String(100), nullable=True)  # Related crops
    location = Column(String(255), nullable=True)
    impact_level = Column(String(20), nullable=True)  # Low, Medium, High
    news_date = Column(DateTime, nullable=True)
    source = Column(String(200), nullable=True)
    url = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
