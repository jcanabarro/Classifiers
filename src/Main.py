from src.Entity.BasesObject.Banana import Banana

banana = Banana()

knn = banana.get_trained_classifiers(3)
print(knn)
# svm_best_param, svm = banana.get_svm_best_param(svm)
# banana.get_tested_classifier(svm, "svm")
# print("Best Parameters: ", svm_best_param)