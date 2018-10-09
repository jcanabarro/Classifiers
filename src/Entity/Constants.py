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


class Constants:
    OBJECT_LIST = [Adult(), Banana(), Blood(), Ctg(), Diabetes(), Ecoli(), Faults(), German(), Glass(), Haberman(),
                   Heart(), Ilpd(), Ionosphere(), Laryngeal1(), Laryngeal3(), Lithuanian(), Liver(), Magic(),
                   Mammo(), Monk(), Phoneme(), Segmentation(), Sonar(), Thyroid(), Vehicle(), Vertebral(), Wbc(),
                   Wdvg(), Weaning(), Wine()]

    STRING_BASE_NAME = ['adult', 'banana', 'blood', 'ctg', 'diabetes', 'ecoli', 'faults', 'german', 'glass', 'haberman',
                        'heart', 'ilpd', 'ionosphere', 'laryngeal1', 'laryngeal3', 'lithuanian', 'liver', 'magic',
                        'mammo', 'monk', 'phoneme', 'segmentation', 'sonar', 'thyroid', 'vehicle', 'vertebral', 'wbc',
                        'wdvg', 'weaning', 'wine']

    COMBINER_METHODS_NAME = ['Borda', 'Majority', 'Max', 'Mean', 'Median', 'Min', 'Oracle', 'Prod', 'Ranking', 'Single', 'Sum']

    TABLE_COMBINER_METHODS_NAME = ['Borda', 'Majority', 'Max', 'Mean', 'Median', 'Min', 'Prod', 'Ranking', 'Sum']

    GOALS_TABLE_COMBINER_METHODS_NAME = ['Oracle', 'Single']

    CSV_HEADER = "Borda,Majority,Max,Mean,Median,Min,Oracle,Prod,Ranking,Single,Sum\n"

    TABLE_HEADER = "Borda,Majority,Max,Mean,Median,Min,Prod,Ranking,Sum\n"

    GOALS_TABLE_HEADER = "Oracle,Single\n"
