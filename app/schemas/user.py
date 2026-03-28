from pydantic import BaseModel, ConfigDict, Field


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


class UserDetails(BaseModel):
    """Partial update for the current user (PATCH). Omit fields you do not want to change."""

    name: str | None = Field(default=None, min_length=1)
    address: str | None = None


class MessageResponse(BaseModel):
    message: str
