from CNN_Classifier.logging import logging
from CNN_Classifier.exception import CNN_Classifier
import os, sys

from CNN_Classifier.entity.Artifact_entity import ImageDataValidationArtifact,ImageDataTransformationArtifact
from CNN_Classifier.entity.Configuration_entity import RootConfig,DataTransformImageConfig

class DataTranformation:
    def __init__(self,Image_data_val_artifact: ImageDataValidationArtifact,
                 data_transformation_config: DataTransformImageConfig):
        self.image_data_val_artifact = Image_data_val_artifact
        self.data_transformation_config =data_transformation_config

    def ImageDataBalance(self,):
        pass

    def ImageResize(self):
        pass

    def DataSplitting(self):
        pass

    def InitiateDataTranformation(self,Image_data_val_artifact):
        try:
            pass
        except Exception as e:
            raise e
         
