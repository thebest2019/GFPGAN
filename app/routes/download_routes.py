from flask import Blueprint, jsonify, current_app, request
import os
from ..utils.api_response_utils import create_api_response  # Import from the new utility module

download_bp = Blueprint('download', __name__)

@download_bp.route('/download/<filename>', methods=['GET'])
def download_file(filename: str):
    """
    API endpoint to return a URL for the output image.
    """
    # Get the absolute path of the UPLOAD_FOLDER
    upload_folder = current_app.config['UPLOAD_FOLDER']
    absolute_upload_folder = os.path.abspath(upload_folder)

    # Print the absolute path for debugging
    print(f"Absolute path of download: {absolute_upload_folder}")

    # Check if the file exists
    file_path = os.path.join(absolute_upload_folder, filename)
    if not os.path.exists(file_path):
        return jsonify(create_api_response(
            client_id="12345",
            is_success=False,
            message="File not found",
            payload=None
        )), 404

    # Construct the URL for the file
    base_url = request.host_url  # Get the base URL of the server (e.g., http://127.0.0.1:5000/)
    file_url = f"{base_url}file/{filename}"  # Construct the full URL

    # Return the URL in the response
    return jsonify(create_api_response(
        client_id="12345",
        is_success=True,
        message="File URL generated successfully",
        payload={"file_url": file_url}
    )), 200