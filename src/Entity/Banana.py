import csv


class Banana:

    def __init__(self):
        self.attribute1 = []
        self.attribute2 = []
        self.classification = []

    def read_csv(self):
        with open('Bases/Banana.csv', newline='') as csv_file:
            base = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in base:
                get_column = list()
                for index, value in enumerate(row):
                    get_column.append(value)
                data = {
                    'a1': get_column[0],
                    'a2': get_column[1],
                    'c': get_column[2]
                }
                self.set_val(data)

    def set_val(self, data):
        self.attribute1.append(data['a1'])
        self.attribute2.append(data['a2'])
        self.classification.append(data['c'])

    def get_values(self):
        print(self.classification)

