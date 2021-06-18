import os

DATA_FOLDER = 'data'
TRAIN_CSV = os.path.join(DATA_FOLDER, 'train.csv')
VAL_CSV = os.path.join(DATA_FOLDER, 'val.csv')

MODELS_FOLDER = 'models'
SAVED_ESTIMATOR = os.path.join(MODELS_FOLDER, 'finalized_model.pickle')