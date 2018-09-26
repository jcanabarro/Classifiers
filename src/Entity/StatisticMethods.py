import pandas as pd
from scipy.stats import kruskal, mannwhitneyu


def calculate_mannwhitne(max_value, min_value):
    return mannwhitneyu(max_value, min_value, alternative="two-sided")


methods_names = ['Borda', 'Majority', 'Max', 'Mean', 'Median', 'Min', 'Prod', 'Raking', 'Sum']

base_name = ['adult', 'wine']

for name in base_name:
    print("Reading " + name + " base")
    data_frame = pd.read_csv("../../ClassifierResult/" + name + ".csv")
    combiner_mean = data_frame.iloc[20]
    data_frame = data_frame.drop(data_frame.index[20])

    evaluate_value = sorted((value, name) for value, name in zip(combiner_mean, methods_names))

    methods_scores_fm = tuple(data_frame[name] for name in data_frame)
    kruskal_h, kruskal_pvalue = kruskal(*methods_scores_fm)

    #  -2 -1
    if kruskal_pvalue < 0.05:
        print("\tIt is significant to Kruskal Wallis: %f" % kruskal_pvalue)
        mann_z, mann_pvalue = calculate_mannwhitne(data_frame[evaluate_value[0][1]], data_frame[evaluate_value[-1][1]])
        if mann_pvalue < 0.05:
            print("\tIt is significant between the instances", end="")
            with open('../../ClassifierMannWhitne/statistics.csv', 'a') as f:
                f.write("%s,%s,%s,%s,%f" % (name, 'yes', evaluate_value[0][1], evaluate_value[-1][1], mann_pvalue))
                f.write("\n")
        else:
            print("\tNon-significant between the instances", end="")
        print(" %s and %s, with the value of p: %f" % (evaluate_value[0][1], evaluate_value[-1][1], mann_pvalue))
    else:
        print("\tNon-significant result to Kruskal Wallis: %f" % kruskal_pvalue)
