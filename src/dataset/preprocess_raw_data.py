import os
import re

# Main project directory
project_dir = os.path.abspath('../..')

# Raw data directory, data in this directory is treated as immutable
raw_data_dir = os.path.join(project_dir, 'data', 'raw')

# Processed data directory, blank lines are removed and the data is stored in the form of a csv file
interim_data_dir = os.path.join(project_dir, 'data', 'interim')

################################## FOR QWS1 #########################################

# open both files for qws1 dataset (raw for reading and interim for writing
qws1_raw_file = open(os.path.join(raw_data_dir, "qws1.txt"), "r")
qws1_interim_file = open(os.path.join(interim_data_dir, "qws1_interim.csv"), "w")

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
qws2_raw_file = open(os.path.join(raw_data_dir, "qws2.txt"), "r")
qws2_interim_file = open(os.path.join(interim_data_dir, "qws2_interim.csv"), "w")

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
