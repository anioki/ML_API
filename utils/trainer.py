from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from settings.constants import SAVED_ESTIMATOR
import pickle

class Estimator:
    @staticmethod
    def fit(train_x, train_y):
        dtr = DecisionTreeClassifier(criterion = 'entropy',random_state=0,max_depth = 6)
        model = dtr.fit(train_x, train_y)
        pickle.dump(model, open(SAVED_ESTIMATOR, 'wb'))
        return model

    @staticmethod
    def predict(trained, test_x):
        y_pred = trained.predict(test_x)
        return y_pred