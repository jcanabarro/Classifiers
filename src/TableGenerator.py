import pandas as pd

from src.Entity.Constants import Constants

base_name = Constants.STRING_BASE_NAME

with open('../Tables/FinalTable.csv', 'a') as file:
    file.write("Bases," + Constants.TABLE_HEADER)

with open('../Tables/GoalsTable.csv', 'a') as file:
    file.write("Bases," + Constants.GOALS_TABLE_HEADER)


def write_on_csv(path, unformatted_path, name_base, mean, stdev, methods_names):
    with open(path, 'a') as f:
        f.write("%s," % name_base.capitalize())
        for method in methods_names:
            if method != methods_names[-1]:
                f.write("{:.4f} $\pm${:.4s},".format(mean[method], repr(stdev[method])))
            else:
                f.write("{:.4f} $\pm${:.4s}\n".format(mean[method], repr(stdev[method])))

    with open(unformatted_path, 'a') as f:
        f.write("%s," % name_base.capitalize())
        for method in methods_names:
            if method != methods_names[-1]:
                f.write("{:.4f},".format(mean[method]))
            else:
                f.write("{:.4f}\n".format(mean[method]))


def format_data_frame(df, columns):
    df = df[df.columns.difference(columns)]
    last_row = df.iloc[20]
    df = df.drop(df.index[20])
    return df, last_row


for name in base_name:
    print("Reading " + name + " base")
    main_data_frame = pd.read_csv("../ClassifierResult/" + name + ".csv")
    goals_data_frame = pd.read_csv("../ClassifierResult/" + name + ".csv")

    # Main Table
    data_frame, combiner_mean = format_data_frame(main_data_frame, Constants.GOALS_COMBINER_METHODS_NAME)
    standard_deviation = data_frame.std(axis=0)
    write_on_csv('../Tables/FinalTable.csv', '../Tables/UnformattedFinalTable.csv', name, combiner_mean,
                 standard_deviation, Constants.TABLE_COMBINER_METHODS_NAME)

    # Second Table
    data_frame, combiner_mean = format_data_frame(goals_data_frame, Constants.TABLE_COMBINER_METHODS_NAME)
    standard_deviation = data_frame.std(axis=0)
    write_on_csv('../Tables/GoalsTable.csv', '../Tables/UnformattedGoalsTable.csv', name, combiner_mean,
                 standard_deviation, Constants.GOALS_COMBINER_METHODS_NAME)
