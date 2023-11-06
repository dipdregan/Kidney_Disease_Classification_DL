from CNN_Classifier.entity.Configuration_entity import RootConfig, ImageDataValidationConfig
from CNN_Classifier.entity.Artifact_entity import DataIngestionArtifact, ImageDataValidationArtifact
from CNN_Classifier.exception import CNN_Classifier
from CNN_Classifier.logging import logging
from CNN_Classifier.utils.util import write_yaml, list_subfolders
import cv2
import os, sys

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
            logging.info(f"Validating the extensions..")
            valid_extensions = self.data_validation_config.image_data_foramts #['.jpg', '.jpeg', '.png'],
            file_extension = os.path.splitext(image_file_path)[1].lower()#.jpg
            if file_extension in ['.jpg', '.jpeg', '.png']:
                return True
            else:
                os.remove(image_file_path)
                return False
        except Exception as e:
            raise CNN_Classifier(e, sys)

    def is_corrupt_image(self, image_file_path):
        try:
            logging.info(f"Validating the currepted images....")
            img = cv2.imread(image_file_path)
            if img is None:
                os.remove(image_file_path)
                return True
        except Exception as e:
            os.remove(image_file_path)
            return True
        return False

    def validate_image_class(self)->bool :
        try:
            logging.info("Validating image Classes....")
            classes_path = list_subfolders(self.data_ingetion_artifact.unzip_data_file_path)
            class_name = [os.path.basename(i) for i in classes_path]

            expected_classes = self.data_validation_config.image_class_label##['cyst', 'normal', 'stone', 'cancer']
            return expected_classes == class_name
        except Exception as e:
            raise CNN_Classifier(e, sys)

    def initiate_validation(self)->ImageDataValidationArtifact:
        try:
            validation_status = True  # Assume validation is successful
            validation_report = {"valid_images": [], "invalid_images": []}
            root_folder = self.data_ingetion_artifact.unzip_data_file_path
            subfolders = list_subfolders(root_folder)
            
            for subfolder_path in subfolders:
                files = os.listdir(subfolder_path)
                for image_file in files:
                    image_path = os.path.join(subfolder_path, image_file)

                    ### LET's Validate image extension
                    if not self.validate_image_extension(image_path):
                        validation_status = False
                        validation_report["invalid_images"].append({"path": image_path, "reason": "Invalid extension"})

                    # Let's Check for corrupt images
                    if self.is_corrupt_image(image_path):
                        validation_status = False
                        validation_report["invalid_images"].append({"path": image_path, "reason": "Corrupt image"})
                        
                        # ## nOW I AM Move corrupted images to the corrupted_image_filepath folder
                        image_filename = os.path.basename(image_path)
                        destination_path = os.path.join(self.data_validation_config.currepted_image_filepath, image_filename)
                        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                        os.rename(image_path, destination_path)

                    # AddING valid images to the report
                    validation_report["valid_images"].append({"path": image_path,"reason":"valid"})

            # Checking for valid image classes
            if not self.validate_image_class(): #['cyst', 'normal', 'stone', 'cancer']
                validation_status = False
                validation_report["invalid_images"].append({"reason": "Invalid image class"})

            # Save the validation report to a YAML file
            validation_report_path = os.path.join(self.data_validation_config.validation_report_path, self.data_validation_config.validation_report)
            os.makedirs(validation_report_path, exist_ok=True)
            write_yaml(validation_report_path, validation_report)

            # Move valid images to the valid_image_filepath folder
            valid_images = [img_info["path"] for img_info in validation_report["valid_images"]]
            for image_path in valid_images:
                image_filename = os.path.basename(image_path)
                folder_name = image_filename.split("-")[0]
                destination_path = os.path.join(self.data_validation_config.valid_image_filepath, folder_name,image_filename)
                os.makedirs(destination_path, exist_ok=True)
                os.rename(image_path, destination_path)

            image_data_validation_artifact = ImageDataValidationArtifact(
                Image_data_validation_path=self.data_validation_config.valid_image_filepath,
                validation_status=validation_status
            )

            return image_data_validation_artifact
        except Exception as e:
            raise CNN_Classifier(e, sys)
        


