from typing import Sequence
from core.security import verify_password, create_access_token

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

async def authenticate_user(username: str, password: str, session: AsyncSession):
    user = await get_user_by_username(username, session)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user

async def login_user(username: str, password: str, session: AsyncSession):
    user = await authenticate_user(username, password, session)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer", "user": user}

from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy import select
from core.models.user import User

# CRUD операция для бана пользователя
async def ban_user(username: str, ban_duration: int, session: AsyncSession):
    user = await get_user_by_username(username, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_banned_until and user.is_banned_until > datetime.now():
        raise HTTPException(status_code=403, detail=f"User is already banned until {user.is_banned_until}")

    user.is_banned_until = datetime.now() + timedelta(minutes=ban_duration)
    user.ban_count += 1
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
        return {"message": f"User {username} has been banned for {ban_duration} minutes."}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# CRUD операция для разблокировки пользователя
async def unban_user(username: str, session: AsyncSession):
    user = await get_user_by_username(username, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_banned_until = None
    session.add(user)
    try:
        await session.commit()
        await session.refresh(user)
        return {"message": f"User {username} has been unbanned."}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Получение пользователя по имени

async def get_user_by_username(username: str, session: AsyncSession) -> User | None:
    stmt = select(User).where(User.username == username)
    result = await session.scalars(stmt)
    return result.first()
