from typing import Optional, Dict


class ParsedNutritionResult:

    def __init__(self, original_text: str):
        self.original_text = original_text
        self.calories: Optional[float] = None

        self.carbohydrates: Optional[float] = None
        self.sugar: Optional[float] = None
        self.fiber: Optional[float] = None

        self.protein: Optional[float] = None

        self.fat: Optional[float] = None
        self.saturated_fat: Optional[float] = None
        self.cholesterol: Optional[float] = None

        self.sodium: Optional[float] = None  # milligrams

    def to_dict(self) -> Dict:
        return {
            "calories": self.calories,
            "carbohydrates": self.carbohydrates,
            "sugar": self.sugar,
            "fiber": self.fiber,
            "protein": self.protein,
            "fat": self.fat,
            "saturated_fat": self.saturated_fat,
            "cholesterol": self.cholesterol,
            "sodium": self.sodium
        }

    @classmethod
    def from_dict(cls, data):
        item = ParsedNutritionResult("")
        item.calories = data["calories"]
        item.carbohydrates = data["carbohydrates"]
        item.sugar = data["sugar"]
        item.fiber = data["fiber"]
        item.protein = data["protein"]
        item.fat = data["fat"]
        item.saturated_fat = data["saturated_fat"]
        item.cholesterol = data["cholesterol"]
        item.sodium = data["sodium"]
        return item