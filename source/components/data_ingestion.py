import os
import sys
from source.exception import CustomException
from source.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from source.components.data_transformation import DataTransformation
from source.components.data_transformation import DataTransformationConfig

from source.components.train_model import ModelTrainerConfig
from source.components.train_model import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    '''This is the class constructor. When an object of DataIngestion is created, the __init__ method initializes 
    the ingestion_config attribute by creating an instance of the DataIngestionConfig class. '''
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        try:
            
            logging.info('Read the dataset as dataframe')
            df=pd.read_csv(r"D:\ML_Project\Notebook\Dataset\stud.csv")
            
            logging.info('Read the dataset as dataframe')

            #This line actually make sures that the file artifacts gets created...
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            # This pandas function writes the DataFrame df to a CSV file.

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            logging.error(f"Error during data ingestion: {str(e)}")
            raise CustomException(e,sys)
        

        
if __name__=="__main__":
    '''The line if __name__ == "__main__": in Python ensures that a block of code is only executed 
    when the script is run directly, and not when it's imported as a module in another script.'''
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_= data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))




