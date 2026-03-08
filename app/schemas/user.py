import email
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    name: str
    address: str
    email: str
    password: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int       # Unique ID of the user
    name: str     # Name of the user
    email: str    # Email of the user

class userLogin(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str