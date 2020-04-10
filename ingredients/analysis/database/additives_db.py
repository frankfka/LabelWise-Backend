import json
import os
import re
from typing import List, Optional

from ingredients.analysis.database.models import AdditiveInfo


def __clean_for_comparison__(text: str):
    """
    Clean text for matching
    """
    text = text.lower()
    text = re.sub(r"[^\w\d]+", " ", text)
    return text


class AdditivesDatabase:

    def __init__(self, data_dir: str):
        """
        Requires the files to be placed in data_dir:
        - additives.json
        - sugar_synonyms.json
        """
        all_additives = []
        sugar_synonyms = []
        try:
            with open(os.path.join(data_dir, "additives.json"), "r") as f:
                all_additives = [AdditiveInfo.from_dict(data) for data in json.load(f)]
            with open(os.path.join(data_dir, "sugar_synonyms.json"), "r") as f:
                sugar_synonyms = json.load(f)
        except Exception as e:
            # TODO: correct error logging
            print("Error creating additives database")
            print(e)
        self.all_additives: List[AdditiveInfo] = all_additives
        self.sugar_synonyms: List[str] = [__clean_for_comparison__(term) for term in sugar_synonyms]

    def get_additive(self, parsed_name: str) -> Optional[AdditiveInfo]:
        name_to_search = __clean_for_comparison__(parsed_name)
        for additive in self.all_additives:
            for name in additive.names:
                if __clean_for_comparison__(name) == name_to_search:
                    return additive
        return None

    def is_sugar_synonym(self, parsed_name: str) -> bool:
        return __clean_for_comparison__(parsed_name) in self.sugar_synonyms


if __name__ == '__main__':
    db = AdditivesDatabase("/Users/frankjia/Desktop/Programming/LabelWise-Backend/assets/ingredients_db")
    res = db.get_additive("sodium stearoyl 2 lactylate")
    if res:
        print(res.to_dict())
    else:
        print("None found")