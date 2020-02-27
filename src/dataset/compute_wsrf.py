import numpy as np
import os.path
import paths
import pandas as pd
import sklearn.preprocessing
# from scipy import stats
# import matplotlib.pyplot as plt


def compute_wsrf(file_path, weights):
    """
    This function computes the WsRF of the dataset in the file with the weights specified and returns it
    :param weights: list
        floating point numbers representing weights of each attribute which add up to 1.0
    :param file_path: str
        string containing the path of the interim
    :return: tuple with complete numpy array and a numpy array containing WsRF scores (between 0 and 1) of each web service
    """
    ######################################################################################
    # Treat as constants
    # For attributes where lower is better, this value is set to 1
    CORRECTION_MATRIX = np.array([1, 0, 0, 0, 0, 0, 0, 1, 0], dtype='float32')
    ATTRIBUTES = ["Response Time",
                  "Availability",
                  "Throughput",
                  "Successability",
                  "Reliability",
                  "Compliance",
                  "Best Practices",
                  "Latency",
                  "Documentation"]
    ######################################################################################

    # Make a dataframe from the csv file, convert it to a 2-D numpy array
    qws_complete_dataframe = pd.read_csv(file_path, header=None)
    qws_complete_numpy_array = qws_complete_dataframe.to_numpy()
    # slice the array to get just the attributes and set dtype to float32
    qws_attributes_numpy_array = qws_complete_numpy_array[:, 0:9].astype('float32')

    # scale the data to a range of [0, 1] using MinMaxScaler
    scaler = sklearn.preprocessing.MinMaxScaler()
    scaler.fit(qws_attributes_numpy_array)
    qws_normalized_attributes = np.absolute(CORRECTION_MATRIX - scaler.transform(qws_attributes_numpy_array))

    # form a numpy array of the external weights
    external_weights = np.array(weights, dtype='float32')
    qws_weighted_attributes = qws_normalized_attributes * external_weights[:, None].T
    calculated_wsrf = qws_weighted_attributes.sum(axis=1)
    return (calculated_wsrf, qws_complete_numpy_array)


if __name__ == "__main__":
    weights = [0.20, 0.17, 0.18, 0.10, 0.10, 0.10, 0.00, 0.05, 0.10]
    file_path = os.path.join(paths.interim_data_dir, "qws1_interim.csv")
    compute_wsrf(file_path, weights)
