from src.first_model.preprocessing import PreProcessingFirstModel
from src.first_model.train import Modeling

# Luciano
PATH_RAW = "/home/luba/Documents/DS/projects-courses-ongoing/bncc-classifier-[doing]/data/raw/bncc_first_classifier.csv"  # noqa
PATH_TO_SAVE = "/home/luba/Documents/DS/projects-courses-ongoing/bncc-classifier-[doing]/data/curated/bncc_first_classifier_cleaned.csv"  # noqa

# will
# PATH_RAW = "/home/wilsonfranccadeolveiraneto/Documentos/TERA/bncc-classifier/data/raw/bncc_first_classifier.csv"  # noqa
# PATH_TO_SAVE = "/home/wilsonfranccadeolveiraneto/Documentos/TERA/bncc-classifier/data/curated/bncc_first_classifier_cleaned.csv"  # noqa


def main():
    prepro_obj = PreProcessingFirstModel(PATH_RAW)
    frq_words, rare_words = prepro_obj.prepro()

    # export list of frq and rare words on our data
    with open("frq_words.txt", "w") as f:
        # print(frq_words)
        _ = [f.write("%s\n" % item) for item in frq_words]

    with open("rare_words.txt", "w") as f:
        # print(rare_words)
        _ = [f.write("%s\n" % item) for item in rare_words]

    prepro_obj.export_cleaned_data(PATH_TO_SAVE)
    modeling = Modeling(prepro_obj.data)
    # modeling.tokenization()
    modeling.split_data()
    modeling.saving_pipeline()
    X_train_trans, X_test_trans = modeling.make_bag_of_words()
    modeling.train_evaluate_log_reg(
        X_train_trans=X_train_trans, X_test_trans=X_test_trans
    )


if __name__ == "__main__":
    main()
