from typing import List

from ingredients.analysis.database.models import AdditiveInfo
from ingredients.analysis.models import IngredientWarning, IngredientWarningCode


def get_warnings_for_additive(additive: AdditiveInfo) -> List[IngredientWarning]:
    warnings: List[IngredientWarning] = []
    warnings.extend(__check_scogs__(additive))
    return warnings


def __check_scogs__(additive: AdditiveInfo) -> List[IngredientWarning]:
    warnings: List[IngredientWarning] = []
    scogs_conclusion = additive.scogs_conclusion
    if scogs_conclusion:
        if scogs_conclusion == "3":
            warnings.append(IngredientWarning(
                code=IngredientWarningCode.SCOGS_3,
                level=IngredientWarning.Level.CAUTION
            ))
        elif scogs_conclusion == "4":
            warnings.append(IngredientWarning(
                code=IngredientWarningCode.SCOGS_4,
                level=IngredientWarning.Level.CAUTION
            ))
        elif scogs_conclusion == "5":
            warnings.append(IngredientWarning(
                code=IngredientWarningCode.SCOGS_5,
                level=IngredientWarning.Level.CAUTION
            ))
    else:
        warnings.append(IngredientWarning(
            code=IngredientWarningCode.NOT_GRAS,
            level=IngredientWarning.Level.SEVERE
        ))
    return warnings
