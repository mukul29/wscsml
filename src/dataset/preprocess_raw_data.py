import os.path
import re
import paths


def preprocess_raw_data():
    ################################# FOR QWS1 #########################################

    # open both files for qws1 dataset (raw for reading and interim for writing
    qws1_raw_file = open(os.path.join(paths.raw_data_dir, "qws1.txt"), "r")
    qws1_interim_file = open(os.path.join(paths.interim_data_dir, "qws1_interim.csv"), "w")

    # regex for blank lines or lines beginning with a "#"
    regex_filter = re.compile(r'(^\s*$)|(^#)')

    # read all lines and store them in a list
    qws1_raw_list = qws1_raw_file.readlines()

    # filter the data and write it in the interim file
    filtered_data = filter(lambda i: not regex_filter.search(i), qws1_raw_list)
    qws1_interim_file.writelines(filtered_data)

    # close both files
    qws1_raw_file.close()
    qws1_interim_file.close()
    #####################################################################################

    ################################## FOR QWS2 #########################################
    # open both files for qws2 dataset
    qws2_raw_file = open(os.path.join(paths.raw_data_dir, "qws2.txt"), "r")
    qws2_interim_file = open(os.path.join(paths.interim_data_dir, "qws2_interim.csv"), "w")

    # regex for blank lines or lines beginning with a "#"
    regex_filter = re.compile(r'(^\s*$)|(^#)')

    # read all lines and store them in a list
    qws2_raw_list = qws2_raw_file.readlines()

    # filter the data and write it in the interim file
    filtered_data = filter(lambda i: not regex_filter.search(i), qws2_raw_list)
    qws2_interim_file.writelines(filtered_data)

    # close both files
    qws2_raw_file.close()
    qws2_interim_file.close()
    #####################################################################################


if __name__ == "__main__":
    preprocess_raw_data()
