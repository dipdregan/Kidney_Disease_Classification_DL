from CNN_Classifier.entity.Artifact_entity import ImageDataValidationArtifact,ImageDataTransformationArtifact
from CNN_Classifier.entity.Configuration_entity import DataTransformImageConfig
from CNN_Classifier.constant.Constants import *

from CNN_Classifier.logging import logging
from CNN_Classifier.exception import CNN_Classifier
import os, sys

import shutil
import random
import cv2
import pickle

from PIL import Image
import numpy as np
from pathlib import Path

class DataTransformation:
    def __init__(self, data_transformation_config:DataTransformImageConfig,
                 data_validaiton_artifacts:ImageDataValidationArtifact):
        
        self.data_transformation_config = data_transformation_config
        self.data_validation_artifact = data_validaiton_artifacts.Image_data_validation_path
        # self.data_validation_artifact = data_validaiton_artifacts

        self.balance_image_data_path = data_transformation_config.balance_image_data_path
        
        self.trasform_image_and_label_path = data_transformation_config.transform_image_data_path
        

    def undersampling(self)->Path:
        try:
            logging.info(f"Starting the UnderSampling process.........>>>>>>>>")
            os.makedirs(self.balance_image_data_path, exist_ok=True)
            class_directories = os.listdir(self.data_validation_artifact)

            class_counts = {}
            for label_name in class_directories:
                label_dir = os.path.join(self.data_validation_artifact, label_name)
                class_counts[label_name] = len(os.listdir(label_dir))

            min_count = min(class_counts.values())
            for label_name, images_count in class_counts.items():
                images_path = os.path.join(self.data_validation_artifact, label_name)
                image_files = os.listdir(images_path)
                
                logging.info(f"Selecting a random sample of :{min_count} images")
                select_images = random.sample(image_files, min_count)

                logging.info(f"Creating a new folder for the selected images if not Exits")
                output_dir = os.path.join(self.balance_image_data_path, label_name)
                os.makedirs(output_dir, exist_ok=True)

                logging.info(f"Copy the selected images to the new folder {output_dir}")
                for image_file in select_images:
                    source_path = os.path.join(images_path, image_file)
                    destination_path = os.path.join(output_dir, image_file)
                    shutil.copy2(source_path, destination_path)
            return self.balance_image_data_path
        
        except Exception as e:
            logging.error(f"An error occurred during Uunder sampling :{e}")
            raise CNN_Classifier(e,sys)

    def image_preprocessing(self,balanced_dataset_dir):
        try:
            logging.info(f"Now Starting the Normalization.....>>>>>>")
            
            images = [] 
            labels = []

            # List all class directories in the balanced dataset
            class_directories = os.listdir(balanced_dataset_dir)

            # Assign numerical labels to each class
            class_to_label = {class_name: i for i, class_name in enumerate(class_directories)}

            for class_dir in class_directories:
                class_path = os.path.join(balanced_dataset_dir, class_dir)
                image_files = os.listdir(class_path)
                class_label = class_to_label[class_dir]

                for image_file in image_files:
                    image_path = os.path.join(class_path, image_file)

                    # Resizing and scaling the image using PIL
                    with Image.open(image_path) as img:
                        img = img.resize((IMAGE_SIZE,IMAGE_SIZE), Image.ANTIALIAS)
                        img = img.convert(IMAGE_CHANNEL)  #'RGB' for color and 'L' for gray
                        img_array = np.array(img) / 255.0 

                    images.append(img_array)
                    labels.append(class_label)

            # Convert the lists to NumPy arrays
            image_data = np.array(images)
            label_data = np.array(labels)
            os.makedirs(self.trasform_image_and_label_path, exist_ok= True)
            
            np.save(os.path.join(self.trasform_image_and_label_path,TRANSFORMED_IMAGE_DATA), image_data)
            np.save(os.path.join(self.trasform_image_and_label_path, TRANSFORMED_LABELS_DATA), label_data)
            logging.info(f"Storing the normalize image_data and label in this folder...:")
            logging.info(f"{self.trasform_image_and_label_path}")

            return images, labels
        except Exception as e:
            logging.info(f"An Error occured during the  data Normilation...>")
            raise CNN_Classifier(e,sys)
        
    def initiate_data_transformation(self) -> ImageDataTransformationArtifact:
        try:
            balance_image_data_path = self.undersampling()
            self.image_preprocessing(balanced_dataset_dir=balance_image_data_path)
    
            image_data_transformation = ImageDataTransformationArtifact(
                Balance_Data_Path=self.balance_image_data_path,
                Transform_Image_Lable_Path=self.trasform_image_and_label_path,    
            )
            return image_data_transformation

        except Exception as e:
            raise CNN_Classifier(e, sys)
        






