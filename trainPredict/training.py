import numpy as np 
import pandas as pd
import os, sys
from sklearn.metrics import classification_report 
import seaborn as sn; sn.set (font_scale=1.4) 
from sklearn.utils import shuffle 
import matplotlib.pyplot as plt
import cv2 
import tensorflow as tf
from tqdm import tqdm
import random
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from keras.preprocessing import image
from levelOutputs import root
# default is intels image database for mountains streets glacier buildings sea forest
class train_model():
    def __init__(self, class_names=['mountain', 'street', 'glacier', 'buildings', 'sea', 'forest'], data_training_path=r"./trainingData/dataset/", data_category=["seg_train", "seg_test"], IMAGE_SIZE=(150,150)):
        self.class_names = class_names
        self.data_training_path = data_training_path
        self.data_category = data_category
        self.IMAGE_SIZE = IMAGE_SIZE
    def load_data(self):
        class_names_label = {class_name:i for i, class_name in enumerate(self.class_names)}
        DIRECTORY = self.data_training_path
        CATEGORY = self.data_category
        output = []
        if not os.path.exists(DIRECTORY):
            root.critical("No database detected")
            sys.exit()

        for category in CATEGORY:
            path = os.path.join(DIRECTORY, category)
            images = []
            labels = []
            root.info("Loading {}".format(category))

            for folder in os.listdir(path):
                label = class_names_label[folder]

                for file in os.listdir(os.path.join(path, folder)):
                    img_path = os.path.join(os.path.join(path, folder), file)
                    image = cv2.imread(img_path)
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    image = cv2.resize(image, self.IMAGE_SIZE)
                    images.append(image)
                    labels.append(label)
            images = np.array(images, dtype = 'float32')
            labels = np.array(labels, dtype = 'int32')
            output.append((images,labels))
        return output 
    def train_data(self):
        model_path = './trainPredict/model/model.keras'
        if os.path.exists(model_path):
            # Load the model
            root.info("Model loaded")
            model = load_model(model_path)
        else:
            K.clear_session()
            (train_images, train_labels), (test_images, test_labels) = self.load_data()

            train_images, train_labels = shuffle(train_images, train_labels, random_state=25)
            model = tf.keras.Sequential([
                tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (150, 150, 3)),
                tf.keras.layers.MaxPooling2D(2,2),
                tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu'),
                tf.keras.layers.MaxPooling2D(2,2),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(128, activation=tf.nn.relu),
                tf.keras.layers.Dense(6, activation=tf.nn.softmax)
            ])
            model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
            history = model.fit(train_images, train_labels, batch_size=128, epochs=6, validation_split = 0.2)
            model.save(model_path)
        return model



