import pandas as pd

methods_names = ['Borda', 'Majority', 'Max', 'Mean', 'Median', 'Min', 'Prod', 'Raking', 'Sum']

base_name = ['adult', 'banana', 'wine']

with open('../ClassifierResult/FinalTable.csv', 'a') as f:
    f.write("Bases,Borda,Max,Mean,Median,Min,Majority,Prod,Raking,Sum\n")

for name in base_name:
    print("Reading " + name + " base")
    data_frame = pd.read_csv("../ClassifierResult/" + name + ".csv")
    combiner_mean = data_frame.iloc[20]
    data_frame = data_frame.drop(data_frame.index[20])
    standard_deviation = data_frame.std(axis=0)
    with open('../ClassifierResult/FinalTable.csv', 'a') as f:
        f.write("%s," % name.capitalize())
        for idx in range(0, len(combiner_mean) - 1):
            f.write("{:.4f} \pm{:.4s},".format(combiner_mean[idx], repr(standard_deviation[idx])))
        f.write("{:.4f} \pm{:.4s}\n".format(combiner_mean[len(combiner_mean) - 1],
                                            repr(standard_deviation[len(combiner_mean) - 1])))
