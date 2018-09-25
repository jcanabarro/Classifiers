import pandas as pd
from scipy.stats import kruskal, mannwhitneyu


def calculate_mannwhitne(max_value, min_value):
    return mannwhitneyu(max_value, min_value, alternative="two-sided")


data_frame = pd.read_csv("../../ClassifierResult/wine.csv")
combiner_mean = data_frame.iloc[20]
data_frame = data_frame.drop(data_frame.index[20])
methods_names = sorted(['Borda', 'Prod', 'Mean', 'Median', 'Max', 'Min', 'Sum', 'Majority', 'Ranking'])

a = sorted((value, name) for value, name in zip(combiner_mean, methods_names))

methods_scores_fm = tuple(data_frame[name] for name in data_frame)
kruskal_h, kruskal_pvalue = kruskal(*methods_scores_fm)
#  -2 -1
if kruskal_pvalue < 0.05:
    print("It is significant to Kruskal Wallis: %f" % kruskal_pvalue)
    mann_z, mann_pvalue = calculate_mannwhitne(data_frame[a[0][1]], data_frame[a[-1][1]])
    if mann_pvalue < 0.05:
        print("\tIt is significant between the instances %s and %s" % (a[0][1], a[-1][1]), end="")
    else:
        print("\tNon-significant between the instances %s and %s" % (a[0][1], a[-1][1]), end="")
    print(", with the value of p: %f" % mann_pvalue)
else:
    print("Non-significant result to Kruskal Wallis: %f" % kruskal_pvalue)
