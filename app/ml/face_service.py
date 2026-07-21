import insightface
import cv2
import numpy as np
from PIL import Image
import io

class FaceService:
    def __init__(self):
        # مدل ArcFace
        self.model = insightface.app.FaceAnalysis(
            name='buffalo_l', 
            providers=['CPUExecutionProvider']
        )
        self.model.prepare(ctx_id=0, det_size=(640, 640))

    def get_embedding(self, image_bytes: bytes):
        """تبدیل عکس به embedding"""
        image = Image.open(io.BytesIO(image_bytes))
        image_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        faces = self.model.get(image_np)
        
        if len(faces) == 0:
            raise ValueError("هیچ چهره‌ای در عکس پیدا نشد")
        
        # قوی‌ترین چهره
        face = max(faces, key=lambda x: x.det_score)
        return face.embedding.tolist()

face_service = FaceService()