"""
Forum schemas
"""

from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class ForumPostCreate(BaseModel):
    user_id: int
    title: str
    content: str
    category: Optional[str] = None
    tags: Optional[List[str]] = None

class ForumPostResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    category: Optional[str]
    tags: Optional[List[str]]
    likes_count: int
    comments_count: int
    views_count: int
    is_pinned: bool
    created_at: datetime
    updated_at: Optional[datetime]

class ForumCommentCreate(BaseModel):
    user_id: int
    content: str
    parent_comment_id: Optional[int] = None

class ForumComment(BaseModel):
    id: int
    post_id: int
    user_id: int
    content: str
    parent_comment_id: Optional[int]
    likes_count: int
    created_at: datetime
