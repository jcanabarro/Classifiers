import csv


class Ionosphere:

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
        self.attribute17 = []
        self.attribute18 = []
        self.attribute19 = []
        self.attribute20 = []
        self.attribute21 = []
        self.attribute22 = []
        self.attribute23 = []
        self.attribute24 = []
        self.attribute25 = []
        self.attribute26 = []
        self.attribute27 = []
        self.attribute28 = []
        self.attribute29 = []
        self.attribute30 = []
        self.attribute31 = []
        self.attribute32 = []
        self.attribute33 = []
        self.attribute34 = []
        self.classification = []

    def read_csv(self):
        with open('Bases/Ionosphere.csv', newline='') as csv_file:
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
                    'a17': get_column[16],
                    'a18': get_column[17],
                    'a19': get_column[18],
                    'a20': get_column[19],
                    'a21': get_column[20],
                    'a22': get_column[21],
                    'a23': get_column[22],
                    'a24': get_column[23],
                    'a25': get_column[24],
                    'a26': get_column[25],
                    'a27': get_column[26],
                    'a28': get_column[27],
                    'a29': get_column[28],
                    'a30': get_column[29],
                    'a31': get_column[30],
                    'a32': get_column[31],
                    'a33': get_column[32],
                    'a34': get_column[33],
                    'c': get_column[34]
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
        self.attribute17.append(data['a17'])
        self.attribute18.append(data['a18'])
        self.attribute19.append(data['a19'])
        self.attribute20.append(data['a20'])
        self.attribute21.append(data['a21'])
        self.attribute22.append(data['a22'])
        self.attribute23.append(data['a23'])
        self.attribute24.append(data['a24'])
        self.attribute25.append(data['a25'])
        self.attribute26.append(data['a26'])
        self.attribute27.append(data['a27'])
        self.attribute28.append(data['a28'])
        self.attribute29.append(data['a29'])
        self.attribute30.append(data['a30'])
        self.attribute31.append(data['a31'])
        self.attribute32.append(data['a32'])
        self.attribute33.append(data['a33'])
        self.attribute34.append(data['a34'])
        self.classification.append(data['c'])

    def get_values(self):
        print(self.classification)
