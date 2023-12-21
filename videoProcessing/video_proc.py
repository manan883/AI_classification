import cv2
import os
from levelOutputs import root
import sys
class video_capture():
    def __init__(self, vidPath):
        self.vidPath = vidPath

    def create_path(self):
        try:
            if not os.path.exists("./videoProcessing/data"):
                os.makedirs("./videoProcessing/data")
                root.info("directory ./videoProcessing/data created")
            else:
                root.warning("./videoProcessing/data path already exists")
        except OSError:
            root.critical("Error making directory: OSError")
            sys.exit()

    def read_video(self, predictingInstance):
        cam = cv2.VideoCapture(self.vidPath)
        currentFrame = 0
        while(True):
            ret,frame = cam.read()
            if ret:
                tempFrame = frame
                temp_file_path = f"./videoProcessing/data/temp_{currentFrame}.jpg"
                cv2.imwrite(temp_file_path, tempFrame)
                className = predictingInstance.predict(temp_file_path)
                name = f'./videoProcessing/data/{className}_{currentFrame}.jpg'
                root.info('Creating...' + name)
                cv2.imwrite(name, frame)
                os.remove(temp_file_path)
                currentFrame += 1
            else:
                break
        cam.release()
        cv2.destroyAllWindows()




