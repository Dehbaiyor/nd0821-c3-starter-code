# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- This model was developed by Adebayo Oshingbesan
- This was done on 10/07/2021
- The model version is version 1
- The model type is Random Forest Classifier with Randomized Search with Cross Validation for Hyperparameter Tuning
- The parameters grid for hyperparameter tuning is:  param_grid = {'bootstrap': [True, False],
               'max_depth': [3, 5, 7, 10, None],
               'max_features': ['auto', 'sqrt'],
               'min_samples_leaf': [2, 4, 8, 16, 32],
               'min_samples_split': [2, 5, 10],
               'n_estimators': [50, 100, 150, 200]}
- The features used includes: {'age', 'workclass', 'fnlgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
       'salary'}
- For comments, email dehbaiyoratgmaildotcom

## Intended Use
- This model was used to practice deployment of scalable ML pipeline with CI/CD
- It is not for actual use case in the real world

## Factors
- The model not trained for actual use case in the world
- There was no bias/ fairness consideration

## Training Data
- The model source is https://archive.ics.uci.edu/ml/datasets/census+income
- 80% of dataset was randomly chosen to train

## Evaluation Data
- The model source: https://archive.ics.uci.edu/ml/datasets/census+income
- 20% of dataset was randomly chosen to test (train and evaluation sets do not overlap)

## Metrics
The metrics used are:
  - fbeta
  - precision
  - recall
  
The training set metrics for the trained model is:
  - Precision: 0.8041
  - Recall: 0.6219
  - Fbeta: 0.7013

The test set metrics for the trained model is:
  - Precision: 0.7994
  - Recall: 0.6314
  - Fbeta: 0.7055


## Ethical Considerations
- There were no ethical considerations

## Caveats and Recommendations
- The model could be optimized for fairness
