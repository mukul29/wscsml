import paths
import os.path
import compute_wsrf
import numpy as np
import pandas as pd


def make_dataset(interim_file_path, processed_file_path, weights, version):
    """
    This function is used to make the final dataset to be used, computes and adds the new WsRF and service classification
    :param interim_file_path: str
        string containing the path of the interim file
    :param processed_file_path: str
        string containing the path of the processed file to be stored
    :param weights:
        floating point numbers representing weights of each attribute which add up to 1.0
    :param: version:
        integer (1 or 2) for qws version 1 or 2 respectively
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
    if(version == 1):
        qws_complete_numpy_array[:, 9:11] = qws_wsrf_level
    elif(version == 2):
        qws_complete_numpy_array = np.hstack((qws_complete_numpy_array, np.zeros((qws_wsrf.shape[0], 2))))
        qws_complete_numpy_array[:, 11:13] = qws_complete_numpy_array[:, 9:11]
        qws_complete_numpy_array[:, 9:11] = qws_wsrf_level
    else:
        print("Version has to be either 1 or 2")

    qws_complete_dataframe_new = pd.DataFrame(qws_complete_numpy_array)
    qws_complete_dataframe_new = qws_complete_dataframe_new.astype({10: int})
    qws_complete_dataframe_new.to_csv(processed_file_path, header=False, index=False)


if __name__ == "__main__":
    weights = [0.20, 0.17, 0.11, 0.08, 0.10, 0.13, 0.00, 0.11, 0.10]

    print(np.sum(weights))

    interim_file_path = os.path.join(paths.interim_data_dir, "qws1_interim.csv")
    processed_file_path = os.path.join(paths.processed_data_dir, "qws1_processed.csv")
    make_dataset(interim_file_path, processed_file_path, weights, 1)

    # weights = [0.20, 0.17, 0.18, 0.10, 0.10, 0.10, 0.00, 0.05, 0.10]
    interim_file_path = os.path.join(paths.interim_data_dir, "qws2_interim.csv")
    processed_file_path = os.path.join(paths.processed_data_dir, "qws2_processed.csv")
    make_dataset(interim_file_path, processed_file_path, weights, 2)
