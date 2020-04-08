from typing import Optional


def get_float(text: str) -> (bool, Optional[float]):
    """
    Returns (success, number)
    """
    try:
        val = float(text)
        return True, val
    except ValueError:
        return False, None
