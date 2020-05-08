from nutrition_parser.models import ParsedNutritionResult
from server.models import NutritionAnalysisResponse, IngredientsAnalysisResponse, ErrorResponse, TYPE_NUTRITION, \
    TYPE_INGREDIENTS
from server.services import AppServices

"""
Central methods that endpoints will call to get the relevant information
- All methods MUST return a valid tuple of (response_dict, response_code?), no response_code implies a 200
"""


def analyze(text: str, type: str, services: AppServices) -> (dict, int):
    if type == TYPE_NUTRITION:
        return __analyze_nutrition__(text, services)
    elif type == TYPE_INGREDIENTS:
        return __analyze_ingredients__(text, services)
    else:
        return ErrorResponse("Invalid analysis type"), 400


def __analyze_nutrition__(text: str, services: AppServices) -> (dict, int):
    parse_result = services.nutrition_parser.parse(text)
    warnings = services.nutrition_analyzer.get_warnings(parse_result)
    # Determine the status
    status = __get_analyze_nutrition_status__(parse_result)
    response = NutritionAnalysisResponse(
        status=status,
        parsed_nutrition=parse_result,
        warnings=warnings
    )
    return response.to_dict(), 200


def __get_analyze_nutrition_status__(parse_result: ParsedNutritionResult) -> NutritionAnalysisResponse.Status:
    if parse_result.calories is None or parse_result.carbohydrates is None \
            or parse_result.protein is None or parse_result.fat is None:
        # Insufficient if we can't parse any macros
        return NutritionAnalysisResponse.Status.INSUFFICIENT

    # Determine whether we have parsed all properties
    if parse_result.did_parse_all():
        return NutritionAnalysisResponse.Status.SUCCESS
    else:
        return NutritionAnalysisResponse.Status.INCOMPLETE


def __analyze_ingredients__(text: str, services: AppServices) -> (dict, int):
    parse_result = services.ingredient_parser.parse(text)
    analyzed_additives = services.ingredient_analyzer.analyze(parse_result)
    response = IngredientsAnalysisResponse(
        parsed_ingredients=parse_result,
        analyzed_additives=analyzed_additives
    )
    return response.to_dict(), 200
