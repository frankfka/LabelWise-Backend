import base64
import os

from config import AppTestConfig
from nutrition_parser.nutrition_parser_service import NutritionalDetailParser
from text_recognition.text_recognition_client import TextRecognitionClient

config = AppTestConfig()

def analyze(filepath):
    text_recog = TextRecognitionClient(config.vision_cred_filepath)
    parser_service = NutritionalDetailParser()

    with open(filepath, "rb") as image_file:
        b64_img = base64.b64encode(image_file.read())

    text_rec_res = text_recog.detect_b64(b64_img)
    parse_result = parser_service.parse(text_rec_res.text)

    print(parse_result.to_dict())


if __name__ == '__main__':
    path = os.path.join(config.test_assets_dir, "IMG_5290.jpg")
    analyze(path)