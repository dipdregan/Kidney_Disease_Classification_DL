from datetime import datetime
from CNN_Classifier.constant import Constants
import os 

class RootConfig:

    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = Constants.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(Constants.ARTIFACT_DIR,timestamp)
        self.timestamp: str = timestamp

class DataIngetionConfig:

    def __init__(self, root_dir: RootConfig):
        self.data_ingestion_dir: str = os.path.join(root_dir.artifact_dir, Constants.DATA_INGETION_DIR_NAME)

        self.kaggle_data_zip_file_path: str = os.path.join(self.data_ingestion_dir, Constants.DATA_INGETION_KAGGLE_DATA_STORE_DIR)

        self.unzip_file_path: str = os.path.join(self.data_ingestion_dir, Constants.DATA_INGETION_UNZIP_DATA_STORE_DIR)

        self.data_api :str = Constants.Data_API

        self.zip_file_name_path: str = os.path.join(self.kaggle_data_zip_file_path,Constants.Zip_File_Name) 


class ImageDataValidationConfig:
    def __init__(self,root_dir:RootConfig):

        self.image_data_foramts = Constants.VALID_IMAGE_FORMATS
        
        self.image_class_label = Constants.VALID_IMAGE_LABELS

        self.validation_report = Constants.VALIDATION_REPORT

        self.image_size = Constants.IMAGE_SIZE

        self.image_channel = Constants.IMAGE_CHANNEL

        self.validating_image_filepath = os.path.join(root_dir.artifact_dir,
                                                      Constants.VALID_IMAGE_ROOT_DIR)

        self.currepted_image_filepath = os.path.join(self.validating_image_filepath,
                                                     Constants.CURREPTED_IMAGE_FILE_PATH)     
        
        self.validation_report_path = os.path.join(root_dir.artifact_dir,
                                                   Constants.VALIDATION_REPORT_FILE_PATH )
        

class DataTransformImageConfig:
    def __init__(self, root_dir: RootConfig):
        self.image_size = Constants.IMAGE_SIZE
        self.color_mode = Constants.IMAGE_CHANNEL

        self.main_data_transform_dir = os.path.join(root_dir.artifact_dir,
                                                    Constants.TRANSFORM_IMAGE_DATA_ROOT_DIR)
        
        self.balance_image_data_path = os.path.join(self.main_data_transform_dir, 
                                                    Constants.BALANCE_IMAGE_DATA_DIR)
        
        self.resized_image_data_path = os.path.join(self.main_data_transform_dir, 
                                                    Constants.RESIZED_IMAGE_DATA_DIR)
        
        self.transform_image_data_path = os.path.join(self.main_data_transform_dir, 
                                                      Constants.TRANSFORM_IMAGE_DATA_DIR)
        
        self.transform_image_npy_data = os.path.join(self.transform_image_data_path, 
                                                     Constants.TRANSFORMED_IMAGE_DATA)
        
        self.transform_label_npy_data = os.path.join(self.transform_image_data_path, 
                                                     Constants.TRANSFORMED_LABELS_DATA)
        
        # self.preprocess_pickle_path = os.path.join(self.main_data_transform_dir, 
        #                                            Constants.PREPROCESS_DATA_IN_PIKEL_PATH)
    