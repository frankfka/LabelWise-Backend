from typing import Dict


class ErrorResponse:

    def __init__(self, message=""):
        self.message = message

    def to_response_dict(self) -> Dict:
        return {
            "message": self.message
        }