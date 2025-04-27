import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext


from jose import JWTError, jwt
from fastapi import HTTPException


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#
#         expiration_time = datetime.fromtimestamp(payload.get("exp"))
#         if expiration_time < datetime.utcnow():
#             raise HTTPException(status_code=401, detail="Token expired")
#
#         if "sub" not in payload:
#             raise HTTPException(status_code=401, detail="Token does not contain subject (sub)")
#
#         return payload
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")
from jose import ExpiredSignatureError, JWTError


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration_time = datetime.utcfromtimestamp(payload.get("exp"))

        if expiration_time < datetime.utcnow():
            raise HTTPException(status_code=401, detail="Token expired")

        if "sub" not in payload:
            raise HTTPException(status_code=401, detail="Token does not contain subject (sub)")

        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

