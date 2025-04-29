from fastapi import APIRouter, Depends, HTTPException, Form
from core.schemas.user import UserCreate, UserLogin, UserRead
from crud.users import create_user, login_user, get_user_by_username
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from fastapi.security import OAuth2PasswordBearer
from core.security import create_access_token, verify_token, get_current_user

router = APIRouter(tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

@router.post("/register", response_model=UserRead)
async def register_user(user_create: UserCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    return await create_user(user_create, session)

@router.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    user = await login_user(username, password, session)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

