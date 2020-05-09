from enum import IntEnum, Enum


class NutritionInsightCode(Enum):
    # Positive
    # Warnings
    HIGH_SODIUM = "HIGH_SODIUM"
    HIGH_SUGAR = "HIGH_SUGAR"
    LOW_FIBER = "LOW_FIBER"
    HIGH_SAT_FAT = "HIGH_SAT_FAT"
    HIGH_CHOLESTEROL = "HIGH_CHOLESTEROL"


class NutritionInsight:
    class Type(IntEnum):
        POSITIVE = 1
        WARN_CAUTION = -1
        WARN_SEVERE = -2

    def __init__(self, code: NutritionInsightCode, insight_type):
        self.code: NutritionInsightCode = code
        self.insight_type: NutritionInsight.Type = insight_type

    def to_dict(self):
        return {
            "code": self.code.value,
            "type": self.insight_type.value
        }