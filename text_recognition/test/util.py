import base64
import io

from text_recognition.text_recognition_client import TextRecognitionClient


def get_image(path) -> str:
    with io.open(path, 'rb') as f:
        return base64.b64encode(f.read())


def get_image_b64(path) -> str:
    with io.open(path, 'r') as f:
        return f.read()


def get_client(cred_path="../../assets/credentials.json"):
    return TextRecognitionClient(cred_path)