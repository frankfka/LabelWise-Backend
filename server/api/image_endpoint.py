from typing import Optional

from flask import g
from flask_restful import Resource, reqparse

from server.api.api import analyze
from server.models import ErrorResponse
from server.services import AppServices
from text_recognition.models import TextRecognitionResult


class ProcessImageEndpoint(Resource):
    IMAGE_ARG = "b64_img"
    TYPE_ARG = "type"

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument(ProcessImageEndpoint.IMAGE_ARG, type=str,
                            help="Base64 encoded image string", required=True, location='json')
        parser.add_argument(ProcessImageEndpoint.TYPE_ARG, type=str,
                            help="Type of label (nutrition/ingredient)", required=True, location='json')
        self.services: AppServices = g.services
        self.req_parser = parser

    def post(self):
        args = self.__get_args_from_req()
        if not args:
            return ErrorResponse("Invalid request, required inputs not provided").to_dict(), 400
        text_recognition_result: TextRecognitionResult = self.services.text_recognition_client.detect(args[1])
        if text_recognition_result.error or not text_recognition_result.text:
            return ErrorResponse(text_recognition_result.error).to_dict(), 500
        return analyze(text=text_recognition_result.text, type=args[0], services=self.services)

    def __get_args_from_req(self) -> Optional[tuple]:
        """
        Return (req_type, b64_img), or None if we are missing any inputs
        """
        args = self.req_parser.parse_args(strict=True)
        req_type = args.get(ProcessImageEndpoint.TYPE_ARG, None)
        b64_img = args.get(ProcessImageEndpoint.IMAGE_ARG, None)
        # Check we have correct input
        if req_type is None or b64_img is None:
            return None
        return req_type, b64_img

