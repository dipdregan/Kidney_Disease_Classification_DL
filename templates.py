import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(message)s')

project_name = "CNN_Classifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/Configuration_entity.py",
    f"{project_name}/entity/Artifact_entity.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/logging.py",
    f"{project_name}/exception.py"
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "research/testing.py",
    "setup.py",
    "model/.gitkeep",
    "templates/index.html",
    "init_setup.sh",
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")