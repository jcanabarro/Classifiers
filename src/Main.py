from src.Entity.BasesObject.Adult import Adult
import numpy as np

adult = Adult()

classifiers = adult.get_trained_classifiers(3)

results = adult.get_borda_rule(classifiers)

print(results)

# np.savetxt("../ExecutionResult/resutls.csv", results, delimiter=",", fmt="%f")
