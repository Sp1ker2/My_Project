from typing import Sequence

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.models import User
from core.schemas.user import UserCreate
import re
from core.security import hash_password


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_user(user_create: UserCreate, session: AsyncSession):
    # new_user = User(**user_create.model_dump())
    #
    # session.add(new_user)
    hashed_pwd = hash_password(user_create.password)

    new_user = User(
        email=str(user_create.email),
        username=user_create.username,
        hashed_password=hashed_pwd,
    )

    session.add(new_user)

    try:
        await session.commit()
        await session.refresh(new_user)
        print(f"New user ID: {new_user.id}")
        return new_user
    except IntegrityError as e:
        await session.rollback()
        print(f"IntegrityError: {e}")
        if 'email' in str(e.orig):
            raise HTTPException(status_code=400, detail="Email already exists")
        elif 'username' in str(e.orig):
            raise HTTPException(status_code=400, detail="Username already exists")
        else:
            raise HTTPException(status_code=400, detail="Integrity error")
# async def get_all_posts()