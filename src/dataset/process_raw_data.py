import os
import re

# Main project directory
project_dir = os.path.abspath('../..')

# Raw data directory, data in this directory is treated as immutable
raw_data_dir = os.path.join(project_dir, 'data', 'raw')

# Processed data directory, blank lines are removed and the data is stored in the form of a csv file
processed_data_dir = os.path.join(project_dir, 'data', 'processed')

################################## FOR QWS1 #########################################

# open both files for qws1 dataset
qws1_raw_file = open(os.path.join(raw_data_dir, "qws1.txt"), "r")
qws1_processed_file = open(os.path.join(processed_data_dir, "qws1_processed.csv"), "w")

# regex for blank lines or lines beginning with a "#"
regex_filter = re.compile(r'(^\s*$)|(^#)')

# read all lines and store them in a list
qws1_raw_list = qws1_raw_file.readlines()

# filter the data and write it in the processed file
filtered_data = filter(lambda i: not regex_filter.search(i), qws1_raw_list)
qws1_processed_file.writelines(filtered_data)

# close both files
qws1_raw_file.close()
qws1_processed_file.close()
#####################################################################################

################################## FOR QWS2 #########################################


#####################################################################################
