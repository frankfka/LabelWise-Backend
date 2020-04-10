from enum import IntEnum, Enum


class NutritionWarningCode(Enum):
    HIGH_SODIUM = "HIGH_SODIUM"
    HIGH_SUGAR = "HIGH_SUGAR"
    LOW_FIBER = "LOW_FIBER"
    HIGH_SAT_FAT = "HIGH_SAT_FAT"
    HIGH_CHOLESTEROL = "HIGH_CHOLESTEROL"


class NutritionWarning:
    class Level(IntEnum):
        NONE = 0
        CAUTION = 1
        SEVERE = 2

    def __init__(self, code: NutritionWarningCode, level):
        self.code: NutritionWarningCode = code
        self.level: NutritionWarning.Level = level

    def to_dict(self):
        return {
            "code": self.code.value,
            "level": self.level.value
        }