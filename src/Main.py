import numpy as np
import time
import sys

# sys.path.append('/home/joao/Classifiers/')

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

bases = [wine]

base_name = ['wine']

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
        # classifiers = base.set_best_params(classifiers)

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
        f.write("Borda,Max,Mean,Median,Min,Majority,Prod,Raking,Sum\n")
        for j in range(0, len(final_proba['borda'])):
            for name in sorted(final_proba):
                if name != 'sum':
                    f.write("%.4f," % (final_proba[name][j][0]))
                else:
                    f.write("%.4f\n" % (final_proba[name][j][0]))

    with open('../ClassifierResult/' + base_name[idx] + '.csv', 'a') as f:
        for name in sorted(final_proba):
            proba_mean = float(np.sum(final_proba[name]) / len(final_proba[name]))
            if name != 'sum':
                f.write("%.4f," % proba_mean)
            else:
                f.write("%.4f\n" % proba_mean)
