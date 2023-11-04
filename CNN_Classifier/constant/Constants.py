from typing import List

ARTIFACT_DIR: str = "artifact"
PIPELINE_NAME: str = "Kidney_Disease_Classification_DL"

# Data Ingestion Related Constants
Data_API: str = "nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone"
DATA_INGETION_DIR_NAME: str = "Image_data_ingetion"
DATA_INGETION_KAGGLE_DATA_STORE_DIR: str = "Kaggel_data_Zip_formate"
DATA_INGETION_UNZIP_DATA_STORE_DIR: str = "Unzip_data"

# Data Validation Related Constants
VALID_IMAGE_FILE_PATH: str = "Validated_image_data"
CURREPTED_IMAGE_FILE_PATH: str = "Correpted_image_data"
VALIDATION_REPORT: str = 'report.yaml'
VALIDATION_REPORT_FILE_PATH: str = "Validation_Report"
VALID_IMAGE_FORMATS: List[str] = [".jpg", ".jpeg", ".png"]
VALID_IMAGE_LABELS: List[str] = ["cyst", "normal", "stone", "cancer"]


