from cvzone.PoseModule import PoseDetector
import cv2

from scripts.dev import kDeveloperMode


class BodyDetector():

    def __init__(self,frame,isDraw):

        self.frame = frame
        self.isDraw = isDraw

        self.detector = PoseDetector()

    def run(self):
        return self.__pose()

    def __pose(self):
        # pose --------------------------------------------------------------
        self.frame = self.detector.findPose(self.frame, draw=kDeveloperMode)
        lmList, bboxInfo = self.detector.findPosition(self.frame, bboxWithHands=False,draw = False)
        if bboxInfo:
            landmarks = lmList[11][1:]
            start_point = (landmarks[0] - 50, landmarks[1])
            end_point = (landmarks[0] - 50, landmarks[1] + 30)

            color = (0, 255, 0)

            if self.isDraw:
                cv2.line  (self.frame, start_point, end_point, color, 2  )
                cv2.circle(self.frame, start_point, 3, color , cv2.FILLED)
                cv2.circle(self.frame, end_point  , 3, color , cv2.FILLED)



            # val = (abs(landmarks[2]) /1000)
            # if val > 0.13 and val < 0.25:
            #     scale = val

            return (start_point,end_point)
