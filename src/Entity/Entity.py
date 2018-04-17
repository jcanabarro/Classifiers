import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import numpy as np


class Entity:

    def __init__(self, path):
        self.data_frame = pd.read_csv(path)
        self.classifier = np.split(self.data_frame, [len(self.data_frame.columns) - 1], axis=1)
        self.train_attributes, self.test_attributes, self.train_class, self.test_class = train_test_split(
            self.classifier[0],
            self.classifier[1],
            test_size=0.5,
            train_size=0.5)
        self.test_attributes, self.validate_attributes,  self.test_class, self.validate_class = train_test_split(
            self.test_attributes,
            self.test_class,
            test_size=0.5,
            train_size=0.5)

    def get_value(self, attr):
        return self.data_frame[attr]

    def get_svm(self):
        self.classifier = svm.SVC()
        # In this case we need to do a ravel because fit don't expect a 1d matrix
        self.classifier.fit(self.train_attributes, np.ravel(self.train_class))
        return self.classifier.predict(self.test_attributes), self.test_class

