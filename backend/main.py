"""
FARMER Backend API
Agricultural Intelligence Platform with ML Models
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
import uvicorn
import os
from dotenv import load_dotenv

# Import routers
from app.routers import auth, users, crops, pests, weather, market, forum, advisory
from app.database import engine, Base
from app.core.config import settings

# Load environment variables
load_dotenv()

# Create database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    pass

# Initialize FastAPI app
app = FastAPI(
    title="FARMER API",
    description="Agricultural Intelligence Platform with ML Models",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(crops.router, prefix="/api/crops", tags=["Crops"])
app.include_router(pests.router, prefix="/api/pests", tags=["Pest Detection"])
app.include_router(weather.router, prefix="/api/weather", tags=["Weather"])
app.include_router(market.router, prefix="/api/market", tags=["Market Data"])
app.include_router(forum.router, prefix="/api/forum", tags=["Forum"])
app.include_router(advisory.router, prefix="/api/advisory", tags=["AI Advisory"])

@app.get("/")
async def root():
    return {
        "message": "FARMER API - Agricultural Intelligence Platform",
        "version": "1.0.0",
        "status": "active"
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "FARMER Backend"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
