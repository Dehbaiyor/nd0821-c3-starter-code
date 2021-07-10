# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- Developer: Adebayo Oshingbesan
- Date: 10/07/2021
- Version: 1
- Type: Random Forest Classifier with Randomized Search with Cross Validation for Hyperparameter Tuning
- Parameters Grid:  param_grid = {'bootstrap': [True, False],
               'max_depth': [3, 5, 7, 10, None],
               'max_features': ['auto', 'sqrt'],
               'min_samples_leaf': [2, 4, 8, 16, 32],
               'min_samples_split': [2, 5, 10],
               'n_estimators': [50, 100, 150, 200]}
- Features: {'age', 'workclass', 'fnlgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
       'salary'}
- For comments, email dehbaiyoratgmaildotcom

## Intended Use
- Practice deployment of scalable ML pipeline with CI/CD
- Not for actual use case in the real world

## Factors
- Model not trained for actual use case in the world
- No bias/ fairness consideration

## Training Data
- Source: https://archive.ics.uci.edu/ml/datasets/census+income
- 80% of dataset was randomly chosen to train

## Evaluation Data
- Source: https://archive.ics.uci.edu/ml/datasets/census+income
- 20% of dataset was randomly chosen to test (train and evaluation sets do not overlap)

## Metrics
- fbeta
- precision
- recall

## Ethical Considerations
- No ethical considerations

## Caveats and Recommendations
- Model could be optimized for fairness
