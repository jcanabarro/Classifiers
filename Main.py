from Adult import Adult
from Banana import Banana
from Blood import Blood
from CTG import CTG
from Diabetes import Diabetes
from Ecoil import Ecoil
from Faults import Faults
from German import German

banana = Banana()
adult = Adult()
blood = Blood()
ctg = CTG()
ecoil = Ecoil()
faults = Faults()
german = German()
diabetes = Diabetes()


banana.read_csv()
adult.read_csv()
blood.read_csv()
ctg.read_csv()
ecoil.read_csv()
faults.read_csv()
german.read_csv()
diabetes.read_csv()


