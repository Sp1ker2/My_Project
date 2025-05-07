from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.schemas.post import PostRead, PostCreate
from crud import posts as posts_crud
from core.security import get_current_user
from datetime import datetime
from fastapi import Depends
from core.models.user import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.responses import Response

from core.models.likes import Likes
from core.models.user import User
from core.models.db_helper import db_helper
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
    if current_user.is_banned_until and current_user.is_banned_until > datetime.now():
        raise HTTPException(status_code=403, detail="User is banned and cannot create posts")

    return await posts_crud.create_post(post_create=post_create, session=session, current_user=current_user)




@router.put("/posts/{post_id}/like", status_code=204)
async def like_post(
    post_id: int,
    db: AsyncSession = Depends(db_helper.get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Likes).where(Likes.user_id == user.id, Likes.post_id == post_id)
    )
    existing_like = result.scalar_one_or_none()

    if existing_like:
        raise HTTPException(status_code=400, detail="Already liked")

    # Добавляем лайк
    new_like = Likes(user_id=user.id, post_id=post_id)
    db.add(new_like)
    await db.commit()
    return Response(status_code=204)

@router.delete("/posts/{post_id}/like", status_code=204)
async def unlike_post(
    post_id: int,
    db: AsyncSession = Depends(db_helper.get_db),
    user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Likes).where(Likes.user_id == user.id, Likes.post_id == post_id)
    )
    like = result.scalar_one_or_none()

    if not like:
        raise HTTPException(status_code=404, detail="Like not found")

    await db.delete(like)
    await db.commit()
    return Response(status_code=204)
