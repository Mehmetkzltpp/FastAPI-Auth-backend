import datetime

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str


    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str

class TagResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class PostResponseWithTags(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    owner_id: int
    tags: list[TagResponse] = []

    class Config:
        from_attributes = True

