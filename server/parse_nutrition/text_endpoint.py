from typing import Any

from flask import g
from flask_restful import Resource, reqparse

from server.models import ErrorResponse
from server.services import AppServices
from text_recognition.models import TextRecognitionResult


class ProcessTextEndpoint(Resource):

    TEXT_ARG = "label_text"

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument(ProcessTextEndpoint.TEXT_ARG, type=str,
                            help="Parsed nutritional label text", required=True, location='json')
        self.services: AppServices = g.services
        self.req_parser = parser

    def post(self):
        label_text = self.__get_label_text_from_req()
        if not label_text:
            return ErrorResponse("No text provided").to_response_dict(), 400
        parse_result = self.services.nutrition_parser.parse(label_text)
        return parse_result.to_dict()

    def __get_label_text_from_req(self):
        args = self.req_parser.parse_args(strict=True)
        return args.get(ProcessTextEndpoint.TEXT_ARG, None)
