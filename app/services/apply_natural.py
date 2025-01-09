import subprocess
import os

async def apply_natural(image_path: str) -> bool:
    """
    Apply the GFPGAN model to enhance the image quality using a subprocess.
    Runs the command:
    python inference_gfpgan.py -i image_path -o outputs -s 3
    Returns True if the command succeeds, False otherwise.
    """

    # Validate the input image path
    if not os.path.exists(image_path):
        print(f"Error: The image path '{image_path}' does not exist.")
        return False

    # Define the command
    command = [
        "python",
        "inference_gfpgan.py",
        "-i", image_path,
        "-o", "outputs",
        "-v", "1.3",
        "-s", "2"
    ]

    # Run the subprocess
    try:
        print(f"Running command: {' '.join(command)}")
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check subprocess result
        if result.returncode == 0:
            print(f"Subprocess completed successfully:\n{result.stdout}")
            return True
        else:
            print(f"Error in subprocess:\n{result.stderr}")
            return False
    except Exception as e:
        print(f"Error running subprocess: {e}")
        return False
