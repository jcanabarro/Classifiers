import numpy as np
import time
import sys

sys.path.append('/home/joao/Classifiers/')

from src.Entity.BasesObject.Adult import Adult
from src.Entity.BasesObject.Banana import Banana
from src.Entity.BasesObject.Blood import Blood
from src.Entity.BasesObject.CTG import Ctg
from src.Entity.BasesObject.Diabetes import Diabetes
from src.Entity.BasesObject.Ecoli import Ecoli
from src.Entity.BasesObject.Faults import Faults
from src.Entity.BasesObject.German import German
from src.Entity.BasesObject.Glass import Glass
from src.Entity.BasesObject.Haberman import Haberman
from src.Entity.BasesObject.Heart import Heart
from src.Entity.BasesObject.ILPD import Ilpd
from src.Entity.BasesObject.Ionosphere import Ionosphere
from src.Entity.BasesObject.Laryngeal1 import Laryngeal1
from src.Entity.BasesObject.Laryngeal3 import Laryngeal3
from src.Entity.BasesObject.Lithuanian import Lithuanian
from src.Entity.BasesObject.Liver import Liver
from src.Entity.BasesObject.Magic import Magic
from src.Entity.BasesObject.Mammo import Mammo
from src.Entity.BasesObject.Monk import Monk
from src.Entity.BasesObject.Phoneme import Phoneme
from src.Entity.BasesObject.Segmentation import Segmentation
from src.Entity.BasesObject.Sonar import Sonar
from src.Entity.BasesObject.Thyroid import Thyroid
from src.Entity.BasesObject.Vehicle import Vehicle
from src.Entity.BasesObject.Vertebral import Vertebral
from src.Entity.BasesObject.WBC import Wbc
from src.Entity.BasesObject.WDVG import Wdvg
from src.Entity.BasesObject.Weaning import Weaning
from src.Entity.BasesObject.Wine import Wine

adult = Adult()
banana = Banana()
blood = Blood()
ctg = Ctg()
diabetes = Diabetes()
ecoli = Ecoli()
faults = Faults()
german = German()
glass = Glass()
haberman = Haberman()
heart = Heart()
ilpd = Ilpd()
ionosphere = Ionosphere()
laryngeal1 = Laryngeal1()
laryngeal3 = Laryngeal3()
lithuanian = Lithuanian()
liver = Liver()
magic = Magic()
mammo = Mammo()
monk = Monk()
phoneme = Phoneme()
segmentation = Segmentation()
sonar = Sonar()
thyroid = Thyroid()
vehicle = Vehicle()
vertebral = Vertebral()
wbc = Wbc()
wdvg = Wdvg()
weaning = Weaning()
wine = Wine()

bases = [mammo, monk, phoneme, segmentation, sonar, thyroid, vehicle, diabetes]

base_name = ['mammo', 'monk', 'phoneme', 'segmentation', 'sonar', 'thyroid', 'vehicle''diabetes']

for idx, base in enumerate(bases):
    borda_proba_final = []
    prod_proba_final = []
    mean_proba_final = []
    median_proba_final = []
    max_proba_final = []
    min_proba_final = []
    sum_proba_final = []
    maj_proba_final = []

    borda_execution_time = []
    prod_execution_time = []
    mean_execution_time = []
    median_execution_time = []
    max_execution_time = []
    min_execution_time = []
    sum_execution_time = []
    maj_execution_time = []

    for i in range(0, 20):
        classifiers = base.get_trained_classifiers(3)
        classifiers = base.set_best_params(classifiers)
        start_time = time.time()
        borda_results, borda_proba = base.get_borda_rule(classifiers)
        borda_execution_time.append(time.time() - start_time)
        borda_proba_final.append(borda_proba)

        start_time = time.time()
        prod_results, prod_proba = base.get_prod_rule(classifiers)
        prod_execution_time.append(time.time() - start_time)
        prod_proba_final.append(prod_proba)

        start_time = time.time()
        mean_results, mean_proba = base.get_mean_rule(classifiers)
        mean_execution_time.append(time.time() - start_time)
        mean_proba_final.append(mean_proba)

        start_time = time.time()
        median_results, median_proba = base.get_median_rule(classifiers)
        median_execution_time.append(time.time() - start_time)
        median_proba_final.append(median_proba)

        start_time = time.time()
        max_results, max_proba = base.get_max_rule(classifiers)
        max_execution_time.append(time.time() - start_time)
        max_proba_final.append(max_proba)

        start_time = time.time()
        min_results, min_proba = base.get_min_rule(classifiers)
        min_execution_time.append(time.time() - start_time)
        min_proba_final.append(min_proba)

        start_time = time.time()
        sum_results, sum_proba = base.get_sum_rule(classifiers)
        sum_execution_time.append(time.time() - start_time)
        sum_proba_final.append(sum_proba)

        start_time = time.time()
        maj_results, maj_proba = base.get_majority_rule(classifiers)
        maj_execution_time.append(time.time() - start_time)
        maj_proba_final.append(maj_proba)

        with open('../ClassifierParam/' + base_name[idx] + '.csv', 'a') as f:
            f.write("Execution %d:\n" % i)
            for item in classifiers:
                f.write("\t%s\n" % item.base_estimator.get_params())
        del classifiers[:]

        with open('../ClassifierResult/' + base_name[idx] + '.csv', 'w') as f:
            f.write("Borda Time\tProd Time\tMean Time\tMedian Time\tMax Time\tMin Time\tSum Time\tMaj Time\n")
            for index, proba in enumerate(borda_proba_final):
                f.write(repr(index) + ": %.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f "
                                      "%.4f\t%.4f %.4f\n"
                        % (proba, borda_execution_time[index], prod_proba_final[index], prod_execution_time[index],
                           mean_proba_final[index], mean_execution_time[index], median_proba_final[index],
                           median_execution_time[index], max_proba_final[index], max_execution_time[index],
                           min_proba_final[index], min_execution_time[index], sum_proba_final[index],
                           sum_execution_time[index]
                           , maj_proba_final[index], maj_execution_time[index]))
    with open('../ClassifierResult/' + base_name[idx] + '.csv', 'a') as f:
        f.write("\nBase Means\n")
        f.write("%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\t%.4f %.4f\n"
                % (float(np.sum(borda_proba_final) / len(borda_proba_final)),
                   float(np.sum(borda_execution_time) / len(borda_execution_time)),
                   float(np.sum(prod_proba_final) / len(prod_proba_final)),
                   float(np.sum(prod_execution_time) / len(prod_execution_time)),
                   float(np.sum(mean_proba_final) / len(mean_proba_final)),
                   float(np.sum(mean_execution_time) / len(mean_execution_time)),
                   float(np.sum(median_proba_final) / len(median_proba_final)),
                   float(np.sum(median_execution_time) / len(median_execution_time)),
                   float(np.sum(max_proba_final) / len(max_proba_final)),
                   float(np.sum(max_execution_time) / len(max_execution_time)),
                   float(np.sum(min_proba_final) / len(min_proba_final)),
                   float(np.sum(min_execution_time) / len(min_execution_time)),
                   float(np.sum(sum_proba_final) / len(sum_proba_final)),
                   float(np.sum(sum_execution_time) / len(sum_execution_time)),
                   float(np.sum(maj_proba_final) / len(maj_proba_final)),
                   float(np.sum(maj_execution_time) / len(maj_execution_time))))
