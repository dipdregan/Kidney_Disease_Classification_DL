import os
import numpy as np
from sklearn.model_selection import train_test_split
from CNN_Classifier.entity.Artifact_entity import ImageDataTransformationArtifact
from CNN_Classifier.entity.Configuration_entity import RootConfig
from CNN_Classifier.constant.Constants import *
import mlflow
import mlflow.tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.metrics import SparseCategoricalAccuracy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import tensorflow as tf
from tensorflow.keras import layers, models
from keras.utils import to_categorical
from CNN_Classifier.logging import logging
from CNN_Classifier.utils.util import read_yaml



class ModelTrainer:
    def __init__(self, path):
        self.data_transformation_artifacts = path
        self.params = read_yaml(Path(os.path.join(os.getcwd(), 'params.yaml')))
        self.model = None  # Initialize the model attribute

    def split_data(self):
        test_size = self.params.TEST_SIZE
        random_state = self.params.RANDOM_STATE
        val_size = self.params.VAL_SIZE  # Make sure VAL_SIZE is defined in your constants

        image_data = np.load(os.path.join(self.data_transformation_artifacts, TRANSFORMED_IMAGE_DATA))
        labels = np.load(os.path.join(self.data_transformation_artifacts, TRANSFORMED_LABELS_DATA))

        X_train, X_temp, y_train, y_temp = train_test_split(image_data, labels, test_size=test_size, random_state=random_state)
        X_test, X_val, y_test, y_val = train_test_split(X_temp, y_temp, test_size=val_size, random_state=random_state)

        y_train = to_categorical(y_train, num_classes=4)
        y_val = to_categorical(y_val, num_classes=4)
        y_test = to_categorical(y_test, num_classes=4)

        return X_train, y_train, X_test, y_test, X_val, y_val

    def CNN_arch(self):
        try:
            model = models.Sequential([
                # Convolutional layers
                layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.params.IMAGE_SIZE),
                layers.MaxPooling2D((2, 2)),
                layers.Conv2D(64, (3, 3), activation='relu'),
                layers.MaxPooling2D((2, 2)),
                layers.Conv2D(128, (3, 3), activation='relu'),
                layers.MaxPooling2D((2, 2)),
                # Flatten the feature maps
                layers.Flatten(),
                # Fully connected layers
                layers.Dense(128, activation='relu'),
                layers.Dropout(0.5),
                layers.Dense(self.params.CLASSES, activation='softmax')
            ])

            model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])

            print(model.summary())

            self.model = model  # Save the model to the instance variable

            return model

        except Exception as e:
            raise e

    def train_model_with_callbacks(self, X_train, y_train, X_val, y_val):
        if self.model is None:
            raise ValueError("Model not initialized. Call CNN_arch() first.")

        early_stopping = EarlyStopping(
            monitor=self.params.MONITORING,        # it will Monitor validation loss
            patience=self.params.PATIENCE,               # Number of epochs with no improvement before stopping
            restore_best_weights=True  # Restore the model weights to the best epoch
        )

        checkpoint = ModelCheckpoint(
            self.params.MODEL_NAME,  # File to save the best model
            monitor=self.params.MONITOR,  # Monitor validation accuracy
            save_best_only=self.params.RESTORE_BEST_WEIGHT,     # Save only the best model
            mode=self.params.MODE,             # Save the model when accuracy is maximized
            verbose=1
        )

        history = self.model.fit(
            X_train,
            y_train,
            epochs=self.params.EPOCHS,
            validation_data=(X_val, y_val),
            callbacks=[early_stopping, checkpoint]
        )

