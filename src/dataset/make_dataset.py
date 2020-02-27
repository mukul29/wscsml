import paths
import os.path
import compute_wsrf
import numpy as np


def make_dataset(interim_file_path, processed_file_path, weights):
    """
    This function is used to make the final dataset to be used, computes and adds the new WsRF and service classification
    :param interim_file_path: str
        string containing the path of the interim file
    :param processed_file_path: str
        string containing the path of the processed file to be stored
    :param weights:
        floating point numbers representing weights of each attribute which add up to 1.0
    :return: None
    """
    qws_wsrf, qws_complete_numpy_array = compute_wsrf.compute_wsrf(interim_file_path, weights)
    # qws_complete_numpy_array_temp = np.append(qws_complete_numpy_array, qws_wsrf, axis=1)


if __name__ == "__main__":
    weights = [0.20, 0.17, 0.18, 0.10, 0.10, 0.10, 0.00, 0.05, 0.10]
    interim_file_path = os.path.join(paths.interim_data_dir, "qws1_interim.csv")
    processed_file_path = os.path.join(paths.interim_data_dir, "qws1_processed.csv")
    make_dataset(interim_file_path, processed_file_path, weights)
