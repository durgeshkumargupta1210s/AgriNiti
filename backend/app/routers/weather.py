"""
Weather API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.weather import WeatherDataResponse, WeatherAlertResponse
from app.services.weather_service import WeatherService
from app.core.config import settings
from typing import Optional
import httpx

router = APIRouter()

@router.get("/current/{location}", response_model=WeatherDataResponse)
async def get_current_weather(
    location: str,
    db: Session = Depends(get_db)
):
    """Get current weather data for a location"""
    weather_service = WeatherService(db)
    
    try:
        # Get weather data from external API
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"http://api.openweathermap.org/data/2.5/weather",
                params={
                    "q": location,
                    "appid": settings.OPENWEATHER_API_KEY,
                    "units": "metric"
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="Weather data not available")
            
            weather_data = response.json()
        
        # Process and save weather data
        processed_data = weather_service.process_weather_data(weather_data, location)
        
        return {
            "location": location,
            "temperature": processed_data["temperature"],
            "humidity": processed_data["humidity"],
            "wind_speed": processed_data["wind_speed"],
            "wind_direction": processed_data["wind_direction"],
            "pressure": processed_data["pressure"],
            "rainfall": processed_data["rainfall"],
            "uv_index": processed_data["uv_index"],
            "visibility": processed_data["visibility"],
            "weather_condition": processed_data["weather_condition"],
            "recorded_at": processed_data["recorded_at"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching weather data: {str(e)}")

@router.get("/forecast/{location}")
async def get_weather_forecast(
    location: str,
    days: int = 7,
    db: Session = Depends(get_db)
):
    """Get weather forecast for a location"""
    weather_service = WeatherService(db)
    
    try:
        # Get forecast data from external API
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"http://api.openweathermap.org/data/2.5/forecast",
                params={
                    "q": location,
                    "appid": settings.OPENWEATHER_API_KEY,
                    "units": "metric",
                    "cnt": days * 8  # 8 data points per day (3-hour intervals)
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="Forecast data not available")
            
            forecast_data = response.json()
        
        # Process forecast data
        processed_forecast = weather_service.process_forecast_data(forecast_data, location)
        
        return {
            "location": location,
            "forecast_days": days,
            "forecast": processed_forecast
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching forecast: {str(e)}")

@router.get("/alerts/{user_id}")
async def get_weather_alerts(
    user_id: int,
    active_only: bool = True,
    db: Session = Depends(get_db)
):
    """Get weather alerts for a user"""
    weather_service = WeatherService(db)
    alerts = weather_service.get_user_alerts(user_id, active_only=active_only)
    
    return {
        "alerts": alerts,
        "total": len(alerts)
    }

@router.post("/alerts")
async def create_weather_alert(
    user_id: int,
    location: str,
    alert_type: str,
    severity: str,
    message: str,
    db: Session = Depends(get_db)
):
    """Create a weather alert for a user"""
    weather_service = WeatherService(db)
    alert = weather_service.create_alert({
        "user_id": user_id,
        "location": location,
        "alert_type": alert_type,
        "severity": severity,
        "message": message
    })
    
    return alert

@router.get("/historical/{location}")
async def get_historical_weather(
    location: str,
    days: int = 30,
    db: Session = Depends(get_db)
):
    """Get historical weather data for a location"""
    weather_service = WeatherService(db)
    historical_data = weather_service.get_historical_data(location, days)
    
    return {
        "location": location,
        "period_days": days,
        "historical_data": historical_data
    }

@router.get("/farming-conditions/{location}")
async def get_farming_conditions(
    location: str,
    db: Session = Depends(get_db)
):
    """Get farming-specific weather conditions and recommendations"""
    weather_service = WeatherService(db)
    
    # Get current weather
    current_weather = await get_current_weather(location, db)
    
    # Analyze farming conditions
    farming_analysis = weather_service.analyze_farming_conditions(current_weather)
    
    return {
        "location": location,
        "current_weather": current_weather,
        "farming_analysis": farming_analysis,
        "recommendations": weather_service.get_farming_recommendations(farming_analysis)
    }
