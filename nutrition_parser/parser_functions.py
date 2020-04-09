import re
from typing import Optional

from nutrition_parser.util import get_float


def parse_calories(clean_text: str) -> Optional[float]:
    """
    Returns calories parsed from the text

    Regex:
    - Look for "calorie"
    - Match anything except for digits
    - Match 1-3 digits (the capturing group)
    - Match a non-digit character
    """
    match_regex = r"calorie[^0-9]*(\d{1,3})[^0-9]"
    return __parse_with_regex__(clean_text, match_regex)


def parse_carbohydrates(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:carbohydr|glucid)[^0-9\.]*(\d{1,2})\s*g[^0-9]"
    return __parse_with_regex__(clean_text, match_regex, cal_per_gram=4, parsed_calories=parsed_calories)


def parse_sugar(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:sugar|sucre)[^0-9\.]*(\d{1,2})\s*g[^0-9]"
    return __parse_with_regex__(clean_text, match_regex, cal_per_gram=4, parsed_calories=parsed_calories)


def parse_fiber(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:fiber|fibre)[^0-9\.]*(\d{1,2})\s*g[^0-9]"
    return __parse_with_regex__(clean_text, match_regex, cal_per_gram=4, parsed_calories=parsed_calories)


def parse_protein(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:protei)[^0-9\.]*(\d{1,2})\s*g[^0-9]"
    return __parse_with_regex__(clean_text, match_regex, cal_per_gram=4, parsed_calories=parsed_calories)


def parse_fat(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:fat|lipid)[^0-9\.]*(\d{1,2})\s*g[^0-9]"
    return __parse_with_regex__(clean_text, match_regex, cal_per_gram=9, parsed_calories=parsed_calories)


def parse_sat_fat(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"saturate[^0-9\.]*(\d{1,2})\s*g[^0-9]"
    return __parse_with_regex__(clean_text, match_regex, cal_per_gram=4, parsed_calories=parsed_calories)


def parse_cholesterol(clean_text: str) -> Optional[float]:
    match_regex = r"cholestero[^0-9\.]*(\d{1,3})\s*mg[^0-9]"
    return __parse_with_regex__(clean_text, match_regex)


def parse_sodium(clean_text: str) -> Optional[float]:
    match_regex = r"sodium[^0-9\.]*(\d{1,4})\s*mg[^0-9]"
    return __parse_with_regex__(clean_text, match_regex)


def __parse_with_regex__(clean_text: str, match_regex: str,
                         cal_per_gram: Optional[float] = None,
                         parsed_calories: Optional[float] = None) -> Optional[float]:
    """
    Return possible match with given regex, will check that calories from nutrient < total calories if given
    """
    all_matches = re.findall(match_regex, clean_text)
    fallback = None  # A fallback value
    for match in all_matches:
        # Attempt to parse the number
        success, val = get_float(match)
        if success:
            if __check_calories__(val, cal_per_gram, parsed_calories):
                # Best case scenario
                return val
            elif fallback is None:
                # Init fallback if it hasn't been initialized
                fallback = val
    return fallback


def __check_calories__(parsed_grams: float, cal_per_gram: Optional[float], parsed_calories: Optional[float]) -> bool:
    """
    Return True if parsed_gram * cal_per_gram < parsed_calories, or if the optional values are not given
    """
    if parsed_calories is None or cal_per_gram is None:
        return True
    return parsed_grams * float(cal_per_gram) < parsed_calories
