from enum import Enum
from typing import Dict, List

from ingredients.analysis.models import AnalyzedIngredient
from ingredients.parser.models import ParsedIngredientsResult
from nutrition_analysis_service.models import NutritionInsight
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
    class Status(Enum):
        COMPLETE = "COMPLETE"
        INCOMPLETE = "INCOMPLETE"
        INSUFFICIENT = "INSUFFICIENT"

    def __init__(self,
                 status: Status,
                 parsed_nutrition: ParsedNutritionResult,
                 insights: List[NutritionInsight]):
        self.status = status
        self.parsed_nutrition = parsed_nutrition
        self.insights = insights

    def to_dict(self) -> dict:
        return {
            "status": self.status.value,
            "parsed_nutrition": self.parsed_nutrition.to_dict(),
            "insights": [insight.to_dict() for insight in self.insights]
        }


class IngredientsAnalysisResponse:
    """
    Standardized response for ingredients analysis and parsing
    """

    def __init__(self,
                 parsed_ingredients: ParsedIngredientsResult,
                 analyzed_additives: List[AnalyzedIngredient]):
        self.parsed_ingredients = parsed_ingredients
        self.analyzed_additives = analyzed_additives

    def to_dict(self) -> dict:
        return {
            "parsed_ingredients": self.parsed_ingredients.to_dict(),
            "analyzed_additives": [additive.to_dict() for additive in self.analyzed_additives]
        }