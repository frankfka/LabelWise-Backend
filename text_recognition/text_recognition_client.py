import base64

from google.cloud import vision

from text_recognition.models import TextRecognitionResult


class TextRecognitionClient:

    def __init__(self, credentials_filepath):
        self.client = vision.ImageAnnotatorClient.from_service_account_file(credentials_filepath)

    def detect(self, b64_img_content: str) -> TextRecognitionResult:
        """
        Takes as input a Base64 encoded image string
        """
        try:
            byte_content = base64.b64decode(b64_img_content)
        except Exception:
            return TextRecognitionResult(error="Invalid Base64 image string")
        image = vision.types.Image(content=byte_content)
        response = self.client.text_detection(image=image)
        return TextRecognitionResult.from_response(response)
