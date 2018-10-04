import time

# import sys
# sys.path.append('/home/joao/Classifiers/')
from src.Entity.Constants import Constants


def classifier_proba_mean(predictions):
    prediction_mean = 0
    for prediction in predictions:
        prediction_mean += prediction[0]
    return float(prediction_mean / len(predictions))


bases = Constants.OBJECT_LIST
base_name = Constants.STRING_BASE_NAME

for idx, base in enumerate(bases):

    final_proba = {
        'borda': [],
        'prod': [],
        'mean': [],
        'median': [],
        'max': [],
        'min': [],
        'sum': [],
        'majority': [],
        'ranking': []
    }

    classifiers = []
    for i in range(0, 20):
        classifiers = base.get_trained_classifiers(3)
        if base_name[idx] != 'blood':
            # The base blood cannot converge for the best params.
            # If remove this conditional probably will generate a infinity executions
            # Remove this just if you don't use this base, our if you change the classifiers
            classifiers = base.set_best_params(classifiers)

        for name in final_proba:
            start_time = time.time()
            result = base.get_rule(classifiers, name)
            final_time = time.time() - start_time
            final_proba[name].append((result, final_time))

        with open('../ClassifierParam/' + base_name[idx] + '.csv', 'a') as f:
            f.write("Execution %d:\n" % i)
            for item in classifiers:
                f.write("\t%s\n" % item.base_estimator.get_params())
        del classifiers[:]

    with open('../ClassifierResult/' + base_name[idx] + '.csv', 'w') as f:
        f.write("Borda,Majority,Max,Mean,Median,Min,Prod,Ranking,Sum\n")
        for j in range(0, len(final_proba['borda'])):
            for name in sorted(final_proba):
                if name != 'sum':
                    f.write("%.4f," % (final_proba[name][j][0]))
                else:
                    f.write("%.4f\n" % (final_proba[name][j][0]))

    with open('../ClassifierResult/' + base_name[idx] + '.csv', 'a') as f:
        for name in sorted(final_proba):
            proba_mean = classifier_proba_mean(final_proba[name])
            if name != 'sum':
                f.write("%.4f," % proba_mean)
            else:
                f.write("%.4f\n" % proba_mean)
