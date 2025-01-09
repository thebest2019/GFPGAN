from flask import Flask
from .config import OUTPUT_FOLDER, UPLOAD_FOLDER, MAX_FILE_SIZE
from .routes.face_swap_routes import face_swap_bp
from .routes.download_routes import download_bp
from .routes.file_routes import file_bp

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

    # Register blueprints
    app.register_blueprint(face_swap_bp)
    app.register_blueprint(download_bp)
    app.register_blueprint(file_bp)

    return app