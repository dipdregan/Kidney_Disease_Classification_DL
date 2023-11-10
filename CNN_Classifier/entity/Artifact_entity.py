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

@dataclass
class PreparebaseModelArtifact:
    Base_model_path: Path
    Updated_model_path : Path
    Pramas_image_size: list
    Pramas_learning_rate: float
    Pramas_include_top: bool 
    Pramas_weight: str
    Pramas_classes: int 
    