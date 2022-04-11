import bcrypt
from sqlalchemy import Column, Integer, LargeBinary, String

from fastapi_template.database import Base
from fastapi_template.models import FastApiTemplateBase, PrimaryKey, TimeStampMixin


class User(Base, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String(4), nullable=False)
    username = Column(String(16), unique=True)
    email = Column(String(256), unique=True)
    password = Column(LargeBinary, nullable=False)

    def check_password(self, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), self.password)


class UserBase(FastApiTemplateBase):
    pass


class UserCreate(UserBase):
    name: str
    username: str
    email: str
    password: str


class UserRead(UserBase):
    id: PrimaryKey
    name: str
    username: str
    email: str


class UserUpdate(UserBase):
    id: PrimaryKey
    username: str
    password: str


class UserDelete(UserBase):
    id: PrimaryKey
