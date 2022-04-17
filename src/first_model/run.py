from src.first_model.preprocessing import PreProcessingFirstModel

PATH_RAW = """/home/luba/Documents/DS/projects-courses-ongoing/
bncc-classifier-[doing]/data/raw/bncc_first_classifier.csv"""
PATH_TO_SAVE = """/home/luba/Documents/DS/projects-courses-ongoing/
bncc-classifier-[doing]/data/curated/bncc_first_classifier_cleaned.csv"""


def main():
    prepro_obj = PreProcessingFirstModel(PATH_RAW)
    prepro_obj.prepro()
    prepro_obj.export_cleaned_data(PATH_TO_SAVE)
    print(prepro_obj.data.columns)


if __name__ == "__main__":
    main()
