from pydantic import BaseModel, ConfigDict, Field, model_validator


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
    """Partial update for the current user (PATCH). Send at least one field with a value."""

    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(
        default=None,
        min_length=1,
        description="New display name (omit if unchanged).",
    )
    address: str | None = Field(
        default=None,
        min_length=1,
        description="New address (omit if unchanged).",
    )


class MessageResponse(BaseModel):
    message: str
