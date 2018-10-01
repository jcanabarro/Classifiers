import pandas as pd

methods_names = ['Borda', 'Majority', 'Max', 'Mean', 'Median', 'Min', 'Prod', 'Ranking', 'Sum']

base_name = ['adult', 'banana', 'blood', 'ctg', 'diabetes', 'ecoli', 'faults', 'german', 'glass', 'haberman', 'heart',
             'ilpd', 'ionosphere', 'laryngeal1', 'laryngeal3', 'lithuanian', 'liver', 'magic', 'mammo', 'monk',
             'phoneme', 'segmentation', 'sonar', 'thyroid', 'vehicle', 'vertebral', 'wbc', 'wdvg', 'weaning', 'wine']

with open('../FinalTable.csv', 'a') as f:
    f.write("Bases,Borda,Max,Mean,Median,Min,Majority,Prod,Ranking,Sum\n")

for name in base_name:
    print("Reading " + name + " base")
    data_frame = pd.read_csv("../ClassifierResult/" + name + ".csv")
    combiner_mean = data_frame.iloc[20]
    data_frame = data_frame.drop(data_frame.index[20])
    standard_deviation = data_frame.std(axis=0)

    with open('../FinalTable.csv', 'a') as f:
        f.write("%s," % name.capitalize())
        for method in methods_names:
            if method != 'Sum':
                f.write("{:.4f} $\pm${:.4s},".format(combiner_mean[method], repr(standard_deviation[method])))
            else:
                f.write("{:.4f} $\pm${:.4s}\n".format(combiner_mean[method], repr(standard_deviation[method])))

