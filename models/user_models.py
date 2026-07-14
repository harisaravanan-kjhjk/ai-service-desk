from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    password:str
    role:str

class LoginRequest(BaseModel):
    name:str
    password:str