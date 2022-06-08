import re
import string
from collections import Counter

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt")

PUNCT_TO_REMOVE = string.punctuation
pt_stopwords = set(stopwords.words("portuguese"))
en_stopwords = set(stopwords.words("english"))


def to_lower(text: str) -> str:
    return text.lower()


def remove_tags(text: str) -> str:
    pattern = re.compile("<.*?>")
    cleantext = re.sub(pattern, " ", text).replace("\xa0", " ")
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
    filtered_sentence = [w for w in word_tokens if w not in stop_words]
    final_sentence = " ".join(filtered_sentence)
    return final_sentence


def remove_html(text):
    html_pattern = re.compile("<.*?>")
    return html_pattern.sub(r"", text)


def remove_punctuation_2(text):
    return text.translate(str.maketrans("", "", PUNCT_TO_REMOVE))


# Função para remover aspas em itálico
def remove_italic_dquotes(text: str) -> str:
    pattern = re.compile(r'"')
    clean_text = re.sub(pattern, " ", text)
    return clean_text


# Função para remover aspas de abertura
def remove_open_dquotes(text: str) -> str:
    pattern = re.compile(r"“")
    clean_text = re.sub(pattern, " ", text)
    return clean_text


# Função para remover aspas de fechamento
def remove_end_dquotes(text: str) -> str:
    pattern = re.compile(r"”")
    clean_text = re.sub(pattern, " ", text)
    return clean_text


# Função para remover single quotes normal
def remove_italic_quotes(text: str) -> str:
    pattern = re.compile(r"'")
    clean_text = re.sub(pattern, " ", text)
    return clean_text


# Função para remover single quotes abertura
def remove_open_quotes(text: str) -> str:
    pattern = re.compile(r"‘")
    clean_text = re.sub(pattern, " ", text)
    return clean_text


# Função para remover single quotes fechamento
def remove_end_quotes(text: str) -> str:
    pattern = re.compile(r"’")
    clean_text = re.sub(pattern, " ", text)
    return clean_text


# Função para remover aspas de abertura
def remove_quote(text: str) -> str:
    pattern = re.compile(r"‛")
    clean_text = re.sub(pattern, " ", text)
    return clean_text


def remove_pt_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in pt_stopwords])


def remove_en_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in en_stopwords])


class RemoveFrqRare:
    def __init__(self, df: pd.DataFrame, n_frq_words: int = 10, n_rare_words: int = 10):
        self.df = df
        self.n_frq_words = n_frq_words
        self.n_rare_words = n_rare_words
        self.frq_words = []
        self.rare_words = []

    def calc_frq_words(self):
        final_list = [
            subitem for item in self.df["questions_clean"] for subitem in item
        ]
        cnt = Counter(final_list)
        self.frq_words = set([w for (w, wc) in cnt.most_common(self.n_frq_words)])
        # print(self.frq_words)

    def calc_rare_words(self):
        # joining all words
        final_list = [
            subitem for item in self.df["questions_clean"] for subitem in item
        ]
        cnt = Counter(final_list)
        self.rare_words = set(
            [w for (w, wc) in cnt.most_common()[: -self.n_rare_words - 1 : -1]]  # noqa
        )
        # print(self.rare_words)

    def remove_frq_words(self, text: str):
        return " ".join(
            [word for word in str(text).split() if word not in self.frq_words]
        )

    def remove_rare_words(self, text: str):
        return " ".join(
            [word for word in str(text).split() if word not in self.rare_words]
        )

    def remove_frq_and_rare(self):
        df_to_return = self.df.copy()
        df_to_return["questions_clean"] = (
            self.df["questions_clean"]
            .apply(lambda x: self.remove_frq_words(x))
            .apply(lambda x: self.remove_rare_words(x))
        )
        return df_to_return
