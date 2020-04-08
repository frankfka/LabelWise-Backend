from typing import Optional, Dict


class ParsedNutritionResult:

    def __init__(self, original_text: str):
        self.original_text = original_text
        self.calories: Optional[float] = None
        self.carbohydrates: Optional[float] = None
        self.protein: Optional[float] = None
        self.fat: Optional[float] = None
        self.fiber: Optional[float] = None
        self.sodium: Optional[float] = None  # milligrams

    def to_dict(self) -> Dict:
        return {
            "calories": self.calories,
            "carbohydrates": self.carbohydrates,
            "protein": self.protein,
            "fat": self.fat,
            "fiber": self.fiber,
            "sodium": self.sodium
        }