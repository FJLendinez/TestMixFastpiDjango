from datetime import datetime, timedelta
from typing import Optional

import jwt
from django.conf import settings
from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from starlette import status

from users.models import UserModel
from users.schemas import TokenData

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    try:
        return UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        raise credentials_exception


def get_admin_user(user: UserModel = Depends(get_current_user)):
    if user.is_admin:
        return user
    raise HTTPException(status_code=400, detail="User is not admin")
