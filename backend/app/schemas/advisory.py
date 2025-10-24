"""
AI Advisory schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class AdvisoryRequest(BaseModel):
    user_id: int
    query: str
    context: Optional[Dict[str, Any]] = None

class AdvisoryResponse(BaseModel):
    conversation_id: int
    response: str
    recommendations: List[Dict[str, Any]]
    related_topics: List[str]
    confidence_score: float

class QuickAction(BaseModel):
    id: int
    title: str
    description: str
    category: str
    prompt: str
    icon: Optional[str] = None

class PersonalizedRecommendation(BaseModel):
    type: str
    title: str
    description: str
    priority: str
    action_items: List[str]
