from typing import Optional

from nutrition_analysis_service.models import NutritionWarning, NutritionWarningCode
from nutrition_parser.models import ParsedNutritionResult


def check_sodium(nutrition: ParsedNutritionResult) -> Optional[NutritionWarning]:
    # Check parse requirements
    result = None
    if nutrition.sodium is None or nutrition.calories is None:
        return result
    if nutrition.sodium > nutrition.calories:
        # TODO: Assign warning level depending on sodium level
        result = NutritionWarning(code=NutritionWarningCode.HIGH_SODIUM, level=NutritionWarning.Level.CAUTION)
    return result
