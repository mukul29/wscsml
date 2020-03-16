import paths
import os.path
import sklearn.svm
import sklearn.multiclass
import pandas as pd
import numpy as np


def make_svm_model(processed_file_path, version):
    # TODO: Use GridSearchCV to optimize
    qws_complete_dataframe = pd.read_csv(processed_file_path, header=None)
    qws_complete_numpy_array = qws_complete_dataframe.to_numpy()
    X_test = qws_complete_numpy_array[:, 0:9].astype('float32')
    np.random.shuffle(qws_complete_numpy_array)
    X = qws_complete_numpy_array[:, 0:9].astype('float32')
    y = qws_complete_numpy_array[:, 10].astype('int32')
    svm_classifier = sklearn.multiclass.OneVsOneClassifier(
        sklearn.svm.SVC(C=1, kernel='rbf', max_iter=1000, gamma='auto'))
    svm_classifier.fit(X, y)


if __name__ == "__main__":
    processed_file_path = os.path.join(paths.processed_data_dir, "qws1_processed.csv")
    make_svm_model(processed_file_path, 1)
