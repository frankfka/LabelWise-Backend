from typing import Optional

from flask import g
from flask_restful import Resource, reqparse

from server.api.api import analyze
from server.authentication import authenticate
from server.models import ErrorResponse
from server.services import AppServices


class ProcessTextEndpoint(Resource):
    method_decorators = [authenticate]

    TEXT_ARG = "text"
    TYPE_ARG = "type"

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument(ProcessTextEndpoint.TEXT_ARG, type=str,
                            help="Parsed nutritional label text", required=True, location='json')
        parser.add_argument(ProcessTextEndpoint.TYPE_ARG, type=str,
                            help="Type of label (nutrition/ingredient)", required=True, location='json')
        self.services: AppServices = g.services
        self.req_parser = parser

    def post(self):
        args = self.__get_args_from_req()
        if not args:
            return ErrorResponse("Invalid request, required inputs not provided").to_dict(), 400
        return analyze(type=args[0], text=args[1], services=self.services)

    def __get_args_from_req(self) -> Optional[tuple]:
        """
        Return (req_type, text), or None if we are missing any inputs
        """
        args = self.req_parser.parse_args()  # Not using strict to allow for key arg
        req_type = args.get(ProcessTextEndpoint.TYPE_ARG, None)
        text = args.get(ProcessTextEndpoint.TEXT_ARG, None)
        # Check we have correct input
        if req_type is None or text is None:
            return None
        return req_type, text
