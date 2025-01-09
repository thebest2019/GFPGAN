import cv2
import numpy as np

def load_image(image_path: str, scale_factor=1.24) -> np.ndarray:
    """
    Load an image and increase its resolution by a scale factor while maintaining the aspect ratio.

    Args:
        image_path (str): Path to the input image.
        scale_factor (float): Factor by which to scale the image (default is 1.16 for 16% increase).

    Returns:
        np.ndarray: Resized image.
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Unable to load image from {image_path}")

    # Get original dimensions
    original_height, original_width = image.shape[:2]

    # Calculate new dimensions with 16% increase
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    return resized_image


def sharpen_image(image: np.ndarray) -> np.ndarray:
    """Apply a sharpening filter to the image."""
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)
