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
        self.resized_image_data_path = data_transformation_config.resized_image_data_path
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

    def resize_images(self, balance_image_data_path):
        try:
            logging.info(f"Now next Step is to start...>>>>>>>> ")
            logging.info(f"Resize Image function started...>>>>>>>> ")
            image_size = IMAGE_SIZE
            channels = IMAGE_CHANNEL

            logging.info(f"Images are resizing to {image_size}x{image_size} format with {channels} channels.")

            for label_name in os.listdir(balance_image_data_path):
                label_dir = os.path.join(balance_image_data_path, label_name)
                for image_file in os.listdir(label_dir):
                    image_path = os.path.join(label_dir, image_file)
                    image = cv2.imread(image_path)
                    
                    # Ensure the image has the specified number of channels
                    if image.shape[-1] != channels:
                        logging.warning(f"Image {image_path} has {image.shape[-1]} channels. Converting to {channels} channels.")
                        if channels == 1:
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        elif channels == 3:
                            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    
                    image = cv2.resize(image, (image_size, image_size))

                    output_path = os.path.join(self.resized_image_data_path, label_name, image_file)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    cv2.imwrite(output_path, image)

            logging.info(f"Images resized and saved in {self.resized_image_data_path}")
            return self.resized_image_data_path
        except Exception as e:
            logging.error(f"There is some problem during image resizing: {e}")
            raise CNN_Classifier(e, sys)


    def normalize_images(self,resized_image_data_path):
        try:
            logging.info(f"Now Starting the Normalization.....>>>>>>")
            image_data = []
            label_data = []

            for label_name in os.listdir(resized_image_data_path):
                label_dir = os.path.join(resized_image_data_path, label_name)
                for image_file in os.listdir(label_dir):
                    image_path = os.path.join(label_dir, image_file)
                    image = cv2.imread(image_path)
                    image = image / 255.0

                    image_data.append(image)
                    label_data.append(label_name)
                    cv2.imwrite(image_path, (image * 255).astype(np.uint8))

            image_data = np.array(image_data)
            label_data = np.array(label_data)
            os.makedirs(self.trasform_image_and_label_path, exist_ok= True)
            
            np.save(os.path.join(self.trasform_image_and_label_path, 'image_data.npy'), image_data)
            np.save(os.path.join(self.trasform_image_and_label_path, 'label_data.npy'), label_data)
            logging.info(f"Storing the normalize image_data and label in this folder...:")
            logging.info(f"{self.trasform_image_and_label_path}")

            return image_data, label_data
        except Exception as e:
            logging.info(f"An Error occured during the  data Normilation...>")
            raise CNN_Classifier(e,sys)
        
    def initiate_data_transformation(self) -> ImageDataTransformationArtifact:
        try:
            balance_image_data_path = self.undersampling()
            resized_image_data_path = self.resize_images(balance_image_data_path)
            image_data, label_data = self.normalize_images(resized_image_data_path=resized_image_data_path)
    
            image_data_transformation = ImageDataTransformationArtifact(
                Balance_Data_Path=self.balance_image_data_path,
                Transform_Image_Lable_Path=self.trasform_image_and_label_path,
                Resized_Image_Data_Path=self.resized_image_data_path
            )
            return image_data_transformation

        except Exception as e:
            raise CNN_Classifier(e, sys)
        






