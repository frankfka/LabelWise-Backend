from nutrition_parser.models import ParsedNutritionResult
import nutrition_parser.parser_functions as parser
from utils.text_util import preprocess


class NutritionalDetailParser:
    """
    Parses nutritional data from OCR text
    - TODO: https://pypi.org/project/regex/ for fuzzy matches
    """

    def parse(self, text: str) -> ParsedNutritionResult:
        clean_text = preprocess(text)
        result = ParsedNutritionResult(clean_text)
        calories = parser.parse_calories(clean_text)
        carbohydrates = parser.parse_carbohydrates(clean_text, calories)
        sugar = parser.parse_sugar(clean_text, calories)
        fiber = parser.parse_fiber(clean_text, calories)
        protein = parser.parse_protein(clean_text, calories)
        fat = parser.parse_fat(clean_text, calories)
        sat_fat = parser.parse_sat_fat(clean_text, calories)
        cholesterol = parser.parse_cholesterol(clean_text)
        sodium = parser.parse_sodium(clean_text)

        result.calories = calories
        result.carbohydrates = carbohydrates
        result.sugar = sugar
        result.fiber = fiber
        result.protein = protein
        result.fat = fat
        result.saturated_fat = sat_fat
        result.cholesterol = cholesterol
        result.sodium = sodium
        return result


if __name__ == '__main__':
    import io

    def get_text(path):
        with io.open(path, 'r') as f:
            return f.read()

    text = get_text("/Users/frankjia/Desktop/Programming/LabelWise-Backend/test_assets/parsed_nutrition/nutrition_1.txt")
    service = NutritionalDetailParser()
    parse_result = service.parse(text)
    print(parse_result.to_dict())