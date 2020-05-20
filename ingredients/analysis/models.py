from enum import IntEnum, Enum
from typing import List, Optional

from ingredients.analysis.database.models import AdditiveInfo


class IngredientInsightCode(Enum):
    NOT_GRAS = "NOT_GRAS"
    SCOGS_3 = "SCOGS_3"
    SCOGS_4 = "SCOGS_4"
    SCOGS_5 = "SCOGS_5"
    ADDED_SUGAR = "ADDED_SUGAR"


class IngredientInsightLevel(IntEnum):
    POSITIVE = 1
    WARN_CAUTION = -1
    WARN_SEVERE = -2


class IngredientInsight:

    def __init__(self, code: IngredientInsightCode, level: IngredientInsightLevel):
        self.code: IngredientInsightCode = code
        self.level: IngredientInsightLevel = level

    def to_dict(self) -> dict:
        return {
            "code": self.code.value,
            "level": self.level.value
        }


class AnalyzedIngredient:

    def __init__(self, ingredient_name: str, insights: List[IngredientInsight],
                 additive_info: Optional[AdditiveInfo] = None):
        self.ingredient_name: str = ingredient_name
        self.insights: List[IngredientInsight] = insights
        self.additive_info: Optional[AdditiveInfo] = additive_info

    def to_dict(self) -> dict:
        additive_info = None
        if self.additive_info:
            additive_info = self.additive_info.to_dict()
        return {
            "ingredient_name": self.ingredient_name,
            "insights": [insight.to_dict() for insight in self.insights],
            "additive_info": additive_info,
        }
