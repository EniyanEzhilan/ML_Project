import os 
from source.logger import logging
from sklearn.model_selection import train_test_split

import pandas as pd

file_path = r"D:\ML_Project\Notebook\Dataset\stud.csv"

# Check if the file exists
if os.path.exists(file_path):
    logging.info(f"File found: {file_path}")
    df = pd.read_csv(file_path)
else:
    logging.error(f"File not found at {file_path}")
    raise FileNotFoundError(f"File not found at {file_path}")


logging.info(f"File found: {file_path}")
df = pd.read_csv(file_path)
logging.info(f"Dataset shape: {df.shape}")
logging.info(f"First few rows of dataset: {df.head()}")

logging.info("Train-test split initiated")
train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
logging.info(f"Train set shape: {train_set.shape}, Test set shape: {test_set.shape}")

logging.info(f"Saving training data to {self.ingestion_config.train_data_path}")
train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
logging.info("Training data saved successfully")

logging.info(f"Saving test data to {self.ingestion_config.test_data_path}")
test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
logging.info("Test data saved successfully")