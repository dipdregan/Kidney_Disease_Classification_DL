from CNN_Classifier.entity.Configuration_entity import DataIngetionConfig,RootConfig
from CNN_Classifier.entity.Artifact_entity import DataIngestionArtifact
from CNN_Classifier.components.data_ingestion import DataIngestion

from CNN_Classifier.logging import logging
from CNN_Classifier.exception import CNN_Classifier

import sys, os

class TRAINING_PIPELINE:
    def __init__(self, root_dir:RootConfig):
        try:
            self.root_dir = root_dir
        except Exception as e:
            raise CNN_Classifier(e, sys)
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngetionConfig(root_dir=self.root_dir)
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise CNN_Classifier(e, sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise CNN_Classifier(e, sys)