import csv


class Sonar:

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
        self.attribute35 = []
        self.attribute36 = []
        self.attribute37 = []
        self.attribute38 = []
        self.attribute39 = []
        self.attribute40 = []
        self.attribute41 = []
        self.attribute42 = []
        self.attribute43 = []
        self.attribute44 = []
        self.attribute45 = []
        self.attribute46 = []
        self.attribute47 = []
        self.attribute48 = []
        self.attribute49 = []
        self.attribute50 = []
        self.attribute51 = []
        self.attribute52 = []
        self.attribute53 = []
        self.attribute54 = []
        self.attribute55 = []
        self.attribute56 = []
        self.attribute57 = []
        self.attribute58 = []
        self.attribute59 = []
        self.attribute60 = []
        self.classification = []

    def read_csv(self):
        with open('Bases/Sonar.csv', newline='') as csv_file:
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
                    'a35': get_column[34],
                    'a36': get_column[35],
                    'a37': get_column[36],
                    'a38': get_column[37],
                    'a39': get_column[38],
                    'a40': get_column[39],
                    'a41': get_column[40],
                    'a42': get_column[41],
                    'a43': get_column[42],
                    'a44': get_column[43],
                    'a45': get_column[44],
                    'a46': get_column[45],
                    'a47': get_column[46],
                    'a48': get_column[47],
                    'a49': get_column[48],
                    'a50': get_column[49],
                    'a51': get_column[50],
                    'a52': get_column[51],
                    'a53': get_column[52],
                    'a54': get_column[53],
                    'a55': get_column[54],
                    'a56': get_column[55],
                    'a57': get_column[56],
                    'a58': get_column[57],
                    'a59': get_column[58],
                    'a60': get_column[59],
                    'c': get_column[60]
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
        self.attribute35.append(data['a35'])
        self.attribute36.append(data['a36'])
        self.attribute37.append(data['a37'])
        self.attribute38.append(data['a38'])
        self.attribute39.append(data['a39'])
        self.attribute40.append(data['a40'])
        self.attribute41.append(data['a41'])
        self.attribute42.append(data['a42'])
        self.attribute43.append(data['a43'])
        self.attribute44.append(data['a44'])
        self.attribute45.append(data['a45'])
        self.attribute46.append(data['a46'])
        self.attribute47.append(data['a47'])
        self.attribute48.append(data['a48'])
        self.attribute49.append(data['a49'])
        self.attribute50.append(data['a50'])
        self.attribute51.append(data['a51'])
        self.attribute52.append(data['a52'])
        self.attribute53.append(data['a53'])
        self.attribute54.append(data['a54'])
        self.attribute55.append(data['a55'])
        self.attribute56.append(data['a56'])
        self.attribute57.append(data['a57'])
        self.attribute58.append(data['a58'])
        self.attribute59.append(data['a59'])
        self.attribute60.append(data['a60'])
        self.classification.append(data['c'])

    def get_values(self):
        print(self.classification)
