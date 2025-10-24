"""
Weather data models for weather tracking and forecasting
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.database.connection import Base

class WeatherData(Base):
    __tablename__ = "weather_data"
    
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String(255), nullable=False, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    wind_speed = Column(Float, nullable=True)
    wind_direction = Column(Float, nullable=True)
    pressure = Column(Float, nullable=True)
    rainfall = Column(Float, nullable=True)
    uv_index = Column(Float, nullable=True)
    visibility = Column(Float, nullable=True)
    weather_condition = Column(String(100), nullable=True)  # Sunny, Rainy, Cloudy, etc.
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
    forecast_data = Column(JSON, nullable=True)  # 7-day forecast data

class WeatherAlert(Base):
    __tablename__ = "weather_alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    location = Column(String(255), nullable=False, index=True)
    alert_type = Column(String(50), nullable=False)  # Storm, Drought, Flood, etc.
    severity = Column(String(20), nullable=False)  # Low, Medium, High, Critical
    message = Column(String(500), nullable=False)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
