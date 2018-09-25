import pandas as pd
from scipy.stats import kruskal, mannwhitneyu


def calculate_mannwhitne(classifiers_result):
    mann_result = []
    for i in range(len(classifiers_result)):
        for j in range(i + 1, len(classifiers_result)):
            result = mannwhitneyu(classifiers_result[i], classifiers_result[j], alternative="two-sided")
            mann_result.append((i, j, *result))
    return mann_result


data_frame = pd.read_csv("../../ClassifierResult/wine.csv")
data_frame = data_frame.drop(data_frame.index[20])
methods_names = ['Borda', 'Prod', 'Mean', 'Median', 'Max', 'Min', 'Sum', 'Majority', 'Ranking']

methods_scores_fm = tuple(data_frame[name] for name in data_frame)
kruskal_h, kruskal_pvalue = kruskal(*methods_scores_fm)

if kruskal_pvalue < 0.05:
    print("It is significant to Kruskal Wallis: %f" % kruskal_pvalue)
    for result in calculate_mannwhitne(methods_scores_fm):
        i, j, mann_z, mann_pvalue = result
        if mann_pvalue < 0.05:
            print("\tIt is significant between the instances %s and %s" % (methods_names[i], methods_names[j]), end="")
        else:
            print("\tNon-significant between the instances %s and %s" % (methods_names[i], methods_names[j]), end="")
        print(", with the value of p: %f" % mann_pvalue)
else:
    print("Non-significant result to Kruskal Wallis: %f" % kruskal_pvalue)
