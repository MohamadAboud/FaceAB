import threading
from cvzone.PoseModule import PoseDetector
import cv2
from utils.dev import Developer

detector = PoseDetector()

class BodyDetectorThread(threading.Thread):

    def __init__(self,frame,isDraw):
        super().__init__()
        # ------------------------------
        self.__frame = frame
        self.__isDraw = isDraw
        self.points = None
        # ------------------------------

    def __covertFrame(self,frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return rgb_frame

    @property
    def frame(self):
        f = cv2.cvtColor(self.__frame,cv2.COLOR_RGB2BGR)
        small_frame = cv2.resize(f, (0, 0), fx=0.5, fy=0.5)
        return small_frame

    def run(self):
        self.points = self.__pose()

    def __pose(self):
        rgb_frame = self.__covertFrame(self.__frame)
        # pose --------------------------------------------------------------
        self.__frame = detector.findPose(rgb_frame, draw=Developer.isTesting)
        cv2.imshow('selftitle', self.__frame)
        lmList, bboxInfo = detector.findPosition(self.__frame, bboxWithHands=False,draw = False)
        if bboxInfo:
            landmarks = lmList[11][1:]
            start_point = (landmarks[0] - 50, landmarks[1])
            end_point = (landmarks[0] - 50, landmarks[1] + 30)

            color = (0, 255, 0)

            if self.__isDraw:
                cv2.line  (self.__frame, start_point, end_point, color, 2  )
                cv2.circle(self.__frame, start_point, 3, color , cv2.FILLED)
                cv2.circle(self.__frame, end_point  , 3, color , cv2.FILLED)

            # val = (abs(landmarks[2]) /1000)
            # if val > 0.13 and val < 0.25:
            #     scale = val

            return (start_point,end_point)
