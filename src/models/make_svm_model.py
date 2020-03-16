import paths
import os.path
import sklearn.svm
import sklearn.metrics
import sklearn.multiclass
import sklearn.model_selection
import pandas as pd
import numpy as np
import src.models.get_X_y


def make_svm_model(processed_file_path):
    # TODO: Use GridSearchCV to optimize
    qws_complete_dataframe = pd.read_csv(processed_file_path, header=None)
    qws_complete_numpy_array = qws_complete_dataframe.to_numpy()
    np.random.shuffle(qws_complete_numpy_array)

    X, y = src.models.get_X_y.get_X_y(qws_complete_numpy_array)

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.4)
    svm_classifier = sklearn.multiclass.OneVsOneClassifier(
        sklearn.svm.SVC(C=1, kernel='rbf', max_iter=1000, gamma='auto'))
    svm_classifier.fit(X_train, y_train)

    result = svm_classifier.predict((X_test))
    print("Classification report for classifier %s:\n%s\n"
          % (svm_classifier, sklearn.metrics.classification_report(y_test, result)))


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.processed_data_dir, "qws2_processed.csv")
    make_svm_model(processed_file_path)
