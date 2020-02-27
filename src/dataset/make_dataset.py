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
    # qws_complete_numpy_array_temp = np.append(qws_complete_numpy_array, qws_wsrf[:, np.newaxis], axis=1)
    qws_wsrf_level = np.array([])
    for score in qws_wsrf:
        if(score > 0.8):
            level = 1
        elif(score > 0.7):
            level = 2
        elif(score > 0.6):
            level = 3
        else:
            level = 4
        score = np.append(score, level)
        qws_wsrf_level = np.append(qws_wsrf_level, score)
    qws_wsrf_level = qws_wsrf_level.reshape(qws_wsrf.shape[0], 2)
    print(qws_wsrf_level)






if __name__ == "__main__":
    weights = [0.20, 0.17, 0.18, 0.10, 0.10, 0.10, 0.00, 0.05, 0.10]
    interim_file_path = os.path.join(paths.interim_data_dir, "qws2_interim.csv")
    processed_file_path = os.path.join(paths.interim_data_dir, "qws2_processed.csv")
    make_dataset(interim_file_path, processed_file_path, weights)
