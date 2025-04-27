from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from core.models import db_helper
from core.schemas.user import UserRead, UserCreate
from crud import users as user_crud

# from core.config import ApiV1Prefix as v1
router = APIRouter(tags=["users"])


@router.get("", response_model=list[UserRead], responses={404: {"description": "Not found"}})
async def get_users(session: Annotated[AsyncSession] = Depends(db_helper.session_getter)):
    users = await user_crud.get_all_users(session=session)
    return users


@router.post("",
             response_model=UserRead,
             responses={404: {"description": "Not found"}})
async def create_user(user_create: UserCreate,
                      session: Annotated[AsyncSession]
                      = Depends(db_helper.session_getter)
                      ):
    user = await user_crud.create_user(
        session=session,
        user_create=user_create)
    return user


# @router.post("/", response_model=UserRead)
# async def create_user(
#         user_create: UserCreate,
#         session: Annotated[AsyncSession] = Depends(db_helper.session_getter)
# ):
#     user = await user_crud.create_user(session=session, user_create=user_create)
#     return user
