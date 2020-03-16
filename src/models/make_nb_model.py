import paths
import os.path
import sklearn.naive_bayes
import sklearn.metrics
import sklearn.model_selection
import pandas as pd
import numpy as np
import src.models.get_X_y


def make_nn_model(processed_file_path):
    qws_complete_dataframe = pd.read_csv(processed_file_path, header=None)
    qws_complete_numpy_array = qws_complete_dataframe.to_numpy()
    np.random.shuffle(qws_complete_numpy_array)

    X, y = src.models.get_X_y.get_X_y(qws_complete_numpy_array)

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.4)

    nb_classifier = sklearn.naive_bayes.MultinomialNB()
    nb_classifier.fit(X_train, y_train)

    result = nb_classifier.predict((X_test))
    print("Classification report for classifier %s:\n\n%s\n"
          % (nb_classifier, sklearn.metrics.classification_report(y_test, result)))


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.processed_data_dir, "qws2_processed.csv")
    make_nn_model(processed_file_path)
