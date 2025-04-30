from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from core.models.db_helper import db_helper
from core.schemas.post import PostRead, PostCreate
from crud import posts as posts_crud
from core.security import get_current_user
from datetime import datetime
from fastapi import Depends, HTTPException
from core.models.user import User
router = APIRouter(tags=["posts"])

@router.get("/posts", response_model=list[PostRead], responses={404: {"description": "Not found"}})
async def get_posts(session: AsyncSession = Depends(db_helper.session_getter)):
    posts = await posts_crud.get_all_posts(session=session)
    return posts

@router.post("/posts", response_model=PostRead)
async def create_post(
    post_create: PostCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
    current_user: User = Depends(get_current_user)
):
    return await posts_crud.create_post(post_create=post_create, session=session, current_user=current_user)
