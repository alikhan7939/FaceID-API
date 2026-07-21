from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Query, Form
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.deps import get_current_user
from app.schemas.face import FaceRegisterResponse, FaceRecognizeResponse
from app.services.face_service import face_db_service
from app.ml.face_service import face_service
from app.models.user import User
from pydantic import Field
from slowapi import Limiter
from app.core.rate_limit import limiter
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Form, Request

from slowapi import Limiter
from app.core.rate_limit import limiter
from app.core.deps import get_current_user

router = APIRouter(prefix="/api/face", tags=["Face Recognition"])

@router.post("/register", response_model=FaceRegisterResponse)
@limiter.limit("10/minute")   # ۱۰ درخواست در دقیقه
async def register_face(
    request: Request,                    # <--- این خط خیلی مهمه
    user_id: str = Form(...),
    name: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    content = await file.read()
    
    try:
        embedding = face_service.get_embedding(content)
        face_db_service.register_face(db, user_id, name, embedding)
        return {"message": "چهره با موفقیت ثبت شد", "user_id": user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/recognize", response_model=FaceRecognizeResponse)
@limiter.limit("20/minute")
async def recognize_face(
    request: Request,                    # <--- اضافه کن
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    content = await file.read()
    
    try:
        embedding = face_service.get_embedding(content)
        matches = face_db_service.find_similar(db, embedding)
        
        if not matches:
            return {"matches": [], "message": "هیچ چهره مشابهی پیدا نشد"}
        
        return {"matches": matches, "message": "شناسایی انجام شد"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))