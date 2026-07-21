from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from pgvector.sqlalchemy import Vector
from app.core.database import Base

class FaceEmbedding(Base):
    __tablename__ = "face_embeddings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    embedding = Column(Vector(512))          # ArcFace embedding dimension
    image_path = Column(String, nullable=True)
    created_at = Column(String)  # می‌تونی از datetime استفاده کنی