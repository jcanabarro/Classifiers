import pandas as pd


class Entity:

    def __init__(self, path):
        self.data_frame = pd.read_csv(path)

    def get_value(self, attr):
        return self.data_frame[attr]
