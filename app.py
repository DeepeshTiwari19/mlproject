# from src.mlproject import logger
# or
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ignestion import DataIngestion
from src.mlproject.components.data_ignestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.mlproject.components.model_trainer import ModelTrainerConfig,ModelTrainer

if __name__=='__main__':
    logging.info("The execution has started")

    try:
        # a=1/0
        # data_ignestion_config=DataIngestionConfig()
        data_ignestion=DataIngestion()
        train_data_path,test_data_path=data_ignestion.initiate_data_ingestion()

        # data_trandormation_config=DataTransformationConfig()
        data_trandormation=DataTransformation()
        train_arr,test_arr,_=data_trandormation.initiate_data_transormation(train_data_path,train_data_path)

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

