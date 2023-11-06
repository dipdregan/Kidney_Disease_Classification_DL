from CNN_Classifier.pipeline.Data_pipeline import TRAINING_PIPELINE
from CNN_Classifier.components.Data_Pipline.data_ingestion import DataIngestion
from CNN_Classifier.entity.Configuration_entity import RootConfig,DataIngetionConfig,ImageDataValidationConfig,DataTransformImageConfig
from CNN_Classifier.logging import logging
from CNN_Classifier.pipeline.Data_pipeline import TRAINING_PIPELINE

if __name__ == "__main__":
    config = RootConfig()
    # print(config.__dict__)
    data_ingetion_config = DataTransformImageConfig(config)
    print(data_ingetion_config.__dict__)
    logging.info(data_ingetion_config.__dict__)

# if __name__=="__main__":
#     pipe = TRAINING_PIPELINE()
#     pipe.run_pipeline()
 