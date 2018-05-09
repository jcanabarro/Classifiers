# from src.Entity.BasesObject.Adult import Adult
from src.Entity.BasesObject.Banana import Banana
# from src.Entity.BasesObject.Blood import Blood
# from src.Entity.BasesObject.CTG import Ctg
# from src.Entity.BasesObject.Diabetes import Diabetes
# from src.Entity.BasesObject.Ecoli import Ecoli
# from src.Entity.BasesObject.Faults import Faults
# from src.Entity.BasesObject.German import German
# from src.Entity.BasesObject.Glass import Glass
# from src.Entity.BasesObject.Haberman import Haberman
# from src.Entity.BasesObject.Heart import Heart
# from src.Entity.BasesObject.ILPD import Ilpd
# from src.Entity.BasesObject.Ionosphere import Ionosphere
# from src.Entity.BasesObject.Laryngeal1 import Laryngeal1
# from src.Entity.BasesObject.Laryngeal3 import Laryngeal3
# from src.Entity.BasesObject.Lithuanian import Lithuanian
# from src.Entity.BasesObject.Liver import Liver
# from src.Entity.BasesObject.Magic import Magic
# from src.Entity.BasesObject.Mammo import Mammo
# from src.Entity.BasesObject.Monk import Monk
# from src.Entity.BasesObject.Phoneme import Phoneme
# from src.Entity.BasesObject.Segmentation import Segmentation
# from src.Entity.BasesObject.Sonar import Sonar
# from src.Entity.BasesObject.Thyroid import Thyroid
# from src.Entity.BasesObject.Vehicle import Vehicle
# from src.Entity.BasesObject.Vertebral import Vertebral
# from src.Entity.BasesObject.WBC import Wbc
# from src.Entity.BasesObject.WDVG import Wdvg
# from src.Entity.BasesObject.Weaning import Weaning
# from src.Entity.BasesObject.Wine import Wine


# adult = Adult()
banana = Banana()
# blood = Blood()
# ctg = Ctg()
# ecoli = Ecoli()
# faults = Faults()
# german = German()
# diabetes = Diabetes()
# glass = Glass()
# haberman = Haberman()
# heart = Heart()
# ilpd = Ilpd()
# ionosphere = Ionosphere()
# laryngeal1 = Laryngeal1()
# laryngeal3 = Laryngeal3()
# lithuanian = Lithuanian()
# liver = Liver()
# magic = Magic()
# mammo = Mammo()
# monk = Monk()
# phoneme = Phoneme()
# segmentation = Segmentation()
# sonar = Sonar()
# thyroid = Thyroid()
# vehicle = Vehicle()
# vertebral = Vertebral()
# wbc = Wbc()
# wdvg = Wdvg()
# weaning = Weaning()
# wine = Wine()

knn = banana.get_knn(3)
best_param, knn = banana.get_knn_best_param(knn)
# classifier_result, classifier_proba = banana.get_tested_classifier(knn, 'knn')
# print("Best Param:", best_param)

