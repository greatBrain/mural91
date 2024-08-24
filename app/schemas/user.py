from pydantic import BaseModel
#from passlib.context import CryptContext

#password_context =  CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
        username:str
        user_pass:str
        role:str = 'user'

        '''@staticmethod
        def hash_passwd(passwd:str) -> str:
            return password_context.hash(passwd)

        @staticmethod
        def verify_passwd(str_password:str, hashed_passwd:str) -> bool:
            return password_context.verify(hashed_passwd, str_password)'''
