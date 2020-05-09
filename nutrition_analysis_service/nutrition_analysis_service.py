from typing import List

from nutrition_analysis_service.models import NutritionInsight
import nutrition_analysis_service.nutrition_checks as checks
from nutrition_parser.models import ParsedNutritionResult


class NutritionAnalysisService:

    def __init__(self):
        pass

    def get_insights(self, nutrition: ParsedNutritionResult) -> List[NutritionInsight]:
        insights: List[NutritionInsight] = [
            checks.check_sodium(nutrition),
            checks.check_sugar(nutrition),
            checks.check_fiber(nutrition),
            checks.check_sat_fat(nutrition),
            checks.check_cholesterol(nutrition)
        ]
        insights = list(filter(lambda insight: insight is not None, insights))
        return insights

