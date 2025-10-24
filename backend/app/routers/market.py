"""
Market Data API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.market import MarketPriceResponse, MarketNewsResponse
from app.services.market_service import MarketService
from app.core.config import settings
from typing import Optional
import httpx

router = APIRouter()

@router.get("/prices", response_model=MarketPriceResponse)
async def get_market_prices(
    location: Optional[str] = None,
    crop_id: Optional[int] = None,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """Get current market prices for crops"""
    market_service = MarketService(db)
    
    try:
        # Get prices from database
        prices = market_service.get_market_prices(
            location=location,
            crop_id=crop_id,
            limit=limit
        )
        
        # If no data in database, fetch from external API
        if not prices and location:
            external_prices = await fetch_external_prices(location)
            if external_prices:
                # Save external data to database
                for price_data in external_prices:
                    market_service.create_price_record(price_data)
                prices = market_service.get_market_prices(location=location, limit=limit)
        
        return {
            "prices": prices,
            "total": len(prices),
            "location": location
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching market prices: {str(e)}")

@router.get("/prices/{crop_id}/trend")
async def get_price_trend(
    crop_id: int,
    days: int = 30,
    db: Session = Depends(get_db)
):
    """Get price trend for a specific crop"""
    market_service = MarketService(db)
    
    try:
        trend_data = market_service.get_price_trend(crop_id, days)
        
        return {
            "crop_id": crop_id,
            "period_days": days,
            "trend_data": trend_data,
            "trend_analysis": market_service.analyze_price_trend(trend_data)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing price trend: {str(e)}")

@router.get("/demand")
async def get_market_demand(
    location: Optional[str] = None,
    crop_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """Get market demand information"""
    market_service = MarketService(db)
    
    try:
        demand_data = market_service.get_market_demand(
            location=location,
            crop_id=crop_id
        )
        
        return {
            "demand_data": demand_data,
            "total": len(demand_data),
            "location": location
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching demand data: {str(e)}")

@router.get("/news")
async def get_market_news(
    crop_related: Optional[str] = None,
    location: Optional[str] = None,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get market news and updates"""
    market_service = MarketService(db)
    
    try:
        news = market_service.get_market_news(
            crop_related=crop_related,
            location=location,
            limit=limit
        )
        
        return {
            "news": news,
            "total": len(news),
            "filters": {
                "crop_related": crop_related,
                "location": location
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching market news: {str(e)}")

@router.get("/analysis/{location}")
async def get_market_analysis(
    location: str,
    db: Session = Depends(get_db)
):
    """Get comprehensive market analysis for a location"""
    market_service = MarketService(db)
    
    try:
        # Get current prices
        prices = market_service.get_market_prices(location=location)
        
        # Get demand data
        demand = market_service.get_market_demand(location=location)
        
        # Get recent news
        news = market_service.get_market_news(location=location, limit=10)
        
        # Perform analysis
        analysis = market_service.perform_market_analysis(prices, demand, news)
        
        return {
            "location": location,
            "analysis": analysis,
            "prices_summary": market_service.get_prices_summary(prices),
            "demand_summary": market_service.get_demand_summary(demand),
            "news_summary": market_service.get_news_summary(news)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error performing market analysis: {str(e)}")

async def fetch_external_prices(location: str):
    """Fetch market prices from external API"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.marketdata.com/prices",
                params={
                    "location": location,
                    "api_key": settings.MARKET_DATA_API_KEY
                }
            )
            
            if response.status_code == 200:
                return response.json()
            return None
            
    except Exception as e:
        print(f"Error fetching external prices: {e}")
        return None
