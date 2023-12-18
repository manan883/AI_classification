import cv2
import os
from levelOutputs import root
import sys
class video_capture():
    def __init__(self, vidPath):
        self.vidPath = vidPath

    def create_path(self):
        try:
            if not os.path.exists("./data"):
                os.makedirs("./data")
                root.info("directory ./data created")
            else:
                root.warning("./data path already exists")
        except OSError:
            root.critical("Error making directory: OSError")
            sys.exit()

    def read_video(self):
        cam = cv2.VideoCapture(self.vidPath)
        currentFrame = 0
        while(True):
            ret,frame = cam.read()
            if ret:
                name = './data/frame' + str(currentFrame) + '.jpg'
                root.info('Creating...' + name) 
                cv2.imwrite(name, frame)
                currentFrame+=1 
            else:
                break
        cam.release()
        cv2.destroyAllWindows()




vc1 = video_capture("../externalData/test.mp4")
vc1.create_path()
vc1.read_video()
