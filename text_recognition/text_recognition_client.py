import base64

from google.cloud import vision

from text_recognition.models import TextRecognitionResult
from utils.logging_util import get_logger

logger = get_logger("TextRecognitionClient")


class TextRecognitionClient:

    def __init__(self, credentials_filepath):
        self.client = vision.ImageAnnotatorClient.from_service_account_file(credentials_filepath)

    def detect_b64(self, b64_img_content: str) -> TextRecognitionResult:
        """
        Takes as input a Base64 encoded image string
        """
        try:
            byte_content = base64.b64decode(b64_img_content)
        except Exception as e:
            logger.error(f"Error decoding Base64 image: {e}", exc_info=True)
            return TextRecognitionResult(error="Invalid Base64 image string")
        return self.detect_bytes(byte_content)

    def detect_bytes(self, byte_img_content: bytes):
        image = vision.types.Image(content=byte_img_content)
        response = self.client.text_detection(image=image)
        return TextRecognitionResult.from_response(response)
