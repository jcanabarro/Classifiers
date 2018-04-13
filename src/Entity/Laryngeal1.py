import csv


class Laryngeal1:

    def __init__(self):
        self.attribute1 = []
        self.attribute2 = []
        self.attribute3 = []
        self.attribute4 = []
        self.attribute5 = []
        self.attribute6 = []
        self.attribute7 = []
        self.attribute8 = []
        self.attribute9 = []
        self.attribute10 = []
        self.attribute11 = []
        self.attribute12 = []
        self.attribute13 = []
        self.attribute14 = []
        self.attribute15 = []
        self.attribute16 = []
        self.classification = []

    def read_csv(self):
        with open('Bases/Laryngeal1.csv', newline='') as csv_file:
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
                    'a7': get_column[6],
                    'a8': get_column[7],
                    'a9': get_column[8],
                    'a10': get_column[9],
                    'a11': get_column[10],
                    'a12': get_column[11],
                    'a13': get_column[12],
                    'a14': get_column[13],
                    'a15': get_column[14],
                    'a16': get_column[15],
                    'c': get_column[16]
                }
                self.set_val(data)

    def set_val(self, data):
        self.attribute1.append(data['a1'])
        self.attribute2.append(data['a2'])
        self.attribute3.append(data['a3'])
        self.attribute4.append(data['a4'])
        self.attribute5.append(data['a5'])
        self.attribute6.append(data['a6'])
        self.attribute7.append(data['a7'])
        self.attribute8.append(data['a8'])
        self.attribute9.append(data['a9'])
        self.attribute10.append(data['a10'])
        self.attribute11.append(data['a11'])
        self.attribute12.append(data['a12'])
        self.attribute13.append(data['a13'])
        self.attribute14.append(data['a14'])
        self.attribute15.append(data['a15'])
        self.attribute16.append(data['a16'])
        self.classification.append(data['c'])

    def get_values(self):
        print(self.classification)
