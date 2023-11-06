from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    unzip_data_file_path:str

@dataclass
class ImageDataValidationArtifact:
    Image_data_validation_path:str
    validation_status: bool

@dataclass
class ImageDataTransformationArtifact:
    Balance_Data_Path: str
    Transform_Image_Lable_Path :str
    Splited_data: str
    