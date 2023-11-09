from CNN_Classifier.entity.Configuration_entity import RootConfig, ImageDataValidationConfig
from CNN_Classifier.entity.Artifact_entity import DataIngestionArtifact, ImageDataValidationArtifact
from CNN_Classifier.exception import CNN_Classifier
from CNN_Classifier.logging import logging
from CNN_Classifier.utils.util import write_yaml, list_subfolders, get_size_image
import cv2
import os, sys
import shutil
from pathlib import Path

class IMAGE_Data_VALIDATION:
    def __init__(self, data_ingetion_artifact: DataIngestionArtifact,
                 data_validation_config: ImageDataValidationConfig):
        try:
            self.data_ingetion_artifact = data_ingetion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise CNN_Classifier(e, sys)


    def validate_image_extension(self, image_file_path):
        try:
            
            valid_extensions = self.data_validation_config.image_data_foramts
            file_extension = os.path.splitext(image_file_path)[1].lower()
            if file_extension in valid_extensions:
                return True
            else:
                os.remove(image_file_path)  # Delete the file if it has an invalid extension
                logging.info(f"Extension Validaion Completed...>>>>>>>>>>>")
                return False
            # logging.info(f"Extension Validaion Completed...>>>>>>>>>>>")
        except FileNotFoundError:
            logging.error(f"File not found: {image_file_path}")
            return False
        except Exception as e:
            logging.error(f"Error while validating file extension: {e}")
            return False

    def is_corrupt_image(self, image_file_path):
        try:
            img = cv2.imread(image_file_path)
            if img is None:
                os.remove(image_file_path)  # Delete the corrupt image
                return True
        except FileNotFoundError:
            logging.error(f"File not found: {image_file_path}")
            return True
        except Exception as e:
            logging.error(f"Error while validating corrupted image: {e}")
            return True
        return False

    def validate_image_class(self):
        try:
            classes_path = list_subfolders(self.data_ingetion_artifact.unzip_data_file_path)
            class_name = [os.path.basename(i) for i in classes_path]
            expected_classes = self.data_validation_config.image_class_label

            return expected_classes == class_name

        except FileNotFoundError:
            logging.error("One or more directories not found.")
            return False
        except Exception as e:
            logging.error(f"Error while validating image classes: {e}")
            return False
        
    def initiate_validation(self) -> ImageDataValidationArtifact:
        try:
            logging.info(f"{10*'===='}")
            logging.info(f"{10*'=='} 'Start Data Validation'{10*'=='}")
            logging.info(f"{10*'===='}")

            validation_status = True  # Assume validation is successful
            validation_report = {"valid_images": [], "invalid_images": []}
            root_folder = self.data_ingetion_artifact.unzip_data_file_path
            subfolders = list_subfolders(root_folder)[0]

            for label in os.listdir(subfolders):
                label_path = os.path.join(subfolders, label)
                logging.info(f"Started  Validating the extensions...>>>>>>>>>>>>>>>")
                logging.info(f"Validating corrupted images...")
                for image_file in os.listdir(label_path):
                    image_path = os.path.join(label_path, image_file)

                    # Validate image extension and corrupted images
                    if not self.validate_image_extension(image_path) or self.is_corrupt_image(image_path):
                        validation_status = False
                        validation_report["invalid_images"].append({"path": image_path, "reason": "Invalid extension or corrupt image"})
                        label_corrupted_folder = os.path.join(self.data_validation_config.currepted_image_filepath, label)
                        os.makedirs(label_corrupted_folder, exist_ok=True)
                        shutil.move(image_path, os.path.join(label_corrupted_folder, os.path.basename(image_path)))
                        continue

                    # Move the validated image to the 'validated' folder under the label's name
                    label_valid_folder = os.path.join(self.data_validation_config.validating_image_filepath, label)
                    os.makedirs(label_valid_folder, exist_ok=True)
                    shutil.move(image_path, os.path.join(label_valid_folder, os.path.basename(image_path)))

                    # Add valid images to the report
                    validation_report["valid_images"].append({"path": image_path, "reason": "valid"})
                logging.info(f"Validating the extensions Completed...>>>>>>>>>>>>>>>")
                logging.info(f"Validating corrupted images Completed...>>>>>>>>>>>>>>>>")
            # Checking for valid image classes
            logging.info(f"validating Images Classes...........>>>>>>>>>")
            if not self.validate_image_class():
                validation_status = False
                validation_report["invalid_images"].append({"reason": "Invalid image class"})
            logging.info(f"Genrating the image Reports")
            # Save the validation report to a YAML file
            validation_report_path = os.path.join(
                self.data_validation_config.validation_report_path,
                self.data_validation_config.validation_report
            )
            os.makedirs(os.path.dirname(validation_report_path), exist_ok=True)
            write_yaml(validation_report_path, validation_report)

            image_data_validation_artifact = ImageDataValidationArtifact(
                Image_data_validation_path=self.data_validation_config.validating_image_filepath,
                validation_status=validation_status
            )
            logging.info(f"{10*'===='}")
            logging.info(f"{10*'=='}'Data Validation_Completed'{10*'=='}")
            logging.info(f"{10*'===='}")
            return image_data_validation_artifact
        except Exception as e:
            raise CNN_Classifier(e, sys)


















    # def validate_image_size(self,image_path):
    #     try:
    #         desired_size = self.data_validation_config.image_size
    #         desired_channels = self.data_validation_config.image_channel

    #         image = cv2.imread(image_path)
    #         if image is not None:
    #             height, width, channels = image.shape
    #             if height == desired_size and width == desired_size and channels == desired_channels:
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return False
    #     except Exception as e:
    #         logging.error(f"Error while validating image size: {e}")
    #         return False