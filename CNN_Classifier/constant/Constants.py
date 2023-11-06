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
IMAGE_SIZE:int = 227
IMAGE_CHANNEL:int = 3
VALID_IMAGE_ROOT_DIR: str = "Image_Data_Validation"
VALID_IMAGE_FILE_PATH: str = "Validated_image_data"
CURREPTED_IMAGE_FILE_PATH: str = "Correpted_image_data"
VALIDATION_REPORT: str = 'report.yaml'
VALIDATION_REPORT_FILE_PATH: str = "Data_Report"
VALID_IMAGE_FORMATS: List[str] = [".jpg", ".jpeg", ".png"]
VALID_IMAGE_LABELS: List[str] = ["cyst", "normal", "stone", "cancer"]

# Data Transformation Related Variable

TRANSFORM_IMAGE_DATA_ROOT_DIR = "Image_Data_transformation"
BALANCE_IMAGE_DATA_DIR:str = "Balanced_data"#["cyst", "normal", "stone", "cancer"]
TRANSFORM_IMAGE_DATA_DIR:str = "Transformed_data"
TRANSFORMED_IMAGE_DATA:str = "Data.ny"
TRANSFORMED_LABELS_DATA:str = "Label.ny"
PREPROCESS_DATA_IN_PIKEL_PATH:str = "Preprocess_data_pkl"
PREPROCESS_DATA_IN_PIKEL_FILE:str = "preprocess.pkl"

## Splited_Data related Constant
SPLIT_DATA_DIR:str ="Splited_Data"
X_TRAIN_FILE:str = "X_train.npy"
Y_TRAIN_FILE :str= "y_train.npy"
X_TEST_FILE :str = "X_test.npy"
Y_TEST_FILE :str = "y_test.npy"
X_VAL_FILE :str = "X_val.npy"
Y_VAL_FILE :str ="y_val.npy" 



