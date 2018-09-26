import pandas as pd

methods_names = ['Borda', 'Majority', 'Max', 'Mean', 'Median', 'Min', 'Prod', 'Raking', 'Sum']

base_name = ['adult', 'banana', 'blood', 'ctg', 'diabetes', 'ecoli', 'faults', 'german', 'glass', 'haberman', 'heart',
             'ilpd', 'ionosphere', 'laryngeal1', 'laryngeal3', 'lithuanian', 'liver', 'magic', 'mammo', 'monk',
             'phoneme', 'segmentation', 'sonar', 'thyroid', 'vehicle', 'vertebral', 'wbc', 'wdvg', 'weaning', 'wine']

with open('../ClassifierResult/FinalTable.csv', 'a') as f:
    f.write("Bases,Borda,Max,Mean,Median,Min,Majority,Prod,Raking,Sum\n")

for name in base_name:
    print("Reading " + name + " base")
    data_frame = pd.read_csv("../ClassifierResult/" + name + ".csv")
    combiner_mean = data_frame.iloc[20]
    with open('../ClassifierResult/FinalTable.csv', 'a') as f:
        f.write("%s," % name)
        for idx in range(0, len(combiner_mean) - 2):
                f.write("%.4f," % combiner_mean[idx])
        f.write("%.4f\n" % combiner_mean[len(combiner_mean) - 1])
