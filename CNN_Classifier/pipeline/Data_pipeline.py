from CNN_Classifier.entity.Configuration_entity import DataIngetionConfig,RootConfig, ImageDataValidationConfig,DataTransformImageConfig
from CNN_Classifier.entity.Artifact_entity import DataIngestionArtifact, ImageDataValidationArtifact,ImageDataTransformationArtifact
from CNN_Classifier.components.Data_Pipline.data_ingestion import DataIngestion
## importing components
from CNN_Classifier.components.Data_Pipline.data_validation import IMAGE_Data_VALIDATION
from CNN_Classifier.components.Data_Pipline.data_transformation import DataTransformation

from CNN_Classifier.logging import logging
from CNN_Classifier.exception import CNN_Classifier

import sys, os

class TRAINING_PIPELINE:
    def __init__(self):
        try:
            self.root_dir = RootConfig()
            
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
    def start_data_validation(self,data_ingestion_artifact):
        try:
            data_validation_config = ImageDataValidationConfig(root_dir=self.root_dir)
            data_validation = IMAGE_Data_VALIDATION(data_ingetion_artifact=data_ingestion_artifact,
                                                    data_validation_config=data_validation_config)
            
            data_validation_artifact = data_validation.initiate_validation()
            return data_validation_artifact
        
        except Exception as e:
            raise CNN_Classifier(e,sys)
        
    def start_data_transformation(self,data_validation_artifacts):
        try:
            data_transformation_config = DataTransformImageConfig(root_dir=self.root_dir)
            data_transformation = DataTransformation(data_transformation_config=data_transformation_config,
                                                     data_validaiton_artifacts=data_validation_artifacts)
            
            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            return data_transformation_artifacts
        
        except Exception as e:
            raise CNN_Classifier(e, sys)
        
    def run_pipeline(self):
        try:
            # data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            # data_ingestion_artifact = r"F:\End_To_End_project\Kidney_Disease_Classification_DL\artifact\11_08_2023_13_11_57\Image_data_ingetion\Unzip_data"

            # data_validation_artifact:ImageDataValidationArtifact = self.start_data_validation(data_ingestion_artifact)
            data_validation_artifact = r"F:\End_To_End_project\Kidney_Disease_Classification_DL\artifact\11_08_2023_14_55_31\Image_Data_Validation"

            data_transformation_artifact:ImageDataTransformationArtifact = self.start_data_transformation(data_validation_artifact)
        
        except Exception as e:
            raise CNN_Classifier(e, sys)