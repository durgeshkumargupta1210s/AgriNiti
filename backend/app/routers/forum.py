"""
Forum API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.forum import ForumPostCreate, ForumPostResponse, ForumCommentCreate
from app.services.forum_service import ForumService
from typing import Optional

router = APIRouter()

@router.post("/posts", response_model=ForumPostResponse)
async def create_post(
    post_data: ForumPostCreate,
    db: Session = Depends(get_db)
):
    """Create a new forum post"""
    forum_service = ForumService(db)
    
    try:
        post = forum_service.create_post(post_data)
        return post
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating post: {str(e)}")

@router.get("/posts")
async def get_posts(
    category: Optional[str] = None,
    tags: Optional[str] = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """Get forum posts with optional filtering"""
    forum_service = ForumService(db)
    
    try:
        posts = forum_service.get_posts(
            category=category,
            tags=tags,
            skip=skip,
            limit=limit
        )
        
        return {
            "posts": posts,
            "total": len(posts),
            "filters": {
                "category": category,
                "tags": tags
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching posts: {str(e)}")

@router.get("/posts/{post_id}")
async def get_post_details(
    post_id: int,
    db: Session = Depends(get_db)
):
    """Get detailed information about a specific post"""
    forum_service = ForumService(db)
    
    try:
        post = forum_service.get_post_by_id(post_id)
        
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        
        # Increment view count
        forum_service.increment_view_count(post_id)
        
        return post
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching post: {str(e)}")

@router.post("/posts/{post_id}/comments")
async def add_comment(
    post_id: int,
    comment_data: ForumCommentCreate,
    db: Session = Depends(get_db)
):
    """Add a comment to a post"""
    forum_service = ForumService(db)
    
    try:
        comment = forum_service.add_comment(post_id, comment_data)
        return comment
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding comment: {str(e)}")

@router.get("/posts/{post_id}/comments")
async def get_post_comments(
    post_id: int,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """Get comments for a specific post"""
    forum_service = ForumService(db)
    
    try:
        comments = forum_service.get_post_comments(
            post_id=post_id,
            skip=skip,
            limit=limit
        )
        
        return {
            "comments": comments,
            "total": len(comments)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching comments: {str(e)}")

@router.post("/posts/{post_id}/like")
async def like_post(
    post_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    """Like or unlike a post"""
    forum_service = ForumService(db)
    
    try:
        result = forum_service.toggle_like(post_id, user_id, "post")
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error liking post: {str(e)}")

@router.post("/comments/{comment_id}/like")
async def like_comment(
    comment_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    """Like or unlike a comment"""
    forum_service = ForumService(db)
    
    try:
        result = forum_service.toggle_like(comment_id, user_id, "comment")
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error liking comment: {str(e)}")

@router.get("/trending")
async def get_trending_topics(
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Get trending topics and tags"""
    forum_service = ForumService(db)
    
    try:
        trending = forum_service.get_trending_topics(limit=limit)
        return trending
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching trending topics: {str(e)}")

@router.get("/categories")
async def get_categories(
    db: Session = Depends(get_db)
):
    """Get available forum categories"""
    forum_service = ForumService(db)
    
    try:
        categories = forum_service.get_categories()
        return {
            "categories": categories
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching categories: {str(e)}")
