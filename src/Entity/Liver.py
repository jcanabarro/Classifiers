import csv


class Liver:

    def __init__(self):
        self.attribute1 = []
        self.attribute2 = []
        self.attribute3 = []
        self.attribute4 = []
        self.attribute5 = []
        self.attribute6 = []
        self.classification = []

    def read_csv(self):
        with open('Bases/Liver.csv', newline='') as csv_file:
            base = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in base:
                get_column = list()
                for index, value in enumerate(row):
                    get_column.append(value)
                data = {
                    'a1': get_column[0],
                    'a2': get_column[1],
                    'a3': get_column[2],
                    'a4': get_column[3],
                    'a5': get_column[4],
                    'a6': get_column[5],
                    'c': get_column[6]
                }
                self.set_val(data)

    def set_val(self, data):
        self.attribute1.append(data['a1'])
        self.attribute2.append(data['a2'])
        self.attribute3.append(data['a3'])
        self.attribute4.append(data['a4'])
        self.attribute5.append(data['a5'])
        self.attribute6.append(data['a6'])
        self.classification.append(data['c'])

    def get_values(self):
        print(self.classification)
