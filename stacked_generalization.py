from sklearn.cross_validation import StratifiedKFold

class StackedGeneralization:
    def __init__(self, n_folds, train_data, train_target, test_data):
        self.n_folds = n_folds
        self.train_data = train_data
        self.train_target = train_target
        self.test_data = test_data

        self.skf = StratifiedKFold(y=train_target, n_folds=n_folds)

    def guess_layer0_with_partition(self, generalizer):
        generalizer_prediction = numpy.array([])
        for train_index, test_index in self.skf:
            generalizer.train(self.train_data[train_index], self.train_target[train_index])
            generalizer_prediction = numpy.append(
                generalizer_prediction,
                generalizer.predict(self.train_data[test_index]))

        reorder_index = [test_index for _, test_indices in self.skf for test_index in test_indices]
        return(generalizer_prediction[reorder_index])

    def guess_layer0_with_whole(self, generalizer):
        generalizer.train(self.train_data, self.train_target)
        return(generalizer.predict(test_data))

    @staticmethod
    def merge_generalizer_predictions(predictions):
        return(numpy.vstack(predictions).T)
