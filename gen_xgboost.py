import xgboost as xgb
import numpy
from generalizer import Generalizer

class Xgboost(Generalizer):
    def name(self):
        return("xg_boost")

    def train(self, data, label):
        dtrain = xgb.DMatrix(data, label = label)
        params = {
            'objective': 'binary:logistic',
            'eta': 1.0
        }
        num_round = 10
        self.model = xgb.train(params, dtrain, num_round)

    def predict(self, data):
        dmatrix = xgb.DMatrix(data)
        predicted = self.model.predict(dmatrix)
        return(numpy.vstack((1 - predicted, predicted)).T)