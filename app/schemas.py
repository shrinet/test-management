from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    username: str
    full_name: str
    password: str
    role: str

class TestCreate(BaseModel):
    title: str

class QuestionCreate(BaseModel):
    test_id: int
    text: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None
