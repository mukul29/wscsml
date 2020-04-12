import os.path
import re
import paths


def preprocess_raw_data(qws_raw_file, qws_interim_file):
    """
    This function takes the raw dataset file and removes blank lines and comments and storing it as interim an dataset
    :param qws_raw_file: file object(class '_io.TextIOWrapper' for the raw file
    :param qws_interim_file: file object(class '_io.TextIOWrapper' for the interim file
    :return: None
    """
    # regex for blank lines or lines beginning with a "#"
    regex_filter = re.compile(r'(^\s*$)|(^#)')

    # read all lines and store them in a list
    qws1_raw_list = qws_raw_file.readlines()

    # filter the data and write it in the interim file
    filtered_data = filter(lambda i: not regex_filter.search(i), qws1_raw_list)
    qws_interim_file.writelines(filtered_data)

    qws_raw_file.close()
    qws_interim_file.close()


if __name__ == "__main__":
    # open both files for qws1 dataset (raw for reading and interim for writing
    qws1_raw_file = open(os.path.join(paths.RAW_DATA_DIR, "qws1.txt"), "r")
    qws1_interim_file = open(os.path.join(paths.INTERIM_DATA_DIR, "qws1_interim.csv"), "w")
    preprocess_raw_data(qws1_raw_file, qws1_interim_file)
    # close both files
    qws1_raw_file.close()
    qws1_interim_file.close()

    # open both files for qws2 dataset (raw for reading and interim for writing
    qws2_raw_file = open(os.path.join(paths.RAW_DATA_DIR, "qws2.txt"), "r")
    qws2_interim_file = open(os.path.join(paths.INTERIM_DATA_DIR, "qws2_interim.csv"), "w")
    preprocess_raw_data(qws2_raw_file, qws2_interim_file)
    # close both files
    qws2_raw_file.close()
    qws2_interim_file.close()
