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

    def borda_rule(self, classifiers):
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
        final_prediction = list()
        for classifier in classifiers:
            predictions = []
            for idx, prediction in enumerate(classifier.predict_proba(self.test_attributes)):
                predictions.append(np.argmax(prediction))
            final_prediction.append(predictions)
        final_prediction = np.array(final_prediction).T
        predictions = []
        for votes in final_prediction:
            votes_count = {}
            for vote in votes:
                if vote not in votes_count:
                    votes_count[vote] = 1
                else:
                    votes_count[vote] += 1
            predictions.append(sorted(votes_count.items(), reverse=True)[0][0])
        return predictions

    def oracle_rule(self, classifiers):
        final_prediction = list()
        for classifier in classifiers:
            predictions = []
            for idx, prediction in enumerate(classifier.predict_proba(self.test_attributes)):
                predictions.append(np.argmax(prediction) + 1)
            final_prediction.append(predictions)
        final_prediction = np.array(final_prediction).T
        predictions = []
        class_result = self.test_class.values
        for idx, votes in enumerate(final_prediction):
            actual_size = len(predictions)
            for vote in votes:
                if vote == class_result[idx]:
                    predictions.append(vote)
                    break
            if actual_size == len(predictions):
                predictions.append(0)
        return predictions

    def single_best_rule(self, classifiers, index):
        return classifiers[index].predict_proba(self.test_attributes)
