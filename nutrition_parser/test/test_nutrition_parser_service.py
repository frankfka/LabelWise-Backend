import inspect
import json
import os

import pytest

from config import AppTestConfig
from nutrition_parser.models import ParsedNutritionResult
from nutrition_parser.nutrition_parser_service import NutritionalDetailParser


def __assert__(actual, expected, compare_tag, test_tag):
    """
    Custom assert method for better test logging
    """
    if actual != expected:
        pytest.fail(f"{test_tag} ({compare_tag}): Actual {actual} | Expected {expected}")


def __compare__(actual: ParsedNutritionResult, expected: ParsedNutritionResult, test_tag):
    __assert__(actual.calories, expected.calories, "calories", test_tag)
    __assert__(actual.carbohydrates, expected.carbohydrates, "carbohydrates", test_tag)
    __assert__(actual.sugar, expected.sugar, "sugar", test_tag)
    __assert__(actual.fiber, expected.fiber, "fiber", test_tag)
    __assert__(actual.fat, expected.fat, "fat", test_tag)
    __assert__(actual.saturated_fat, expected.saturated_fat, "saturated_fat", test_tag)
    __assert__(actual.cholesterol, expected.cholesterol, "cholesterol", test_tag)
    __assert__(actual.sodium, expected.sodium, "sodium", test_tag)


config = AppTestConfig()
nutrition_parser_service = NutritionalDetailParser()


class TestNutritionParserService:

    def test_all(self):
        """
        Test all tests defined in test.json
        """
        parse_nutrition_assets_root = os.path.join(config.test_assets_dir, "parsed_nutrition")
        # Get json file that contains all the tests
        curr_dir = os.path.dirname(inspect.getfile(TestNutritionParserService))
        nutrition_test_json_filepath = os.path.join(curr_dir, "test.json")
        with open(nutrition_test_json_filepath, "r") as f:
            tests = json.load(f)
        # Test each object
        for test_data in tests:
            self.__test_one(test_data, parse_nutrition_assets_root)

    def __test_one(self, test_data: dict, root_path):
        with open(os.path.join(root_path, test_data["file"]), "r") as f:
            ocr_text = f.read()
        parsed = nutrition_parser_service.parse(ocr_text)
        expected = ParsedNutritionResult.from_dict(test_data["actual"])
        __compare__(parsed, expected, test_tag=test_data["file"])
