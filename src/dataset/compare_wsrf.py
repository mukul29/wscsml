import numpy as np
import os.path
import paths
import pandas as pd


def compare_wsrf():
    # TODO fix the value of calculated wsrf
    qws1_complete_dataframe = pd.read_csv(os.path.join(paths.interim_data_dir, "qws1_interim.csv"), header=None)
    qws1_complete_numpy_array = qws1_complete_dataframe.to_numpy()
    qws1_attributes_numpy_array = qws1_complete_numpy_array[:, 0:9]

    qws1_normalized_maximum = qws1_attributes_numpy_array.max(axis=0)
    qws1_normalized_attributes = qws1_attributes_numpy_array / qws1_normalized_maximum[:, None].T

    external_weights = np.array([0.175911, 0.162317, 0.263999, 0.115322, 0.285133, 0.073854, -0.08905, -0.19998, 0.204159])
    qws1_weighted_attributes = qws1_normalized_attributes * external_weights[:, None].T
    calculated_wsrf = qws1_weighted_attributes.sum(axis=1)


if __name__ == "__main__":
    compare_wsrf()
