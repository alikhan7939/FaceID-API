from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., example="ali_ahmadi", min_length=3, max_length=50)
    email: EmailStr = Field(..., example="ali@example.com")
    password: str = Field(..., example="123456", min_length=6)
    full_name: Optional[str] = Field(None, example="علی احمدی")

class Token(BaseModel):
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    token_type: str = "bearer"