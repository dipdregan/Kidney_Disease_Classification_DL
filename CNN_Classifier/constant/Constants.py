from typing import List

ARTIFACT_DIR: str = "artifact"
PIPELINE_NAME: str = "Kidney_Disease_Classification_DL"

# Data Ingestion Related Constants
Data_API: str = "nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone"
Zip_File_Name: str = "ct-kidney-dataset-normal-cyst-tumor-and-stone.zip"
DATA_INGETION_DIR_NAME: str = "Image_data_ingetion"
DATA_INGETION_KAGGLE_DATA_STORE_DIR: str = "Kaggel_data_Zip_formate"
DATA_INGETION_UNZIP_DATA_STORE_DIR: str = "Unzip_data"


# Data Validation Related Constants

VALID_IMAGE_ROOT_DIR: str = "Image_Data_Validation"
VALID_IMAGE_FILE_PATH: str = "Validated_image_data"
CURREPTED_IMAGE_FILE_PATH: str = "Correpted_image_data"
VALIDATION_REPORT: str = 'report.yaml'
VALIDATION_REPORT_FILE_PATH: str = "Data_Report"
VALID_IMAGE_FORMATS: List[str] = [".jpg", ".jpeg", ".png"]
VALID_IMAGE_LABELS: List[str] = ["cyst", "normal", "stone", "cancer"]

# Data Transformation Related Variable
IMAGE_SIZE:int = 224
IMAGE_CHANNEL:int = 'RGB'#for color image 'RGB' 
TRANSFORM_IMAGE_DATA_ROOT_DIR = "Image_Data_transformation"
BALANCE_IMAGE_DATA_DIR:str = "Balanced_image_data"#["cyst", "normal", "stone", "cancer"]
TRANSFORM_IMAGE_DATA_DIR:str = "Transformed_data"
TRANSFORMED_IMAGE_DATA:str = "Image_Data.npy"
TRANSFORMED_LABELS_DATA:str = "Label_Data.npy"


### Base Model Realted Constants
PREPARE_BASE_MODEL_DIR:str = "Prepare_base_model"
PREPARE_BASE_MODEL_NAME:str = "base_model.h5"
UPDATED_BASE_MODEL_NAME: str = "updated_model.h5"



