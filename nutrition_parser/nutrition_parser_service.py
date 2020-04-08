from nutrition_analysis_service.nutrition_analysis_service import NutritionAnalysisService
from nutrition_parser.models import ParsedNutritionResult
from nutrition_parser.parser_functions import parse_carbohydrates, parse_calories, parse_protein, parse_fats, \
    parse_sodium
from utils.text_util import preprocess


class NutritionalDetailParser:
    """
    Parses nutritional data from OCR text
    - TODO: https://pypi.org/project/regex/ for fuzzy matches
    """

    def parse(self, text: str) -> ParsedNutritionResult:
        clean_text = preprocess(text)
        result = ParsedNutritionResult(clean_text)
        calories = parse_calories(clean_text)
        carbohydrates = parse_carbohydrates(clean_text, calories)
        protein = parse_protein(clean_text, calories)
        fat = parse_fats(clean_text, calories)
        sodium = parse_sodium(clean_text)
        result.calories = calories
        result.carbohydrates = carbohydrates
        result.protein = protein
        result.fat = fat
        result.sodium = sodium
        return result


if __name__ == '__main__':
    import io

    def get_text(path):
        with io.open(path, 'r') as f:
            return f.read()

    text = get_text("//test_assets/parsed_nutrition/nutrition_9.txt")
    parser = NutritionalDetailParser()
    parse_result = parser.parse(text)
    print(parse_result.to_dict())