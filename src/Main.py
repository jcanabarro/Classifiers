from Entity.Glass import Glass
from Entity.Haberman import Haberman
from Entity.Heart import Heart
from Entity.ILPD import ILPD
from src.Entity.Adult import Adult
from src.Entity.Banana import Banana
from src.Entity.Blood import Blood
from src.Entity.CTG import CTG
from src.Entity.Diabetes import Diabetes
from src.Entity.Ecoil import Ecoli
from src.Entity.Faults import Faults
from src.Entity.German import German

banana = Banana()
adult = Adult()
blood = Blood()
ctg = CTG()
ecoli = Ecoli()
faults = Faults()
german = German()
diabetes = Diabetes()
glass = Glass()
haberman = Haberman()
heart = Heart()
ilpd = ILPD()


banana.read_csv()
adult.read_csv()
blood.read_csv()
ctg.read_csv()
ecoli.read_csv()
faults.read_csv()
german.read_csv()
diabetes.read_csv()
glass.read_csv()
haberman.read_csv()
heart.read_csv()
ilpd.read_csv()

