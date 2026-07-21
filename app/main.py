from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.rate_limit import add_rate_limit_middleware
from app.api.endpoints.face import router as face_router
from app.api.endpoints.auth import router as auth_router

app = FastAPI(
    title="FaceID API",
    description=""" 
    پلتفرم هوشمند تشخیص و شناسایی چهره با FastAPI + InsightFace
    
    ویژگی‌ها:
    - ثبت و شناسایی چهره
    - احراز هویت JWT
    - ذخیره embedding در PostgreSQL + pgvector
    """,
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your@email.com",
    },
    license_info={
        "name": "MIT",
    },
    openapi_tags=[
        {"name": "Authentication", "description": "ثبت‌نام و لاگین کاربران"},
        {"name": "Face Recognition", "description": "عملیات تشخیص و ثبت چهره"},
    ]
)
# Rate Limiting
add_rate_limit_middleware(app=app)
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FaceID API is running 🚀"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

app.include_router(face_router)
app.include_router(auth_router)