import training
from levelOutputs import root
from keras.preprocessing import image
import numpy as np
t1 = training.train_model()
model = t1.train_data()

class predict_data():
    def predict(self, imgpath: str, image_size=(150,150)):
        img = image.load_img(imgpath, target_size=image_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        return t1.class_names[predicted_class[0]]
