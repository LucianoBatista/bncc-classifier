import html
from pathlib import Path
from typing import Union

import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn import preprocessing

from src.cleaning import cleaning


class PreProcessingFirstModel:
    def __init__(self, path: Union[str, Path]) -> None:
        self.data = pd.read_csv(path)

    def prepro(self) -> None:
        df = self.data.copy()

        # selecting useful columns
        df = df[["id", "question", "name.1"]]
        df.columns = ["id", "questions", "target"]

        # BNCC Areas == bncc_a
        bncc_a = [
            "Língua Portuguesa",
            "Arte",
            "Educação Física",
            "Inglês",
            "Matemática",
            "Ciências",
            "Geografia",
            "História",
            "Ensino Religioso",
            "Biologia",
            "Física",
            "Química",
        ]

        # selecting target that belongs to bncc_a
        df = df.loc[df["target"].isin(bncc_a)]

        # encoding the target with labels for the classifier
        lb_enc = preprocessing.LabelEncoder()

        # train on the column we want encode
        lb_enc.fit(df["target"])
        df["target_enc"] = lb_enc.transform(df["target"])

        # chaining all cleaning steps
        df["questions_clean"] = (
            df["questions"]
            .astype(str)
            .apply(html.unescape)
            .apply(lambda x: cleaning.remove_html(x))
            .apply(lambda x: x.lower())
            .apply(lambda x: cleaning.remove_punctuation_2(x))
            .apply(cleaning.remove_italic_quotes)
            .apply(cleaning.remove_open_quotes)
            .apply(cleaning.remove_end_quotes)
            .apply(cleaning.remove_italic_dquotes)
            .apply(cleaning.remove_open_dquotes)
            .apply(cleaning.remove_quote)
            .apply(lambda x: cleaning.remove_pt_stopwords(x))
            .apply(lambda x: cleaning.remove_en_stopwords(x))
            .apply(word_tokenize)
            .apply(lambda x: cleaning.remove_punctuation_2(x))
        )

        # class to remove frq and rare, we can choose how many rare or frq words to remove
        remove_frq_rare = cleaning.RemoveFrqRare(df=df)
        remove_frq_rare.calc_frq_words()
        remove_frq_rare.calc_rare_words()
        remove_frq_rare_df = remove_frq_rare.remove_frq_and_rare()

        # removing registers with zero chars
        remove_frq_rare_df["words_counts"] = remove_frq_rare_df[
            "questions_clean"
        ].apply(len)
        final_df = remove_frq_rare_df[remove_frq_rare_df["words_counts"] != 0]
        self.data = final_df.copy()
        return remove_frq_rare.frq_words, remove_frq_rare.rare_words

    def export_cleaned_data(self, path: Union[str, Path]) -> None:
        # exporting the dataset
        df_to_save = self.data[["id", "questions_clean", "target_enc", "words_counts"]]
        df_to_save.to_csv(path, index=False)
