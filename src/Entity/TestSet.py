import numpy as np


class TestSet:

    def __init__(self, test_attributes, test_class):
        self.test_attributes = test_attributes
        self.test_class = test_class

    def predictions_result(self, classifiers):
        predictions_ = list()
        for classifier in classifiers:
            predictions_.append(classifier.predict_proba(self.test_attributes))
        return predictions_

    def borda_count(self, classifiers):
        final_prediction = list()
        for classifier in classifiers:
            predictions = []
            for prediction in classifier.predict_proba(self.test_attributes):
                sorted_by_class = sorted([(prob, index + 1) for index, prob in enumerate(prediction)])
                sorted_by_index = sorted([(index, weight + 1) for weight, (prob, index) in enumerate(sorted_by_class)])
                predictions.append([weight for prob, weight in sorted_by_index])
            final_prediction.append(predictions)
        return np.argmax(np.sum(np.array(final_prediction), axis=0), axis=-1)

    def ranking_rule(self, classifiers):
        final_prediction = list()
        for classifier in classifiers:
            predictions = []
            for prediction in classifier.predict_proba(self.test_attributes):
                sorted_by_class = sorted([(prob, index + 1) for index, prob in enumerate(prediction)], reverse=True)
                sorted_by_index = sorted([(index, weight + 1) for weight, (prob, index) in enumerate(sorted_by_class)])
                predictions.append([weight for prob, weight in sorted_by_index])
            final_prediction.append(predictions)
        return np.argmin(np.sum(np.array(final_prediction), axis=0), axis=-1)

    def prod_rule(self, classifiers):
        return np.argmax(np.prod(self.predictions_result(classifiers), axis=0), axis=-1)

    def max_rule(self, classifiers):
        return np.argmax(np.max(self.predictions_result(classifiers), axis=0), axis=-1)

    def min_rule(self, classifiers):
        return np.argmax(np.min(self.predictions_result(classifiers), axis=0), axis=-1)

    def median_rule(self, classifiers):
        return np.argmax(np.median(self.predictions_result(classifiers), axis=0), axis=-1)

    def mean_rule(self, classifiers):
        return np.argmax(np.mean(self.predictions_result(classifiers), axis=0), axis=-1)

    def sum_rule(self, classifiers):
        return np.argmax(np.sum(self.predictions_result(classifiers), axis=0), axis=-1)

    def majority_rule(self, classifiers):
        pass
