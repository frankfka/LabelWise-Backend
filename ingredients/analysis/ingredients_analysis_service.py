from typing import List

from ingredients.analysis.additive_insights import get_insights_for_additive
from ingredients.analysis.database.additives_db import AdditivesDatabase
from ingredients.analysis.models import AnalyzedIngredient, IngredientInsight, IngredientInsightCode, \
    IngredientInsightType
from ingredients.parser.models import ParsedIngredientsResult


class IngredientsAnalysisService:

    def __init__(self, additives_db_filepath):
        self.db = AdditivesDatabase(additives_db_filepath)

    def analyze(self, parsed_ingredients: ParsedIngredientsResult) -> List[AnalyzedIngredient]:
        """
        Analyzes the parsed ingredients. Currently, this will only return additives that have been analyzed
        (i.e. sugar synonym or additive)
        - Annotates with insights, if applicable
        """
        analyzed: List[AnalyzedIngredient] = []
        for ingredient_name in parsed_ingredients.parsed_ingredients:
            is_analyzed = False
            insights = []
            # Check if it is an added sugar
            if self.db.is_sugar_synonym(ingredient_name):
                is_analyzed = True
                insights.append(
                    IngredientInsight(code=IngredientInsightCode.ADDED_SUGAR, type=IngredientInsightType.WARN_CAUTION)
                )
            # Analyze additives
            found_additive = self.db.get_additive(ingredient_name)
            if found_additive:
                is_analyzed = True
                insights += get_insights_for_additive(found_additive)
            if is_analyzed:
                analyzed.append(
                    AnalyzedIngredient(
                        ingredient_name=ingredient_name,
                        insights=insights,
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