from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_template.config import SECRET_KEY
from fastapi_template.database import get_db
from fastapi_template.models import Response
from fastapi_template.auth.models import User, UserCreate, UserRead
from fastapi_template.auth.services import create_user

router = APIRouter()


@router.post("/signup", response_model=Response[UserRead])
async def signup_user(
    user_in: UserCreate,
    db_session: Session = Depends(get_db),
    secret: str = SECRET_KEY
):
    user = await create_user(db_session=db_session, user_in=user_in, secret=secret)
    return Response[UserRead](data=user)
