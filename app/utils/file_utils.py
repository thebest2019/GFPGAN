import os
from typing import List
from ..config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE

def allowed_file(filename: str) -> bool:
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file_size(file) -> bool:
    """Validate that the file size is within the allowed limit."""
    file.seek(0, os.SEEK_END)  # Move to the end of the file
    file_size = file.tell()  # Get the file size
    file.seek(0)  # Reset the file pointer
    return file_size <= MAX_FILE_SIZE

def cleanup_files(*file_paths: str) -> None:
    """Remove files from the filesystem."""
    for file_path in file_paths:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")