import os
import subprocess
from CNN_Classifier.constant import Data_API
import os
import zipfile

def download_kaggle_dataset():

    dataset_name = Data_API
    output_dir = r"F:\End_To_End_project\Kidney_Disease_Classification_DL\Kidney_data"
    #kaggle datasets download -d nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone

    os.makedirs(output_dir, exist_ok=True)
    download_command = f"kaggle datasets download -d {dataset_name} -p {output_dir}"

    try:
        subprocess.run(download_command, shell=True, check=True)
        print("Dataset downloaded successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")



def unzip_files(zip_file_dir, unzip_file_dir):
    # List all ZIP files in the specified directory
    zip_files = [f for f in os.listdir(zip_file_dir) if f.endswith('.zip')]

    for zip_file in zip_files:
        zip_file_path = os.path.join(zip_file_dir, zip_file)

        # Create a directory with the same name as the ZIP file (without the .zip extension)
        unzip_dir = os.path.splitext(zip_file)[0]
        unzip_dir_path = os.path.join(unzip_file_dir, unzip_dir)
        os.makedirs(unzip_dir_path, exist_ok=True)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir_path)
            print(f"Extracted {zip_file} successfully to {unzip_dir_path}")

# Example usage:
zip_file_dir = r"F:\End_To_End_project\Kidney_Disease_Classification_DL\data"  # Directory containing ZIP files
unzip_file_dir = r"F:\End_To_End_project\Kidney_Disease_Classification_DL\data\extracted_data"  # Directory to extract files
unzip_files(zip_file_dir, unzip_file_dir)

