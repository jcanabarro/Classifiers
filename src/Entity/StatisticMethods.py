import pandas as pd
from scipy.stats import kruskal


base_name = ['adult', 'banana', 'blood', 'ctg', 'diabetes', 'ecoli', 'faults', 'german', 'glass', 'haberman', 'heart',
             'ilpd', 'ionosphere', 'laryngeal1', 'laryngeal3', 'lithuanian', 'liver', 'magic', 'mammo', 'monk',
             'phoneme', 'segmentation', 'sonar', 'thyroid', 'vehicle', 'vertebral', 'wbc', 'wdvg', 'weaning', 'wine']

for name in base_name:
    print("Reading " + name + " base", end="")
    data_frame = pd.read_csv("../../ClassifierResult/" + name + ".csv")
    data_frame = data_frame.drop(data_frame.index[20])

    methods_scores_fm = tuple(data_frame[name] for name in data_frame)
    kruskal_h, kruskal_pvalue = kruskal(*methods_scores_fm)

    if kruskal_pvalue < 0.05:
        print(" It is significant to Kruskal Wallis: %f" % kruskal_pvalue)
    else:
        print(" Non-significant result to Kruskal Wallis: %f" % kruskal_pvalue)
