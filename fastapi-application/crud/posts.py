# from typing import Sequence
#
# from fastapi import HTTPException
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import session
#
# from core.models import Post
# from core.schemas.post import PostCreate
# import re
# from core.security import hash_password
#
# async def get_all_posts(session: AsyncSession) -> Sequence[Post]:
#     stmt = select(Post).order_by(Post.id)
#     result = await session.scalars(stmt)
#     return result.all()
#
#
# async def create_post(post_create: PostCreate):
#     new_post = Post(title=post_create.title, content=post_create.content, owner_id=post_create.owner_id)
#     session.add(new_post)
#     session.commit(new_post)
#     return new_post
#
# crud/posts.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.models import Post
from core.schemas.post import PostCreate


from sqlalchemy.orm import joinedload

async def get_all_posts(session: AsyncSession):
    stmt = select(Post).options(joinedload(Post.owner)).order_by(Post.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_post(post_create: PostCreate, session: AsyncSession, current_user):
    post_data = post_create.model_dump()
    post_data['owner_id'] = current_user.id  # беремо id з поточного користувача

    new_post = Post(**post_data)

    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)

    return new_post
