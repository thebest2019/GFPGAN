import insightface
from insightface.app import FaceAnalysis
import numpy as np
from ..config import MODELS_NAME, MODELS_FOLDER

# Initialize InsightFace models
face_app = FaceAnalysis(name='buffalo_l')
face_app.prepare(ctx_id=0, det_size=(640, 640))

# Load the face swapper model
swapper = insightface.model_zoo.get_model(f'{MODELS_FOLDER}/{MODELS_NAME}', download=False)

def detect_faces(image: np.ndarray) -> list:
    """Detect faces in the given image."""
    faces = face_app.get(image)
    if not faces:
        raise ValueError("No faces detected in the image.")
    return faces