import pandas as pd


class Banana:

    def __init__(self):
        self.df = []

    def read_csv(self):
        self.df = pd.read_csv('../Bases/Banana.csv')

    def get_values(self, attr):
        print(self.df[attr])
0