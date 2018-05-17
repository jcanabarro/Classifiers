from src.Entity.BasesObject.Banana import Banana

banana = Banana()

knn = banana.get_knn(3)
knn_best_param, knn = banana.get_knn_best_param(knn)
banana.get_tested_classifier(knn, "knn")
print("Best Parameters: ", knn_best_param)

svm = banana.get_svm()
svm_best_param, svm = banana.get_svm_best_param(svm)
banana.get_tested_classifier(svm, "svm")
print("Best Parameters: ", svm_best_param)

dt = banana.get_tree_decision()
dt_best_param, dt = banana.get_tree_decision_best_params(dt)
banana.get_tested_classifier(dt, "dt")
print("Best Parameters: ", dt_best_param)

nb = banana.get_naive_bayes()
nb_best_param, nb = banana.get_naive_bayes_best_param(nb)
banana.get_tested_classifier(nb, "nb")
print("Best Parameters: ", nb_best_param)

mlp = banana.get_mlp()
mlp_best_param, mlp = banana.get_mlp_best_param(mlp)
banana.get_tested_classifier(mlp, "mlp")
print("Best Parameters: ", mlp_best_param)
