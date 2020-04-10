from typing import List

from ingredients.analysis.additive_warnings import get_warnings_for_additive
from ingredients.analysis.database.additives_db import AdditivesDatabase
from ingredients.analysis.models import AnalyzedIngredient, IngredientWarning, IngredientWarningCode
from ingredients.parser.models import ParsedIngredientsResult


class IngredientsAnalysisService:

    def __init__(self, additives_db_filepath):
        self.db = AdditivesDatabase(additives_db_filepath)

    def analyze(self, parsed_ingredients: ParsedIngredientsResult) -> List[AnalyzedIngredient]:
        """
        Analyzes the parsed ingredients. Currently, this will only return additives found in the database
        - Annotates with warnings, if applicable
        """
        analyzed: List[AnalyzedIngredient] = []
        for ingredient_name in parsed_ingredients.parsed_ingredients:
            warnings = []
            # Check if it is an added sugar
            if self.db.is_sugar_synonym(ingredient_name):
                warnings.append(
                    IngredientWarning(code=IngredientWarningCode.ADDED_SUGAR, level=IngredientWarning.Level.CAUTION)
                )
            # Analyze additives
            found_additive = self.db.get_additive(ingredient_name)
            if found_additive:
                warnings += get_warnings_for_additive(found_additive)
            analyzed.append(
                AnalyzedIngredient(
                    ingredient_name=ingredient_name,
                    warnings=warnings,
                    additive_info=found_additive
                )
            )
        return analyzed


if __name__ == '__main__':
    ingredients = {'4 g', 'maltitol', 'corn syrup', 'water', 'modified milk ingredients', 'natural and artificial flavour',
                   'sucralose', 'sodium alginate', '5 mg', 'cocoa', 'colour', 'per 106 g serving',
                   'modified corn starch', 'sodium stearoyl 2 lactylate', '15 mg', 'acesulfame potassium', 'salt'}
    parsed = ParsedIngredientsResult("")
    parsed.parsed_ingredients = ingredients

    service = IngredientsAnalysisService("/Users/frankjia/Desktop/Programming/LabelWise-Backend/assets/ingredients_db")
    analyzed = service.analyze(parsed)
    for ingredient in analyzed:
        print(ingredient.to_dict())