import re
from typing import Optional, Set

from ingredients.parser.models import ParsedIngredientsResult
from utils.text_util import preprocess


class IngredientsParser:
    """
    Parses ingredients from OCR text
    """
    INGREDIENT_STR_BREAKS = {
        "ingrédien",  # For Canadian labels, signal start of French section
        "manufacture",  # Place of manufacture string
        "contains"  # Start of allergy information
    }

    def parse(self, text: str) -> ParsedIngredientsResult:
        clean_text = preprocess(text, remove_accents=False)
        result = ParsedIngredientsResult(clean_text)
        ingredients_str = self.__get_ingredients_str(clean_text)
        result.parsed_ingredients = self.__get_ingredients(ingredients_str)
        return result

    def __get_ingredients_str(self, clean_text: str) -> str:
        """
        Gets portion of the string that contains the ingredients. Not meant to be perfect so requires postprocessing.
        Using regex is very slow, so iterate over string items
        """
        ingredient_segments = []
        add_segment = False  # Whether to add segments

        def should_stop_adding(segment: str) -> bool:
            for break_segment in IngredientsParser.INGREDIENT_STR_BREAKS:
                if break_segment in segment:
                    return True
            return False

        # Iterate over words / punctuation separated by a space
        for str_segment in clean_text.split():
            # Add if we have started gathering the ingredients
            if add_segment:
                # Check for keywords that signal the end of the ingredients section
                if should_stop_adding(str_segment):
                    break
                # Otherwise, add the segment
                ingredient_segments.append(str_segment)
            elif "ingredie" in str_segment:
                # Part of the word "ingredients", signals start of section
                add_segment = True
        return " ".join(ingredient_segments)

    def __get_ingredients(self, ingredients_text: str) -> Set[str]:

        def get_clean_ingredient_text(ingredient: str) -> Optional[str]:
            """
            Return a valid cleaned ingredient name, or None if invalid
            """
            ingredient = ingredient.strip()
            # Replace non-alphanumeric with space
            ingredient = re.sub(r"[^\w\d]+", " ", ingredient)
            # Normalized spaces
            ingredient_words = ingredient.strip().split()
            if 0 < len(ingredient_words) < 5:
                return " ".join(ingredient_words)
            return None

        # Split by brackets, commas
        ingredients = re.split(r"[,()\[\]{\}]", ingredients_text)
        # Map to clean ingredients
        ingredients = map(get_clean_ingredient_text, ingredients)
        ingredients = filter(lambda ingredient: ingredient, ingredients)
        return set(ingredients)


if __name__ == '__main__':
    import io

    def get_text(path):
        with io.open(path, 'r') as f:
            return f.read()

    text = get_text("//test_assets/parsed_ingredients/ingredients_6.txt")
    parser = IngredientsParser()
    parse_result = parser.parse(text)
    print(parse_result.parsed_ingredients)
