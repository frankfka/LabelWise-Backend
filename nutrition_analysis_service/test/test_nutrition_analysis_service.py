import inspect
import json
import os
from typing import Set

import pytest

from config import AppTestConfig
from nutrition_analysis_service.models import NutritionInsight
from nutrition_analysis_service.nutrition_analysis_service import NutritionAnalysisService
from nutrition_parser.models import ParsedNutritionResult


def __compare__(actual: Set[NutritionInsight], expected: Set[NutritionInsight], desc):
    def get_set_description(s: Set[NutritionInsight]):
        return [i.to_dict() for i in s]
    in_actual_not_in_expected = actual - expected
    in_expected_not_in_actual = expected - actual
    if in_expected_not_in_actual or in_actual_not_in_expected:
        fail_message = desc
        fail_message += f"\nItems found in generated insights but not expected: {get_set_description(in_actual_not_in_expected)}"
        fail_message += f"\nItems found in expected insights but not generated: {get_set_description(in_expected_not_in_actual)}"
        pytest.fail(fail_message, pytrace=False)


config = AppTestConfig()
nutrition_analysis_service = NutritionAnalysisService()


class TestNutritionAnalysisService:

    def test_all(self):
        """
        Test all tests defined in test.json
        """
        # Get json file that contains all the tests
        curr_dir = os.path.dirname(inspect.getfile(TestNutritionAnalysisService))
        nutrition_test_json_filepath = os.path.join(curr_dir, "test.json")
        with open(nutrition_test_json_filepath, "r") as f:
            tests = json.load(f)
        # Test each object
        for test_data in tests:
            self.__test_one(test_data)

    def __test_one(self, test_data: dict):
        description = test_data["description"]
        nutrition = ParsedNutritionResult.from_dict(test_data["nutrition"])
        generated_insights = set(nutrition_analysis_service.get_insights(nutrition))
        expected_insights = set([NutritionInsight.from_dict(data) for data in test_data["insights"]])
        __compare__(generated_insights, expected_insights, description)