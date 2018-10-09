import pandas as pd
from scipy.stats import kruskal
from src.Entity.Constants import Constants

base_name = Constants.STRING_BASE_NAME


def format_data_frame(df, columns):
    df = df[df.columns.difference(columns)]
    df = df.drop(df.index[20])
    return df


for name in base_name:
    print("Reading " + name + " base", end="")
    data_frame = pd.read_csv("../ClassifierResult/" + name + ".csv")
    data_frame = format_data_frame(data_frame, Constants.GOALS_COMBINER_METHODS_NAME)
    methods_scores_fm = tuple(data_frame[name] for name in data_frame)
    kruskal_h, kruskal_pvalue = kruskal(*methods_scores_fm)

    if kruskal_pvalue < 0.05:
        print(" It is significant to Kruskal Wallis: %f" % kruskal_pvalue)
    else:
        print(" Non-significant result to Kruskal Wallis: %f" % kruskal_pvalue)
