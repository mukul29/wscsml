import sklearn.preprocessing
import numpy as np

def get_X_y(qws_complete_numpy_array):
    CORRECTION_MATRIX = np.array([1, 0, 0, 0, 0, 0, 0, 1, 0], dtype='float32')
    qws_attributes_numpy_array = qws_complete_numpy_array[:, 0:9].astype('float32')
    scaler = sklearn.preprocessing.MinMaxScaler()
    scaler.fit(qws_attributes_numpy_array)
    X = np.absolute(CORRECTION_MATRIX - scaler.transform(qws_attributes_numpy_array))
    y = qws_complete_numpy_array[:, 10].astype('int32')

    return X, y