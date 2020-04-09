from typing import Set


class ParsedIngredientsResult:

    def __init__(self, original_text: str):
        self.original_text = original_text
        self.parsed_ingredients: Set[str] = set()

    def to_dict(self):
        return {
            "parsed_ingredients": list(self.parsed_ingredients)
        }