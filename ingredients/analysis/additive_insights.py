from typing import List

from ingredients.analysis.database.models import AdditiveInfo
from ingredients.analysis.models import IngredientInsight, IngredientInsightCode, IngredientInsightLevel


def get_insights_for_additive(additive: AdditiveInfo) -> List[IngredientInsight]:
    insights: List[IngredientInsight] = []
    insights.extend(__check_scogs__(additive))
    return insights


def __check_scogs__(additive: AdditiveInfo) -> List[IngredientInsight]:
    scogs_conclusion = additive.scogs_conclusion
    insight_code: IngredientInsightCode = IngredientInsightCode.NOT_GRAS
    insight_level: IngredientInsightLevel = IngredientInsightLevel.WARN_SEVERE
    if scogs_conclusion:
        if scogs_conclusion == "1":
            insight_code = IngredientInsightCode.SCOGS_1
            insight_level = IngredientInsightLevel.POSITIVE
        elif scogs_conclusion == "2":
            insight_code = IngredientInsightCode.SCOGS_2
            insight_level = IngredientInsightLevel.POSITIVE
        elif scogs_conclusion == "3":
            insight_code = IngredientInsightCode.SCOGS_3
            insight_level = IngredientInsightLevel.WARN_CAUTION
        elif scogs_conclusion == "4":
            insight_code = IngredientInsightCode.SCOGS_4
            insight_level = IngredientInsightLevel.WARN_CAUTION
        elif scogs_conclusion == "5":
            insight_code = IngredientInsightCode.SCOGS_5
            insight_level = IngredientInsightLevel.WARN_SEVERE
    return [
        IngredientInsight(
            code=insight_code,
            level=insight_level
        )
    ]
