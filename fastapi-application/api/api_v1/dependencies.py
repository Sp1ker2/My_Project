# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.ext.asyncio import AsyncSession
# from core.models import db_helper
# from crud.users import get_user_by_username
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
#
# async def get_current_user(
#     session: AsyncSession = Depends(db_helper.session_getter),
#     token: str = Depends(oauth2_scheme)
# ):
#     user = await get_user_by_username(token, session)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Could not validate credentials",
#         )
#     return user
