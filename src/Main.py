from src.Entity.BasesObject.Banana import Banana

banana = Banana()

# knn = banana.get_knn(3, 30)
# knn_best_param, knn = banana.get_knn_best_param(knn)
# banana.get_tested_classifier(knn, "knn")
# print("Best Parameters: ", knn_best_param)

svm = banana.get_svm(30)
svm_best_param, svm = banana.get_svm_best_param(svm)
banana.get_tested_classifier(svm, "svm")
print("Best Parameters: ", svm_best_param)

# dt = banana.get_tree_decision(1)
# dt_best_param, dt = banana.get_tree_decision_best_params(dt)
# banana.get_tested_classifier(dt, "dt")
# print("Best Parameters: ", dt_best_param)
#
# nb = banana.get_naive_bayes(1)
# nb_best_param, nb = banana.get_naive_bayes_best_param(nb)
# banana.get_tested_classifier(nb, "nb")
# print("Best Parameters: ", nb_best_param)
#
# mlp = banana.get_mlp(1)
# mlp_best_param, mlp = banana.get_mlp_best_param(mlp)
# banana.get_tested_classifier(mlp, "mlp")
# print("Best Parameters: ", mlp_best_param)
