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
    calories_match = re.findall(match_regex, clean_text)
    for match in calories_match:
        # Attempt to parse the number
        success, val = get_float(match)
        if success:
            return val
    return None


def parse_carbohydrates(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:carbohydr|glucid)[^0-9\.]*(\d{1,3})\s*g[^0-9]"
    carbs_match = re.findall(match_regex, clean_text)
    fallback = None  # A fallback value
    for match in carbs_match:
        # Attempt to parse the number
        success, val = get_float(match)
        if success:
            if not parsed_calories or val * 4 < parsed_calories:
                # Return immediately, didn't parse calories
                return val
            elif fallback is None:
                # Init fallback if it hasn't been initialized
                fallback = val
    return fallback


def parse_protein(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:protei)[^0-9\.]*(\d{1,3})\s*g[^0-9]"
    protein_match = re.findall(match_regex, clean_text)
    fallback = None  # A fallback value
    for match in protein_match:
        # Attempt to parse the number
        success, val = get_float(match)
        if success:
            if not parsed_calories or val * 4 < parsed_calories:
                # Return immediately, didn't parse calories
                return val
            elif fallback is None:
                # Init fallback if it hasn't been initialized
                fallback = val
    return fallback


def parse_fats(clean_text: str, parsed_calories: Optional[float] = None) -> Optional[float]:
    match_regex = r"(?:fat|lipid)[^0-9\.]*(\d{1,3})\s*g[^0-9]"
    fat_match = re.findall(match_regex, clean_text)
    fallback = None  # A fallback value
    for match in fat_match:
        # Attempt to parse the number
        success, val = get_float(match)
        if success:
            if not parsed_calories or val * 9 < parsed_calories:
                # Return immediately, didn't parse calories
                return val
            elif fallback is None:
                # Init fallback if it hasn't been initialized
                fallback = val
    return fallback


def parse_sodium(clean_text: str) -> Optional[float]:
    match_regex = r"sodium[^0-9\.]*(\d{1,4})\s*mg[^0-9]"
    sodium_match = re.findall(match_regex, clean_text)
    for match in sodium_match:
        # Attempt to parse the number
        success, val = get_float(match)
        if success:
            return val
    return None
