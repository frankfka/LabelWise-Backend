from ingredients.analysis.ingredients_analysis_service import IngredientsAnalysisService
from ingredients.parser.ingredient_parser_service import IngredientsParser
from nutrition_analysis_service.nutrition_analysis_service import NutritionAnalysisService
from nutrition_parser.nutrition_parser_service import NutritionalDetailParser
from text_recognition.text_recognition_client import TextRecognitionClient


class AppServices:
    """
    Services for use by the server
    """

    def __init__(self, google_cred_path: str, additive_db_path: str):
        self.text_recognition_client = TextRecognitionClient(google_cred_path)
        self.nutrition_parser = NutritionalDetailParser()
        self.nutrition_analyzer = NutritionAnalysisService()
        self.ingredient_parser = IngredientsParser()
        self.ingredient_analyzer = IngredientsAnalysisService(additive_db_path)


class AppServiceSingleton:
    """
    The singleton instance of the above AppServices. This is injected into the global Flask object
    """
    instance: AppServices = None

    def __init__(self, google_cred_path: str, additive_db_path: str):
        if not AppServiceSingleton.instance:
            AppServiceSingleton.instance = AppServices(google_cred_path, additive_db_path)

    def __getattr__(self, name):
        return getattr(self.instance, name)