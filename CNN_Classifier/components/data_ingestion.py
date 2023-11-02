from CNN_Classifier.entity.Artifact_entity import DataIngestionArtifact
from CNN_Classifier.entity.Configuration_entity import DataIngetionConfig

import subprocess
import zipfile

from CNN_Classifier.exception import CNN_Classifier
from CNN_Classifier.logging import logging
import os, sys

class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngetionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise CNN_Classifier(e,sys)
    
    def importing_data_from_kaggle(self):
        try:
            dataset_api = self.data_ingestion_config.data_api

            output_dir = self.data_ingestion_config.kaggle_data_zip_file_path
            os.makedirs(output_dir, exist_ok=True)

            download_command = f"kaggle datasets download -d {dataset_api} -p {output_dir}"
    
            try:
                subprocess.run(download_command, shell=True, check=True)
                print("Dataset downloaded successfully!")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
        except Exception as e:
            raise CNN_Classifier(e, sys)
        
    def unziping_the_data(self):
        try:
            zip_file_path = self.data_ingestion_config.kaggle_data_zip_file_path
    
            unzip_dir = self.data_ingestion_config.unzip_file_path
            os.makedirs(unzip_dir, exist_ok= True)

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
                print(f"Data successfully extracted to {unzip_dir}")
        except Exception as e:
            raise CNN_Classifier(e, sys)
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info(f"{30*'===='}")
            logging.info(f"{10*'=='}Data Ingestion Started...{10*'=='}")
            logging.info(f"{30*'===='}")
            
            logging.info(f"Data is Downloading from Kaggle...")
            logging.info(f"Storing the data in this folder :{self.data_ingestion_config.kaggle_data_zip_file_path}")
            self.importing_data_from_kaggle()
            
            logging.info(f" Unzipping the data into this folder :{self.data_ingestion_config.unzip_file_path}")
            self.unziping_the_data()

            logging.info(f"{30*'===='}")
            logging.info(f"{10*'=='}Data Ingestion Completed...{10*'=='}")
            logging.info(f"{30*'===='}")

            data_ingestion_artifact = DataIngestionArtifact(
                unzip_data_file_path=self.data_ingestion_config.unzip_file_path
            )

            return data_ingestion_artifact
        except Exception as e:
            raise CNN_Classifier(e, sys)