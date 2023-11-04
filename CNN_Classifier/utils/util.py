from pathlib import Path
from CNN_Classifier.exception import CNN_Classifier
from CNN_Classifier.logging import logging
import sys, os
from box import ConfigBox
import joblib
import base64
import yaml
import json
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(file_path: Path)-> ConfigBox:
    try:
        with open(file_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
        logging.info(f"yaml file: {file_path} lodded Successfully...")
        return  ConfigBox(content)
        
    except Exception as e:
        raise CNN_Classifier(e, sys) from e
    

def write_yaml(path_to_save,validation_report):
    try:
        with open(path_to_save, 'w') as report_file:
            yaml.dump(validation_report, report_file)

    except Exception as e:
        raise CNN_Classifier(e, sys)
    
def list_subfolders(root_folder):
    try:
        subfolder_paths = []
        subfolders = os.listdir(os.path.join(root_folder, os.listdir(root_folder)[0]))
        
        for subfolder in subfolders:
            subfolder_path = os.path.join(root_folder, os.listdir(root_folder)[0], subfolder)
            subfolder_paths.append(subfolder_path)
        
        return subfolder_paths
    except Exception as e:
        raise e


@ensure_annotations   
def save_json(path_to_save: Path, data: dict):
    try:
        with open(path_to_save, "w") as file:
            json.dump(data, file, indent= 4)
        logging.info(f"JSON file saved at : {path_to_save}")

    except Exception as e:
        raise CNN_Classifier(e, sys) from e
    

@ensure_annotations
def load_json(path_to_load: Path, data: dict):
    try:
        with open(path_to_load) as file:
            content = json.load(file)
        logging.info(f"JSON file loaded successfully from : {path_to_load}")
        logging.info(f"{content}")

    except Exception as e:
        raise CNN_Classifier(e, sys) from e

@ensure_annotations
def create_directories(path_to_directories: list, verbose =True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"Created Directory at :{path}")
    except Exception as e:
        raise CNN_Classifier(e, sys) from e
    
@ensure_annotations
def save_binary_file(data, path:Path):
    try:
        joblib.dump(value=data, filename={path})
        logging.info(f"binary file saved at path {path}")

    except Exception as e:
        raise CNN_Classifier(e, sys) from e
    
@ensure_annotations
def load_binary_file(path:Path):
    try:
        data = joblib.load(path)
        logging.info(f"Binary file loaded from path :{path}")
        logging.info(f"{data}")

    except Exception as e:
        raise CNN_Classifier(e, sys) from e 
    
@ensure_annotations
def get_size(path:Path):
    try:
        size_in_kb = round(os.path.getsize(path)/1024)
    except Exception as e:
        raise CNN_Classifier(e, sys)

@ensure_annotations
def decodeImage(imgstring, filename):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(filename, 'wb') as f:
            f.write(imgdata)
            f.close()
    except Exception as e:
        raise CNN_Classifier(e, sys) from e
    
@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())
    except Exception as e:
        raise CNN_Classifier(e, sys) from e
        

    

