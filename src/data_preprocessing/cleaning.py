import re


def to_lower(text: str) -> str:
    return text.lower()


def remove_tags(text: str) -> str:
    pattern = re.compile("<.*?>")
    cleantext = re.sub(pattern, "", text).replace(u"\xa0", u" ")
    return cleantext


def remove_punctuation(text: str) -> str:
    return re.sub(r"[^\w\s]", "", text)


def remove_numbers(text: str) -> str:
    pattern = re.compile("[0-9]+")
    clean_text = re.sub(pattern, "", text)
    return clean_text
