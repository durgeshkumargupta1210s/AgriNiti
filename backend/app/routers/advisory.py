"""
AI Advisory API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.advisory import AdvisoryRequest, AdvisoryResponse
from app.services.advisory_service import AdvisoryService
from typing import Optional

router = APIRouter()

@router.post("/chat", response_model=AdvisoryResponse)
async def get_ai_advice(
    request: AdvisoryRequest,
    db: Session = Depends(get_db)
):
    """Get AI-powered farming advice"""
    advisory_service = AdvisoryService(db)
    
    try:
        # Process the user query
        advice = advisory_service.process_query(
            query=request.query,
            user_id=request.user_id,
            context=request.context
        )
        
        # Save the conversation
        conversation = advisory_service.save_conversation({
            "user_id": request.user_id,
            "query": request.query,
            "response": advice["response"],
            "context": request.context
        })
        
        return {
            "conversation_id": conversation.id,
            "response": advice["response"],
            "recommendations": advice["recommendations"],
            "related_topics": advice["related_topics"],
            "confidence_score": advice["confidence_score"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing advisory request: {str(e)}")

@router.get("/conversations/{user_id}")
async def get_user_conversations(
    user_id: int,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get user's conversation history"""
    advisory_service = AdvisoryService(db)
    
    try:
        conversations = advisory_service.get_user_conversations(
            user_id=user_id,
            skip=skip,
            limit=limit
        )
        
        return {
            "conversations": conversations,
            "total": len(conversations)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching conversations: {str(e)}")

@router.get("/quick-actions")
async def get_quick_actions(
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get quick action suggestions for common farming queries"""
    advisory_service = AdvisoryService(db)
    
    try:
        quick_actions = advisory_service.get_quick_actions(category=category)
        return {
            "quick_actions": quick_actions
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching quick actions: {str(e)}")

@router.get("/recommendations/{user_id}")
async def get_personalized_recommendations(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get personalized farming recommendations based on user profile"""
    advisory_service = AdvisoryService(db)
    
    try:
        recommendations = advisory_service.get_personalized_recommendations(user_id)
        return {
            "recommendations": recommendations,
            "user_id": user_id
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@router.get("/knowledge-base")
async def get_knowledge_base(
    topic: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get farming knowledge base articles"""
    advisory_service = AdvisoryService(db)
    
    try:
        articles = advisory_service.get_knowledge_base(
            topic=topic,
            category=category,
            limit=limit
        )
        
        return {
            "articles": articles,
            "total": len(articles),
            "filters": {
                "topic": topic,
                "category": category
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching knowledge base: {str(e)}")

@router.post("/feedback")
async def submit_feedback(
    conversation_id: int,
    rating: int,
    feedback_text: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Submit feedback for AI advisory responses"""
    advisory_service = AdvisoryService(db)
    
    try:
        feedback = advisory_service.submit_feedback({
            "conversation_id": conversation_id,
            "rating": rating,
            "feedback_text": feedback_text
        })
        
        return {
            "feedback_id": feedback.id,
            "message": "Feedback submitted successfully"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error submitting feedback: {str(e)}")
