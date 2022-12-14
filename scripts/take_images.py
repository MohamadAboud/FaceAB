import time

import cv2
import mediapipe as mp
from scripts.dev import kDeveloperMode
from scripts.data import Data
from utils.utils import *

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.7)

saveImagePath = "./data/users"  # + [ user folder -> user-00000 ]

def cropImage(frame):
    height, width, _ = frame.shape
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x = int(bbox.xmin * width) - 15
            y = int(bbox.ymin * height) - 75
            w = int(bbox.width * width + bbox.xmin * width) + 15
            h = int(bbox.height * height + bbox.ymin * height) + 15

            cropped_face = frame[y:h, x: w].copy()
            cropped_face = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2GRAY)

            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 3)
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -3)
            cv2.circle(frame, (w, h), 3, (0, 0, 255), -3)

            return (frame,cropped_face)

def save_image(image,count):
    path = f"{saveImagePath}/user-{Data.UID}/{count}.jpg"
    print(path)
    cv2.imwrite(path,image)



def TakeImages(updateProgressBar):


    Data.UID = str(time.time())
    CrateFolder(f"{saveImagePath}/user-{Data.UID}")


    cap = cv2.VideoCapture(0)

    count = 0
    while True:
        ret, frame = cap.read()




        try:
            frame, croppedFace = cropImage(frame)

            if count == 100:
                break
            count += 1
            updateProgressBar()

            save_image(croppedFace, count)
        except:
            pass


        cv2.imshow("Take Image", frame)
        cv2.imshow("Cropped face", croppedFace)
        key = cv2.waitKey(100)
        if kDeveloperMode and key == 27:
            break

    cap.release
    cv2.destroyAllWindows()

