import numpy as np
import os
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

bases = [adult, banana, blood, ctg, diabetes, ecoli, faults, german, glass, haberman, heart, ilpd, ionosphere,
         laryngeal1, laryngeal3, lithuanian, liver, magic, mammo, monk, phoneme, segmentation, sonar, thyroid,
         vehicle, vertebral, wbc, wdvg, weaning, wine]

base_name = ['adult', 'banana', 'blood', 'ctg', 'diabetes', 'ecoli', 'faults', 'german', 'glass', 'haberman', 'heart',
             'ilpd', 'ionosphere', 'laryngeal1', 'laryngeal3', 'lithuanian', 'liver', 'magic', 'mammo', 'monk',
             'phoneme', 'segmentation', 'sonar', 'thyroid', 'vehicle', 'vertebral', 'wbc', 'wdvg', 'weaning', 'wine']

for base in base_name:
    classifier_directory = '../ClassifierParam/' + base + '/'
    result_directory = '../ClassifierResult/' + base + '/'
    if not os.path.exists(classifier_directory):
        os.makedirs(classifier_directory)
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

for idx, base in enumerate(bases):
    proba_final = []
    for i in range(0, 20):
        classifiers = base.get_trained_classifiers(3)
        results, proba = base.get_prod_rule(classifiers)
        proba_final.append(proba)
        with open('../ClassifierParam/' + base_name[idx] + '/BordaCounteRule' + repr(i) + '.csv', 'w') as f:
            for item in classifiers:
                f.write("%s\n" % item.base_estimator.get_params())
        del classifiers[:]
        with open('../ClassifierResult/' + base_name[idx] + '/BordaCounteRule.csv', 'w') as f:
            for index, proba in enumerate(proba_final):
                f.write(repr(index) + ": %.4f\n" % proba)
    with open('../ClassifierResult/' + base_name[idx] + '/BordaCounteRule.csv', 'a') as f:
        f.write("FinalProba: %.4f\n" % np.sum(proba_final) / len(proba_final))
