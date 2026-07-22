# FaceID-API
پلتفرم هوشمند تشخیص و شناسایی چهره با FastAPI + InsightFace


clone:
    git clone https://github.com/alikhan7939/FaceID-API.git
    cd faceid-api

env:
    python -m venv venv
    source venv/bin/activate    # در ویندوز: venv\Scripts\activate
    pip install -r requirements.txt

Database:
    docker-compose up -d postgres redis

Migration:
    alembic upgrade head

Run:
    uvicorn app.main:app --reload


API Endpoints:
    Method,Endpoint,توضیح
    POST,/api/auth/register,ثبت کاربر جدید
    POST,/api/auth/login,لاگین و دریافت توکن
    POST,/api/face/register,ثبت چهره (نیاز به توکن)
    POST,/api/face/recognize,شناسایی چهره (نیاز به توکن)


Package Used:
    Backend: FastAPI, Uvicorn
    AI: InsightFace, OpenCV
    Database: PostgreSQL + pgvector
    Auth: JWT + bcrypt
    Rate Limit: SlowAPI
    Container: Docker

Structure Of Project:
    app/
        ├── api/endpoints/ 
        ├── core/           # config, security, deps
        ├── models/
        ├── schemas/
        ├── services/
        ├── ml/             # مدل‌های هوش مصنوعی
        └── main.py


Deploy:
    Docker: docker-compose up --build
    Railway / Render: آماده است (فقط Dockerfile و docker-compose.yml کپی کن)
    VPS: با uvicorn + nginx
