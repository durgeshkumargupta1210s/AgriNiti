"""
User management API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserProfile, UserUpdate
from app.services.user_service import UserService
from typing import Optional

router = APIRouter()

@router.get("/profile/{user_id}", response_model=UserProfile)
async def get_user_profile(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get user profile information"""
    user_service = UserService(db)
    
    try:
        user = user_service.get_user_by_id(user_id)
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user profile: {str(e)}")

@router.put("/profile/{user_id}")
async def update_user_profile(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
):
    """Update user profile information"""
    user_service = UserService(db)
    
    try:
        updated_user = user_service.update_user(user_id, user_update)
        
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return updated_user
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating user profile: {str(e)}")

@router.get("/dashboard/{user_id}")
async def get_user_dashboard(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get user dashboard data"""
    user_service = UserService(db)
    
    try:
        dashboard_data = user_service.get_dashboard_data(user_id)
        return dashboard_data
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching dashboard data: {str(e)}")

@router.get("/farm-stats/{user_id}")
async def get_farm_statistics(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get user's farm statistics"""
    user_service = UserService(db)
    
    try:
        farm_stats = user_service.get_farm_statistics(user_id)
        return farm_stats
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching farm statistics: {str(e)}")

@router.get("/activity/{user_id}")
async def get_user_activity(
    user_id: int,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get user's recent activity"""
    user_service = UserService(db)
    
    try:
        activities = user_service.get_user_activity(
            user_id=user_id,
            skip=skip,
            limit=limit
        )
        
        return {
            "activities": activities,
            "total": len(activities)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user activity: {str(e)}")

@router.delete("/account/{user_id}")
async def delete_user_account(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Delete user account (soft delete)"""
    user_service = UserService(db)
    
    try:
        result = user_service.delete_user(user_id)
        
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {
            "message": "Account deleted successfully",
            "user_id": user_id
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting account: {str(e)}")
