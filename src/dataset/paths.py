import os.path

# Main project directory
here = os.path.dirname(__file__)
source_dir = os.path.dirname(here)
project_dir = os.path.abspath(os.path.join(source_dir, os.pardir))

# Raw data directory, data in this directory is treated as immutable
raw_data_dir = os.path.join(project_dir, 'data', 'raw')

# Processed data directory, blank lines are removed and the data is stored in the form of a csv file
interim_data_dir = os.path.join(project_dir, 'data', 'interim')
