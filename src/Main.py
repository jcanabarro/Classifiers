from src.Entity.BasesObject.Banana import Banana

banana = Banana()

knn = banana.get_knn(3)
best_param, knn = banana.get_knn_best_param(knn)
banana.get_tested_classifier(knn, "knn")
print("Best Parameters: ", best_param)