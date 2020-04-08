import json
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

    def __init__(self, data_filepath: str):
        all_additives = []
        try:
            with open(data_filepath, "r") as f:
                all_additives = [AdditiveInfo.from_dict(data) for data in json.load(f)]
        except Exception as e:
            # TODO: correct error logging
            print("Error creating additives database")
            print(e)
        self.all_additives: List[AdditiveInfo] = all_additives

    def get_additive(self, parsed_name: str) -> Optional[AdditiveInfo]:
        name_to_search = __clean_for_comparison__(parsed_name)
        for additive in self.all_additives:
            for name in additive.names:
                if __clean_for_comparison__(name) == name_to_search:
                    return additive
        return None


if __name__ == '__main__':
    db = AdditivesDatabase("/assets/additives_db/additives.json")
    res = db.get_additive("sodium stearoyl 2 lactylate")
    if res:
        print(res.to_dict())
    else:
        print("None found")