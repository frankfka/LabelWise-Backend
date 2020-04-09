from typing import List

from nutrition_analysis_service.models import NutritionWarning
import nutrition_analysis_service.nutrition_checks as checks
from nutrition_parser.models import ParsedNutritionResult


class NutritionAnalysisService:

    def __init__(self):
        pass

    def get_warnings(self, nutrition: ParsedNutritionResult) -> List[NutritionWarning]:
        warnings: List[NutritionWarning] = [
            checks.check_sodium(nutrition),
            checks.check_sugar(nutrition),
            checks.check_fiber(nutrition)
        ]
        warnings = list(filter(lambda warning: warning is not None, warnings))
        return warnings

