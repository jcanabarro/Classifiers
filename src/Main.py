from src.Entity.BasesObject.Adult import Adult

adult = Adult()

classifiers = adult.get_trained_classifiers(3)
# print(knn)

a = adult.get_prod_rule(classifiers)

print(a)
