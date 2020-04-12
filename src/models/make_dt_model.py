import paths
import os.path
import sklearn.tree
import sklearn.metrics
import sklearn.model_selection
import pandas as pd
import numpy as np
import src.models.get_test_train_data


def make_dt_model(processed_file_path, split):
    X_train, X_test, y_train, y_test = src.models.get_test_train_data.zscaled_data(processed_file_path, split)
    dt_classifier = sklearn.tree.DecisionTreeClassifier(max_depth=8, min_samples_leaf=3)
    dt_classifier.fit(X_train, y_train)
    result = dt_classifier.predict(X_test)
    print("Classification report for classifier %s:\n\n%s\n"
          % (dt_classifier, sklearn.metrics.classification_report(y_test, result)))


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.PROCESSED_DATA_DIR, "qws2_processed.csv")
    make_dt_model(processed_file_path, split=0.4)
