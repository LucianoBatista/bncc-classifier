import re


def remove_tags(text: str):
    pattern = re.compile("<.*?>")
    cleantext = re.sub(pattern, "", text).replace(u"\xa0", u" ")
    return cleantext
