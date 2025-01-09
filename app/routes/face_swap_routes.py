from flask import Blueprint, request, jsonify, current_app
import uuid
import os
from werkzeug.utils import secure_filename

from app.services.apply_natural import apply_natural
from ..services.face_swap_service import face_swap
from ..utils.file_utils import allowed_file, validate_file_size, cleanup_files
from ..utils.api_response_utils import create_api_response  # Import the utility function

face_swap_bp = Blueprint('face_swap', __name__)

@face_swap_bp.route('/face_swap', methods=['POST'])
async def face_swap_api():
    """
    API endpoint for face swapping with asynchronous processing.
    """
    # Check if files are provided
    if 'source_image' not in request.files or 'target_image' not in request.files:
        return jsonify(create_api_response(
            client_id="12345",
            is_success=False,
            message="Please provide both source and target images",
            payload=None
        )), 400

    source_image = request.files['source_image']
    target_image = request.files['target_image']

    if source_image.filename == '' or target_image.filename == '':
        return jsonify(create_api_response(
            client_id="12345",
            is_success=False,
            message="No selected file",
            payload=None
        )), 400

    if not (allowed_file(source_image.filename) and allowed_file(target_image.filename)):
        return jsonify(create_api_response(
            client_id="12345",
            is_success=False,
            message="File type not allowed",
            payload=None
        )), 400

    # Validate file sizes
    if not validate_file_size(source_image) or not validate_file_size(target_image):
        return jsonify(create_api_response(
            client_id="12345",
            is_success=False,
            message=f"File size exceeds the maximum limit of {current_app.config['MAX_FILE_SIZE'] / 1024 / 1024} MB",
            payload=None
        )), 400

    # Generate unique filenames using UUID
    source_filename = f"{uuid.uuid4()}_{secure_filename(source_image.filename)}"
    target_filename = f"{uuid.uuid4()}_{secure_filename(target_image.filename)}"
    output_filename = f"{uuid.uuid4()}_{secure_filename(target_image.filename)}"

    source_path = os.path.join(current_app.config['UPLOAD_FOLDER'], source_filename)
    target_path = os.path.join(current_app.config['UPLOAD_FOLDER'], target_filename)
    output_path = os.path.join(current_app.config['UPLOAD_FOLDER'], output_filename)

    # Save the uploaded files
    source_image.save(source_path)
    target_image.save(target_path)

    try:
        # Perform face swapping asynchronously
        await face_swap(source_path, target_path, output_path)

        # Perform image processing with Natural AI
        success = await apply_natural(output_path)
        if not success:
            return jsonify(create_api_response(
                client_id="12345",
                is_success=False,
                message="Face swap successful but failed to apply Natural AI",
                payload=None)), 200

        # Construct the URL for the file
        base_url = request.host_url  # Get the base URL of the server (e.g., http://127.0.0.1:5000/)
        file_url = f"{base_url}file/{output_filename}"

        # Return success response with the output filename
        return jsonify(create_api_response(
            client_id="12345",
            is_success=True,
            message="Face swap successful",
            payload={"file_url": file_url}
        )), 200
    except Exception as e:
        # Return error response
        return jsonify(create_api_response(
            client_id="12345",
            is_success=False,
            message=str(e),
            payload=None
        )), 500
    finally:
        # Clean up source and target images after processing
        cleanup_files(source_path, target_path)