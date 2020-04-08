from flask import g
from flask_restful import Resource, reqparse

from server.models import ErrorResponse
from server.services import AppServices
from text_recognition.models import TextRecognitionResult


class ProcessImageEndpoint(Resource):

    IMAGE_ARG = "b64_img"

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument(ProcessImageEndpoint.IMAGE_ARG, type=str,
                            help="Base64 encoded image string", required=True, location='json')
        self.services: AppServices = g.services
        self.req_parser = parser

    def post(self):
        img = self.__get_img_from_req()
        if not img:
            return ErrorResponse("No image provided").to_response_dict(), 400
        text_recognition_result: TextRecognitionResult = self.services.text_recognition_client.detect(img)
        if text_recognition_result.error or not text_recognition_result.text:
            return ErrorResponse(text_recognition_result.error).to_response_dict(), 500
        parse_result = self.services.nutrition_parser.parse(text_recognition_result.text)
        return parse_result.to_dict()

    def __get_img_from_req(self):
        args = self.req_parser.parse_args(strict=True)
        return args.get(ProcessImageEndpoint.IMAGE_ARG, None)
