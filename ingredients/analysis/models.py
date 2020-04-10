from enum import IntEnum, Enum
from typing import List, Optional

from ingredients.analysis.database.models import AdditiveInfo


class IngredientWarningCode(Enum):
    NOT_GRAS = "NOT_GRAS"
    SCOGS_3 = "SCOGS_3"
    SCOGS_4 = "SCOGS_4"
    SCOGS_5 = "SCOGS_5"
    ADDED_SUGAR = "ADDED_SUGAR"


class IngredientWarning:
    class Level(IntEnum):
        NONE = 0
        CAUTION = 1
        SEVERE = 2

    def __init__(self, code: IngredientWarningCode, level):
        self.code: IngredientWarningCode = code
        self.level: IngredientWarning.Level = level

    def to_dict(self) -> dict:
        return {
            "code": self.code.value,
            "level": self.level.value
        }


class AnalyzedIngredient:

    def __init__(self, ingredient_name: str, warnings: List[IngredientWarning],
                 additive_info: Optional[AdditiveInfo] = None):
        self.ingredient_name: str = ingredient_name
        self.warnings: List[IngredientWarning] = warnings
        self.additive_info: Optional[AdditiveInfo] = additive_info

    def to_dict(self) -> dict:
        additive_info = None
        if self.additive_info:
            additive_info = self.additive_info.to_dict()
        return {
            "ingredient_name": self.ingredient_name,
            "warnings": [warning.to_dict() for warning in self.warnings],
            "additive_info": additive_info,
        }
