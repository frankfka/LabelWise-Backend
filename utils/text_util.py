import re
import unicodedata


def preprocess(text: str, remove_accents: bool = True) -> str:
    clean_text = text.lower()
    clean_text = re.sub(r"\s+", " ", clean_text)
    if remove_accents:
        clean_text = __remove_accents(clean_text)
    return clean_text


def __remove_accents(text: str) -> str:
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    return str(text)
