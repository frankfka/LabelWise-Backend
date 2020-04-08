from enum import IntEnum, Enum
from typing import List

from ingredients.analysis.database.models import AdditiveInfo


class IngredientWarningCode(Enum):
    NOT_GRAS = "NOT_GRAS"
    SCOGS_3 = "SCOGS_3"
    SCOGS_4 = "SCOGS_4"
    SCOGS_5 = "SCOGS_5"


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


class AnalyzedAdditive:

    def __init__(self, additive: AdditiveInfo, additive_name: str, warnings: List[IngredientWarning]):
        self.additive_name: str = additive_name
        self.additive: [AdditiveInfo] = additive
        self.warnings: List[IngredientWarning] = warnings

    def to_dict(self) -> dict:
        return {
            "ingredient_name": self.additive_name,
            "ingredient": self.additive.to_dict(),
            "warnings": [warning.to_dict() for warning in self.warnings],
        }
