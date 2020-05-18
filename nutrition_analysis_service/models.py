from enum import IntEnum, Enum


class NutritionInsightCode(Enum):
    # Positive
    LOW_SODIUM = "LOW_SODIUM"
    LOW_SUGAR = "LOW_SUGAR"
    HIGH_FIBER = "HIGH_FIBER"
    HIGH_PROTEIN = "HIGH_PROTEIN"
    # Warnings
    HIGH_SODIUM = "HIGH_SODIUM"
    HIGH_SUGAR = "HIGH_SUGAR"
    LOW_FIBER = "LOW_FIBER"
    HIGH_SAT_FAT = "HIGH_SAT_FAT"
    HIGH_CHOLESTEROL = "HIGH_CHOLESTEROL"


class NutritionInsightType(IntEnum):
    POSITIVE = 1
    WARN_CAUTION = -1
    WARN_SEVERE = -2


class NutritionInsight:

    def __init__(self, code: NutritionInsightCode, insight_type):
        self.code: NutritionInsightCode = code
        self.insight_type: NutritionInsightType = insight_type

    def to_dict(self):
        return {
            "code": self.code.value,
            "type": self.insight_type.value
        }

    @classmethod
    def from_dict(cls, data):
        """
        Parse NutritionInsight from a dict - can return none if code or type is not valid
        """
        raw_code = data.get("code", None)
        raw_type = data.get("type", None)
        if raw_code and raw_type:
            try:
                code = NutritionInsightCode(raw_code)
                insight_type = NutritionInsightType(raw_type)
                return NutritionInsight(code=code, insight_type=insight_type)
            except ValueError:
                pass
        return None

    def __hash__(self):
        return hash((self.code.value, self.insight_type.value))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.code == other.code and self.insight_type == other.insight_type