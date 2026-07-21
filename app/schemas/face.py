from pydantic import BaseModel, Field
from typing import List, Optional

class FaceRegisterResponse(BaseModel):
    message: str = Field(..., example="چهره با موفقیت ثبت شد")
    user_id: str = Field(..., example="user123")

class FaceMatch(BaseModel):
    user_id: str = Field(..., example="user123")
    name: str = Field(..., example="علی احمدی")
    similarity: float = Field(..., example=92.5, description="درصد شباهت")

class FaceRecognizeResponse(BaseModel):
    matches: List[FaceMatch]
    message: str = Field(..., example="شناسایی انجام شد")