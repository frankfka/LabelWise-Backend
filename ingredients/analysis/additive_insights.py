from typing import List

from ingredients.analysis.database.models import AdditiveInfo
from ingredients.analysis.models import IngredientInsight, IngredientInsightCode, IngredientInsightLevel


def get_insights_for_additive(additive: AdditiveInfo) -> List[IngredientInsight]:
    insights: List[IngredientInsight] = []
    insights.extend(__check_scogs__(additive))
    return insights


def __check_scogs__(additive: AdditiveInfo) -> List[IngredientInsight]:
    insights: List[IngredientInsight] = []
    scogs_conclusion = additive.scogs_conclusion
    if scogs_conclusion:
        if scogs_conclusion == "3":
            insights.append(IngredientInsight(
                code=IngredientInsightCode.SCOGS_3,
                level=IngredientInsightLevel.WARN_CAUTION
            ))
        elif scogs_conclusion == "4":
            insights.append(IngredientInsight(
                code=IngredientInsightCode.SCOGS_4,
                level=IngredientInsightLevel.WARN_CAUTION
            ))
        elif scogs_conclusion == "5":
            insights.append(IngredientInsight(
                code=IngredientInsightCode.SCOGS_5,
                level=IngredientInsightLevel.WARN_CAUTION
            ))
    else:
        insights.append(IngredientInsight(
            code=IngredientInsightCode.NOT_GRAS,
            level=IngredientInsightLevel.WARN_SEVERE
        ))
    return insights
