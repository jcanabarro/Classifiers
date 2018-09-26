import pandas as pd
from scipy.stats import kruskal


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

    if kruskal_pvalue < 0.05:
        print("\tIt is significant to Kruskal Wallis: %f" % kruskal_pvalue)
    else:
        print("\tNon-significant result to Kruskal Wallis: %f" % kruskal_pvalue)
