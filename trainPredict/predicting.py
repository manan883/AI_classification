import training
from levelOutputs import root

t1 = training.train_model()
t1.load_data()
t1.train_data()

class predict_data():
    def __init(self, img):
        self.img = img
