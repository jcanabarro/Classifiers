import pandas as pd

from src.Entity.Constants import Constants


def removing_data(df):
    columns = ['Oracle', 'Single']
    df.drop(columns, inplace=True, axis=1)
    last_row = df.iloc[20]
    df = df.drop(df.index[20])
    return df, last_row


methods_names = Constants.TABLE_COMBINER_METHODS_NAME
base_name = Constants.STRING_BASE_NAME

with open('../FinalTable.csv', 'a') as f:
    f.write("Bases," + Constants.TABLE_HEADER)

for name in base_name:
    print("Reading " + name + " base")
    data_frame = pd.read_csv("../ClassifierResult/" + name + ".csv")
    data_frame, combiner_mean = removing_data(data_frame)
    standard_deviation = data_frame.std(axis=0)

    with open('../FinalTable.csv', 'a') as f:
        f.write("%s," % name.capitalize())
        for method in methods_names:
            if method != 'Sum':
                f.write("{:.4f} $\pm${:.4s},".format(combiner_mean[method], repr(standard_deviation[method])))
            else:
                f.write("{:.4f} $\pm${:.4s}\n".format(combiner_mean[method], repr(standard_deviation[method])))

    with open('../UnformattedFinalTable.csv', 'a') as f:
        f.write("%s," % name.capitalize())
        for method in methods_names:
            if method != 'Sum':
                f.write("{:.4f},".format(combiner_mean[method]))
            else:
                f.write("{:.4f}\n".format(combiner_mean[method]))

