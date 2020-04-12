import os.path

# Main project directory
PROJECT_DIR = os.path.dirname(__file__)

# Raw data directory, data in this directory is treated as immutable
RAW_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'raw')
# Interim data directory, blank lines are removed and the data is stored in the form of a csv file
INTERIM_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'interim')
# Processed data directory, new qws values are used and new classes as well
PROCESSED_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'processed')
