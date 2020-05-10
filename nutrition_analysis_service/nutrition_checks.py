from typing import Optional

from nutrition_analysis_service.models import NutritionInsight, NutritionInsightCode
from nutrition_parser.models import ParsedNutritionResult


def check_sodium(nutrition: ParsedNutritionResult) -> Optional[NutritionInsight]:
    result = None
    if nutrition.sodium is None:
        pass
    # Severe Warning
    elif nutrition.sodium > 800:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_SODIUM, insight_type=NutritionInsight.Type.WARN_SEVERE)
    # Caution warning
    elif nutrition.calories is not None and nutrition.sodium > nutrition.calories:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_SODIUM, insight_type=NutritionInsight.Type.WARN_CAUTION)
    # Low sodium: https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/sodium/art-20045479
    elif nutrition.sodium < 140:
        result = NutritionInsight(code=NutritionInsightCode.LOW_SODIUM, insight_type=NutritionInsight.Type.POSITIVE)
    return result


def check_sugar(nutrition: ParsedNutritionResult) -> Optional[NutritionInsight]:
    result = None
    if nutrition.sugar is None:
        pass
    # Severe Warning
    elif nutrition.sugar > 20:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_SUGAR, insight_type=NutritionInsight.Type.WARN_SEVERE)
    # Caution warning
    elif nutrition.sugar > 10 or \
            (nutrition.sugar > 2 and nutrition.protein is not None and nutrition.fiber is not None
             and nutrition.sugar > nutrition.protein + nutrition.fiber):  # Sugar > Protein + Fiber
        result = NutritionInsight(code=NutritionInsightCode.HIGH_SUGAR, insight_type=NutritionInsight.Type.WARN_CAUTION)
    # Low sugar - less than 10% of calories
    elif nutrition.calories and nutrition.sugar * 4 < nutrition.calories * 0.1:
        result = NutritionInsight(code=NutritionInsightCode.LOW_SUGAR, insight_type=NutritionInsight.Type.POSITIVE)
    return result


def check_fiber(nutrition: ParsedNutritionResult) -> Optional[NutritionInsight]:
    result = None
    if not nutrition.fiber: # This checks that it is non-zero as well, as we divide by 0
        pass
    # Caution warning
    elif nutrition.carbohydrates and nutrition.carbohydrates > 10 and nutrition.carbohydrates / nutrition.fiber > 5:
        result = NutritionInsight(code=NutritionInsightCode.LOW_FIBER, insight_type=NutritionInsight.Type.WARN_CAUTION)
    # High fiber - more than 5g
    elif nutrition.fiber > 5:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_FIBER, insight_type=NutritionInsight.Type.POSITIVE)
    return result


def check_sat_fat(nutrition: ParsedNutritionResult) -> Optional[NutritionInsight]:
    result = None
    if nutrition.saturated_fat is None:
        pass
    elif nutrition.saturated_fat > 10:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_SAT_FAT, insight_type=NutritionInsight.Type.WARN_SEVERE)
    elif nutrition.saturated_fat > 5:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_SAT_FAT, insight_type=NutritionInsight.Type.WARN_CAUTION)
    return result


def check_cholesterol(nutrition: ParsedNutritionResult) -> Optional[NutritionInsight]:
    result = None
    if nutrition.cholesterol is None:
        pass
    elif nutrition.cholesterol > 200:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_CHOLESTEROL, insight_type=NutritionInsight.Type.WARN_SEVERE)
    elif nutrition.cholesterol > 100:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_CHOLESTEROL, insight_type=NutritionInsight.Type.WARN_CAUTION)
    return result


def check_protein(nutrition: ParsedNutritionResult) -> Optional[NutritionInsight]:
    result = None
    if nutrition.protein is None:
        pass
    elif nutrition.protein > 10:
        result = NutritionInsight(code=NutritionInsightCode.HIGH_PROTEIN, insight_type=NutritionInsight.Type.POSITIVE)
    return result
