from typing import Dict, List

from ingredients.analysis.models import AnalyzedAdditive
from ingredients.parser.models import ParsedIngredientsResult
from nutrition_analysis_service.models import NutritionWarning
from nutrition_parser.models import ParsedNutritionResult

# Analysis types
TYPE_NUTRITION = "nutrition"
TYPE_INGREDIENTS = "ingredients"


class ErrorResponse:
    """
    Standardized error response to return from the API
    """

    def __init__(self, message=""):
        self.message = message

    def to_dict(self) -> dict:
        return {
            "message": self.message
        }


class NutritionAnalysisResponse:
    """
    Standardized response for nutrition analysis and parsing
    """

    def __init__(self,
                 parsed_nutrition: ParsedNutritionResult,
                 warnings: List[NutritionWarning]):
        self.parsed_nutrition = parsed_nutrition
        self.warnings = warnings

    def to_dict(self) -> dict:
        return {
            "parsed_nutrition": self.parsed_nutrition.to_dict(),
            "warnings": [warning.to_dict() for warning in self.warnings]
        }


class IngredientsAnalysisResponse:
    """
    Standardized response for ingredients analysis and parsing
    """

    def __init__(self,
                 parsed_ingredients: ParsedIngredientsResult,
                 analyzed_additives: List[AnalyzedAdditive]):
        self.parsed_ingredients = parsed_ingredients
        self.analyzed_additives = analyzed_additives

    def to_dict(self) -> dict:
        return {
            "parsed_ingredients": self.parsed_ingredients.to_dict(),
            "analyzed_additives": [additive.to_dict() for additive in self.analyzed_additives]
        }