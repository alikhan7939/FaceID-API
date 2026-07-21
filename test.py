from insightface.app import FaceAnalysis
import cv2


app = FaceAnalysis(name="buffalo_l", providers={'CPUExecutionProvider'})
app.prepare(ctx_id=0, det_size=(640, 640))


img = cv2.imread("face.jpg")

faces = app.get(img)

for face in faces:
    print(f"cornets: {face.bbox}")
    print(f"key points: {face.kps}")
    print(f"face embedding: {face.embedding}")
    print(f"detection score: {face.det_dcore}")