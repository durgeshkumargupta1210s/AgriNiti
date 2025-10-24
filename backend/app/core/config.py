"""
Configuration settings for FARMER Backend
"""

from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FARMER"
    VERSION: str = "1.0.0"
    
    # Database
    DATABASE_URL: str = "postgresql://farmer:farmer123@localhost:5432/farmer_db"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # External APIs
    OPENWEATHER_API_KEY: str = "your-openweather-api-key"
    MARKET_DATA_API_KEY: str = "your-market-data-api-key"
    
    # ML Models
    PEST_DETECTION_MODEL_PATH: str = "app/ml_models/pest_detection_model.h5"
    CROP_RECOMMENDATION_MODEL_PATH: str = "app/ml_models/crop_recommendation_model.pkl"
    
    # File Upload
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_IMAGE_TYPES: list = ["image/jpeg", "image/png", "image/jpg"]
    
    # CORS
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    
    class Config:
        env_file = ".env"

settings = Settings()
