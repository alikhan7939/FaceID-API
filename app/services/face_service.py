from sqlalchemy.orm import Session
from app.models.face import FaceEmbedding
from app.ml.face_service import face_service
import numpy as np

class FaceServiceDB:
    def register_face(self, db: Session, user_id: str, name: str, embedding: list):
        face = FaceEmbedding(
            user_id=user_id,
            name=name,
            embedding=embedding
        )
        db.add(face)
        db.commit()
        db.refresh(face)
        return face

    def find_similar(self, db: Session, embedding: list, threshold: float = 0.6):
        faces = db.query(FaceEmbedding).all()
        matches = []

        for face in faces:
            similarity = 1 - (np.linalg.norm(np.array(face.embedding) - np.array(embedding)) / 2)
            if similarity >= threshold:
                matches.append({
                    "user_id": face.user_id,
                    "name": face.name,
                    "similarity": round(similarity * 100, 2)
                })

        return sorted(matches, key=lambda x: x["similarity"], reverse=True)

face_db_service = FaceServiceDB()