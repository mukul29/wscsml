import os.path

# Main project directory
project_dir = os.path.dirname(__file__)

# Raw data directory, data in this directory is treated as immutable
raw_data_dir = os.path.join(project_dir, 'data', 'raw')
# Interim data directory, blank lines are removed and the data is stored in the form of a csv file
interim_data_dir = os.path.join(project_dir, 'data', 'interim')
# Processed data directory, new qws values are used and new classes as well
processed_data_dir = os.path.join(project_dir, 'data', 'processed')
