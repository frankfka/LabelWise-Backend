import io
from typing import Optional

import werkzeug
from flask import g
from flask_restful import Resource, reqparse

from server.api.api import analyze
from server.authentication import authenticate
from server.models import ErrorResponse
from server.services import AppServices
from text_recognition.models import TextRecognitionResult
from utils.logging_util import get_logger

logger = get_logger("ProcessImageUploadEndpoint")


class ProcessImageUploadEndpoint(Resource):
    method_decorators = [authenticate]

    IMAGE_ARG = "img"
    TYPE_ARG = "type"

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument(ProcessImageUploadEndpoint.IMAGE_ARG, type=werkzeug.datastructures.FileStorage,
                            help="Image to Analyze", required=True, location='files')
        parser.add_argument(ProcessImageUploadEndpoint.TYPE_ARG, type=str,
                            help="Type of label (nutrition/ingredient)", required=True, location='form')
        self.services: AppServices = g.services
        self.req_parser = parser

    def post(self):
        args = self.__get_args_from_req()
        if not args:
            return ErrorResponse("Invalid request, required inputs not provided").to_dict(), 400
        text_recognition_result: TextRecognitionResult = self.services.text_recognition_client.detect_bytes(args[1])
        if text_recognition_result.error or not text_recognition_result.text:
            logger.warn(f"Could not parse text from image: {text_recognition_result.error}")
            return ErrorResponse(text_recognition_result.error).to_dict(), 500
        return analyze(text=text_recognition_result.text, analyze_type=args[0], services=self.services)

    def __get_args_from_req(self) -> Optional[tuple]:
        """
        Return (req_type, img_byte_content), or None if we are missing any inputs
        """
        args = self.req_parser.parse_args(strict=True)
        req_type = args.get(ProcessImageUploadEndpoint.TYPE_ARG, None)
        img = args.get(ProcessImageUploadEndpoint.IMAGE_ARG, None)
        # Check we have correct input
        if req_type is None or img is None:
            return None
        # Read file into bytes
        return req_type, img.read()

