class TextRecognitionResult:

    @classmethod
    def from_response(cls, client_resp):
        error = client_resp.error.message
        text = ""
        if client_resp.text_annotations:
            # The first item should contain the full text, the subsequent items are individual words
            text = client_resp.text_annotations[0].description
        return TextRecognitionResult(
            text=text,
            error=error
        )

    def __init__(self, text: str = "", error: str = ""):
        self.error = error
        self.text = text
