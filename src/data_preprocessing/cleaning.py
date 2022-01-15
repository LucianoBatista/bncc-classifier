import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def to_lower(text: str) -> str:
    return text.lower()


def remove_tags(text: str) -> str:
    pattern = re.compile("<.*?>")
    cleantext = re.sub(pattern, " ", text).replace(u"\xa0", u" ")
    return cleantext


def remove_punctuation(text: str) -> str:
    return re.sub(r"[^\w\s]", " ", text)


def remove_numbers(text: str) -> str:
    pattern = re.compile("[0-9]+")
    clean_text = re.sub(pattern, " ", text)
    return clean_text


def remove_standard_stopwords(text: str) -> str:
    stop_words = set(stopwords.words("portuguese"))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    final_sentence = " ".join(filtered_sentence)
    return final_sentence
