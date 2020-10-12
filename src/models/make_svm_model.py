import paths
import os.path
import sklearn.svm
import sklearn.metrics
import sklearn.multiclass
import sklearn.model_selection
import pandas as pd
import numpy as np
import src.models.get_test_train_data


def make_svm_model(processed_file_path, split):
    # TODO: Use GridSearchCV to optimize
    X_train, X_test, y_train, y_test = src.models.get_test_train_data.zscaled_data(processed_file_path, split)
    svm_classifier = sklearn.multiclass.OneVsOneClassifier(
        sklearn.svm.SVC(C=1, kernel='rbf', max_iter=1000, gamma='auto'))
    svm_classifier.fit(X_train, y_train)

    result = svm_classifier.predict(X_test)
    print("Classification report for classifier %s:\n%s\n"
          % (svm_classifier, sklearn.metrics.classification_report(y_test, result)))
    return result, y_test


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.PROCESSED_DATA_DIR, "qws2_processed.csv")
    make_svm_model(processed_file_path, split=0.4)