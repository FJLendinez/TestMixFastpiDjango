from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from users.models import UserModel
from users.schemas import UserSignUp, UserSignUpOut, Token
from users.utils import create_access_token, get_current_user

router = APIRouter()


@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserModel.login(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=UserSignUpOut)
def register(user: UserSignUp):
    user = UserModel.register(user.username, user.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return user


@router.get("/me/")
async def read_logged_user(current_user=Depends(get_current_user)):
    return current_user