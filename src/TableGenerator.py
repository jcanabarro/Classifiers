import pandas as pd

from src.Entity.Constants import Constants

methods_names = Constants.COMBINER_METHODS_NAME
base_name = Constants.STRING_BASE_NAME

with open('../FinalTable.csv', 'a') as f:
    f.write("Bases,Borda,Majority,Max,Mean,Median,Min,Prod,Ranking,Sum\n")

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

    with open('../UnformatFinalTable.csv', 'a') as f:
        f.write("%s," % name.capitalize())
        for method in methods_names:
            if method != 'Sum':
                f.write("{:.4f},".format(combiner_mean[method]))
            else:
                f.write("{:.4f}\n".format(combiner_mean[method]))

