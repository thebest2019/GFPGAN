import asyncio
import cv2
from ..utils.image_utils import load_image, sharpen_image
from ..models.face_model import detect_faces, swapper

async def face_swap(source_image_path: str, target_image_path: str, output_image_path: str) -> None:
    """
    Perform face swapping between the source and target images asynchronously.
    """
    # Load images
    source_image = load_image(source_image_path)
    target_image = load_image(target_image_path)

    # Detect faces in the images
    source_faces = detect_faces(source_image)
    target_faces = detect_faces(target_image)

    if not source_faces or not target_faces:
        raise ValueError("No faces detected in one or both images.")

    # Swap faces (use the first detected face in each image)
    result_image = swapper.get(target_image, target_faces[0], source_faces[0], paste_back=True)

    # Apply post-processing
    # result_image = sharpen_image(result_image)

    # Save the output image
    cv2.imwrite(output_image_path, result_image)