from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:

        print("1. Starting pipeline")

        trainingpipelineconfig = TrainingPipelineConfig()

        print("2. TrainingPipelineConfig created")

        dataingestionconfig = DataIngestionConfig(
            training_pipeline_config=trainingpipelineconfig
        )

        print("3. DataIngestionConfig created")

        data_ingestion = DataIngestion(
            data_ingestion_config=dataingestionconfig
        )

        print("4. DataIngestion object created")

        logging.info("Initiate the data ingestion")

        print("5. Starting data ingestion")

        dataingestionartifact = data_ingestion.initiate_data_ingestion()

        print("6. Data ingestion completed")

        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)


'''if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion=DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate the data ingestion")
        
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)'''
