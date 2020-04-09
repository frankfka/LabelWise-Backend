from typing import Optional

from nutrition_analysis_service.models import NutritionWarning, NutritionWarningCode
from nutrition_parser.models import ParsedNutritionResult


def check_sodium(nutrition: ParsedNutritionResult) -> Optional[NutritionWarning]:
    result = None
    if nutrition.sodium is None:
        pass
    elif nutrition.sodium > 800:
        result = NutritionWarning(code=NutritionWarningCode.HIGH_SODIUM, level=NutritionWarning.Level.SEVERE)
    elif nutrition.calories is not None and nutrition.sodium > nutrition.calories:
        result = NutritionWarning(code=NutritionWarningCode.HIGH_SODIUM, level=NutritionWarning.Level.CAUTION)
    return result


def check_sugar(nutrition: ParsedNutritionResult) -> Optional[NutritionWarning]:
    result = None
    if nutrition.sugar is None:
        pass
    elif nutrition.sugar > 20:
        result = NutritionWarning(code=NutritionWarningCode.HIGH_SUGAR, level=NutritionWarning.Level.SEVERE)
    elif nutrition.sugar > 10 or \
            (nutrition.sugar > 2 and nutrition.protein is not None and nutrition.fiber is not None
             and nutrition.sugar > nutrition.protein + nutrition.fiber):
        result = NutritionWarning(code=NutritionWarningCode.HIGH_SUGAR, level=NutritionWarning.Level.CAUTION)
    return result


def check_fiber(nutrition: ParsedNutritionResult) -> Optional[NutritionWarning]:
    result = None
    if nutrition.carbohydrates is None or nutrition.fiber is None:
        pass
    elif nutrition.carbohydrates > 10 and nutrition.carbohydrates / nutrition.fiber > 5:
        result = NutritionWarning(code=NutritionWarningCode.LOW_FIBER, level=NutritionWarning.Level.CAUTION)
    return result

# TODO
def check_trans_fats(nutrition: ParsedNutritionResult) -> Optional[NutritionWarning]:
    return None


def check_sat_fat(nutrition: ParsedNutritionResult) -> Optional[NutritionWarning]:
    return None


def check_cholesterol(nutrition: ParsedNutritionResult) -> Optional[NutritionWarning]:
    return None