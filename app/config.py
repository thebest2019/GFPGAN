import os

# Configuration
UPLOAD_FOLDER = 'inputs/uploads'  # Path to the uploads directory
OUTPUT_FOLDER = 'outputs/restored_imgs'  # Path to the uploads directory
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
MAX_FILE_SIZE = 25 * 1024 * 1024  # 10 MB
MODELS_FOLDER = 'experiments/pretrained_models'  # Path to the models directory
MODELS_NAME = 'inswapper_128.onnx'  # Name of the face swapper model

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)