from nutrition_parser.models import ParsedNutritionResult
from server.models import NutritionAnalysisResponse, IngredientsAnalysisResponse, ErrorResponse, TYPE_NUTRITION, \
    TYPE_INGREDIENTS
from server.services import AppServices
from utils.logging_util import get_logger

"""
Central methods that endpoints will call to get the relevant information
- All methods MUST return a valid tuple of (response_dict, response_code?), no response_code implies a 200
"""

logger = get_logger("APIServer")


def analyze(text: str, analyze_type: str, services: AppServices) -> (dict, int):
    if analyze_type == TYPE_NUTRITION:
        return __analyze_nutrition__(text, services)
    elif analyze_type == TYPE_INGREDIENTS:
        return __analyze_ingredients__(text, services)
    else:
        logger.info(f"Invalid request. Given analyze type: {analyze_type}")
        return ErrorResponse("Invalid analysis type").to_dict(), 400


def __analyze_nutrition__(text: str, services: AppServices) -> (dict, int):
    parse_result = services.nutrition_parser.parse(text)
    insights = services.nutrition_analyzer.get_insights(parse_result)
    # Determine the status
    status = __get_analyze_nutrition_status__(parse_result)
    response = NutritionAnalysisResponse(
        status=status,
        parsed_nutrition=parse_result,
        insights=insights
    )
    return response.to_dict(), 200


def __get_analyze_nutrition_status__(parse_result: ParsedNutritionResult) -> NutritionAnalysisResponse.Status:
    if parse_result.calories is None or parse_result.carbohydrates is None \
            or parse_result.protein is None or parse_result.fat is None:
        # Insufficient if we can't parse any macros
        return NutritionAnalysisResponse.Status.INSUFFICIENT

    # Determine whether we have parsed all properties
    if parse_result.did_parse_all():
        return NutritionAnalysisResponse.Status.COMPLETE
    else:
        return NutritionAnalysisResponse.Status.INCOMPLETE


def __analyze_ingredients__(text: str, services: AppServices) -> (dict, int):
    parse_result = services.ingredient_parser.parse(text)
    analyzed_ingredients = services.ingredient_analyzer.analyze(parse_result)
    response = IngredientsAnalysisResponse(
        parsed_ingredients=parse_result,
        analyzed_ingredients=analyzed_ingredients
    )
    return response.to_dict(), 200
