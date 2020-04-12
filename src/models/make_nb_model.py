import paths
import os.path
import sklearn.naive_bayes
import sklearn.metrics
import sklearn.model_selection
import pandas as pd
import numpy as np
import src.models.get_test_train_data

def make_nb_model(processed_file_path, split):
    X_train, X_test, y_train, y_test = src.models.get_test_train_data.min_max_scaled_data(processed_file_path, split)
    nb_classifier = sklearn.naive_bayes.MultinomialNB()
    nb_classifier.fit(X_train, y_train)

    result = nb_classifier.predict(X_test)
    print("Classification report for classifier %s:\n\n%s\n"
          % (nb_classifier, sklearn.metrics.classification_report(y_test, result)))


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.PROCESSED_DATA_DIR, "qws1_processed.csv")
    make_nb_model(processed_file_path, split=0.4)
