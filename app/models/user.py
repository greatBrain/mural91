from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext

class User(BaseModel):
        __tablename__ = "users"
        id=Column(Integer, primary_key=True, index=True)
        username=Column(String(length=25), index=True)
        user_pass=Column(String, index=False)
        role=Column(String, index=True)

        '''@staticmethod
        def hash_passwd(passwd:str) -> str:
            return password_context.hash(passwd)

        @staticmethod
        def verify_passwd(str_password:str, hashed_passwd:str) -> bool:
            return password_context.verify(hashed_passwd, str_password)'''