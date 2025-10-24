"""
Crop model for crop management and recommendations
"""

from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database.connection import Base

class Crop(Base):
    __tablename__ = "crops"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    scientific_name = Column(String(150), nullable=True)
    category = Column(String(50), nullable=False)  # Cereals, Vegetables, Fruits, etc.
    season = Column(String(20), nullable=False)  # Kharif, Rabi, Zaid
    duration_days = Column(Integer, nullable=False)  # Growing period in days
    water_requirement = Column(String(20), nullable=True)  # Low, Medium, High
    soil_type = Column(String(100), nullable=True)  # Clay, Loamy, Sandy, etc.
    temperature_min = Column(Float, nullable=True)  # Minimum temperature
    temperature_max = Column(Float, nullable=True)  # Maximum temperature
    rainfall_min = Column(Float, nullable=True)  # Minimum rainfall
    rainfall_max = Column(Float, nullable=True)  # Maximum rainfall
    ph_min = Column(Float, nullable=True)  # Minimum pH
    ph_max = Column(Float, nullable=True)  # Maximum pH
    yield_per_hectare = Column(Float, nullable=True)  # Expected yield
    market_price = Column(Float, nullable=True)  # Current market price
    description = Column(Text, nullable=True)
    growing_tips = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class UserCrop(Base):
    __tablename__ = "user_crops"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    crop_id = Column(Integer, nullable=False, index=True)
    planting_date = Column(DateTime, nullable=True)
    expected_harvest_date = Column(DateTime, nullable=True)
    area_planted = Column(Float, nullable=True)  # Area in hectares
    status = Column(String(20), default="planted")  # planted, growing, harvested
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
