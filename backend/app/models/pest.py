"""
Pest and disease models for pest detection system
"""

from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.database.connection import Base

class Pest(Base):
    __tablename__ = "pests"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    scientific_name = Column(String(150), nullable=True)
    category = Column(String(50), nullable=False)  # Insect, Disease, Fungus, etc.
    affected_crops = Column(JSON, nullable=True)  # List of crop IDs
    symptoms = Column(Text, nullable=True)
    damage_description = Column(Text, nullable=True)
    prevention_methods = Column(Text, nullable=True)
    treatment_methods = Column(Text, nullable=True)
    severity_level = Column(String(20), nullable=True)  # Low, Medium, High, Critical
    season_occurrence = Column(String(100), nullable=True)  # When it typically occurs
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class PestDetection(Base):
    __tablename__ = "pest_detections"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    image_path = Column(String(500), nullable=False)
    detected_pest_id = Column(Integer, nullable=True, index=True)
    confidence_score = Column(Float, nullable=True)  # ML model confidence
    detection_date = Column(DateTime(timezone=True), server_default=func.now())
    location = Column(String(255), nullable=True)
    crop_affected = Column(String(100), nullable=True)
    severity = Column(String(20), nullable=True)
    treatment_recommended = Column(Text, nullable=True)
    is_verified = Column(Boolean, default=False)  # User verification
    notes = Column(Text, nullable=True)
