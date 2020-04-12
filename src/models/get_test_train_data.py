import sklearn.preprocessing
import numpy as np
import pandas as pd
import sklearn.model_selection
import paths
import os.path
import matplotlib.pyplot as plt


def get_X_y(processed_file_path):
    qws_complete_dataframe = pd.read_csv(processed_file_path, header=None)
    qws_complete_numpy_array = qws_complete_dataframe.to_numpy()
    np.random.shuffle(qws_complete_numpy_array)
    X = qws_complete_numpy_array[:, 0:9].astype('float32')
    y = qws_complete_numpy_array[:, 10].astype('int32')
    return X, y


def zscaled_data(processed_file_path, split):
    X, y = get_X_y(processed_file_path)
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=split)
    scaler = sklearn.preprocessing.StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test


def min_max_scaled_data(processed_file_path, split):
    X, y = get_X_y(processed_file_path)
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=split)
    scaler = sklearn.preprocessing.MinMaxScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    X_train, y_train, X_test, y_test = min_max_scaled_data(os.path.join(paths.PROCESSED_DATA_DIR, "qws1_processed.csv"),
                                                           split=0.4)
    print(X_train.mean(axis=0))
    plt.plot(X_train)
    plt.figure()
    plt.plot(X_test)
    plt.show()
