import inspect
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

    def did_parse_all(self):
        """
        Determines whether all properties were parsed successfully
        """
        attr_vals = [val for val in self.to_dict().values()]
        return None not in attr_vals

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
        item.calories = data.get("calories", None)
        item.carbohydrates = data.get("carbohydrates", None)
        item.sugar = data.get("sugar", None)
        item.fiber = data.get("fiber", None)
        item.protein = data.get("protein", None)
        item.fat = data.get("fat", None)
        item.saturated_fat = data.get("saturated_fat", None)
        item.cholesterol = data.get("cholesterol", None)
        item.sodium = data.get("sodium", None)
        return item
