from src.Entity.BasesObject.Banana import Banana

banana = Banana()

knn = banana.get_trained_classifiers(3)
# print(knn)

a = banana.get_sum_rule(knn)

print(a)
