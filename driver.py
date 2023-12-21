import sys
sys.path.insert(0, "./trainPredict/")
sys.path.insert(0, "./videoProcessing/")

import predicting
import video_proc

vc1 = video_proc.video_capture("./externalData/test.mp4")
vc1.create_path()
p1 = predicting.predict_data()
vc1.read_video(p1)
