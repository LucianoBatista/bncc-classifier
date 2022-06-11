# Classificador BNCC

==============================

Nesse projeto iremos criar um classificador de questão da BNCC

## Project Organization - TODO!

---

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

## Best Practices

- Environment: Here we'll be using Pipenv to manage all the packages utilized on the project. So, to make the environment active, you'll need to run `pipenv shell`.
- Installing all packages: To install all the packages already versioned on the repository you'll need to run `pipenv install`.
- Package installations: It is a best practice to install a package with the version, for example: `pipenv install pandas==1.0.3`. After this command the package will be listed on the `Pipfile` and `Pipfile.lock`, making possible the reproducibility.
- Naming notebooks: To name your notebooks is a good practice to put your name within the date and a descriptive name, for example: `luciano-20-11-numeric-eda.ipynb`
- .gitignore: Every sensible information, or files that we don't can expose to the public will be put here on `.gitignore`.
- Data: Don't put the dataset on the repository, is a good practice to put a indication of the file pointing to the place where the data is stored.
- Running notebooks: To run your notebooks with the `Pipenv` you'll need to run `pipenv run jupyter lab`. Or you can use vscode to run those notebooks.
