# Serve files from the UPLOAD_FOLDER
from flask import Blueprint, send_from_directory, jsonify, current_app
import os

from app.utils.api_response_utils import create_api_response


file_bp = Blueprint('file', __name__)

@file_bp.route('/file/<filename>')
def uploaded_file(filename):
    """
    API endpoint to return a URL for the output image.
    """
    # Get the absolute path of the UPLOAD_FOLDER
    upload_folder = current_app.config['UPLOAD_FOLDER']
    output_folder = current_app.config['UPLOAD_FOLDER']
    absolute_upload_folder = os.path.abspath(upload_folder)
    absolute_output_folder = os.path.abspath(output_folder)

    # Check if the file exists


    file_path = os.path.join(absolute_output_folder, filename)
    if not os.path.exists(file_path):
        return send_from_directory(absolute_upload_folder, filename, as_attachment=True)

    return send_from_directory(absolute_output_folder, filename, as_attachment=True)