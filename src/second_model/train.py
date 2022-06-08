import pickle

import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn import feature_extraction, linear_model, metrics, model_selection
from sklearn.pipeline import Pipeline


class Modeling:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def tokenization(self):
        df = self.data.copy()
        df["question_tokens"] = df["questions_clean"].apply(word_tokenize)
        self.data = df.copy()

    def split_data(self):
        X = self.data.drop(["id", "words_counts", "target_enc"], axis=1)
        y = self.data["target_enc"]
        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        ) = model_selection.train_test_split(X, y, random_state=1)

    def saving_pipeline(self):

        pipe = Pipeline(
            [
                ("count_vect", feature_extraction.text.CountVectorizer()),
                (
                    "logistic_regression",
                    linear_model.LogisticRegression(class_weight="balanced"),
                ),
            ]
        )
        print(self.X_train.columns)
        pipe.fit(self.X_train["questions_clean"], self.y_train)

        # saving
        with open(
            "/home/luba/Documents/DS/projects-courses-ongoing/bncc-classifier-[doing]/models/lr_second_model.bin",
            "wb",
        ) as lr_out:
            pickle.dump(pipe, lr_out)

    def make_bag_of_words(self):
        vect_bow = feature_extraction.text.CountVectorizer()
        X_train_trans = vect_bow.fit_transform(self.X_train["questions_clean"])
        X_test_trans = vect_bow.transform(self.X_test["questions_clean"])

        return X_train_trans, X_test_trans

    def train_evaluate_log_reg(self, X_train_trans, X_test_trans):
        log_reg = linear_model.LogisticRegression(class_weight="balanced")
        log_reg.fit(X_train_trans, self.y_train)
        y_pred_class = log_reg.predict(X_test_trans)
        print(metrics.classification_report(self.y_test, y_pred_class))
