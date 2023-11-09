from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionArtifact:
    unzip_data_file_path:Path

@dataclass
class ImageDataValidationArtifact:
    Image_data_validation_path:Path
    validation_status: bool

@dataclass
class ImageDataTransformationArtifact:
    Balance_Data_Path: Path
    Transform_Image_Lable_Path :Path
    Preprocess_Pickle_Path: Path
    