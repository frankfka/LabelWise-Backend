from typing import List

from ingredients.analysis.additive_warnings import get_warnings_for_additive
from ingredients.analysis.database.additives_db import AdditivesDatabase
from ingredients.analysis.models import AnalyzedAdditive
from ingredients.parser.models import ParsedIngredientsResult


class IngredientsAnalysisService:

    def __init__(self, additives_db_filepath):
        self.db = AdditivesDatabase(additives_db_filepath)

    def analyze(self, parsed_ingredients: ParsedIngredientsResult) -> List[AnalyzedAdditive]:
        """
        Analyzes the parsed ingredients. Currently, this will only return additives found in the database
        - Annotates with warnings, if applicable
        """
        analyzed: List[AnalyzedAdditive] = []
        for ingredient_name in parsed_ingredients.parsed_ingredients:
            # Analyze additives
            found_additive = self.db.get_additive(ingredient_name)
            if found_additive:
                additive_warnings = get_warnings_for_additive(found_additive)
                analyzed.append(
                    AnalyzedAdditive(
                        additive=found_additive,
                        additive_name=ingredient_name,
                        warnings=additive_warnings
                    )
                )
        return analyzed


if __name__ == '__main__':
    ingredients = {'4 g', 'maltitol', 'water', 'modified milk ingredients', 'natural and artificial flavour',
                   'sucralose', 'sodium alginate', '5 mg', 'cocoa', 'colour', 'per 106 g serving',
                   'modified corn starch', 'sodium stearoyl 2 lactylate', '15 mg', 'acesulfame potassium', 'salt'}
    parsed = ParsedIngredientsResult("")
    parsed.parsed_ingredients = ingredients

    service = IngredientsAnalysisService("/Users/frankjia/Desktop/Programming/LabelWise-Backend/assets/additives_db/additives.json")
    analyzed = service.analyze(parsed)
    for ingredient in analyzed:
        print(ingredient.to_dict())