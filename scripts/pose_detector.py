import threading
import mediapipe as mp
import cv2
from utils.dev import Developer


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)


class BodyDetectorThread(threading.Thread):

    def __init__(self, frame, isDraw):
        super().__init__()
        # ------------------------------
        self.__frame = frame
        self.__isDraw = isDraw
        self.points = None
        # ------------------------------

    def __covertFrame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return rgb_frame

    @property
    def frame(self):
        small_frame = cv2.resize(self.__frame, (0, 0), fx=0.5, fy=0.5)
        return small_frame

    def run(self):
        self.__frame = self.__frame.copy()
        self.points = self.__pose()

    def __pose(self):
        rgb_frame = self.__covertFrame(self.__frame)

        # pose --------------------------------------------------------------
        results = pose.process(rgb_frame)
        landmarks = results.pose_landmarks

        if landmarks:
            h, w, _ = self.__frame.shape

            hartLandmark = (landmarks.landmark[11].x, landmarks.landmark[11].y)
            x = int(hartLandmark[0] * w)
            y = int(hartLandmark[1] * h)

            start_point = (x - 50, y)
            end_point = (x - 50, y + 30)

            color = (0, 255, 0)

            if self.__isDraw:
                cv2.line(self.__frame, start_point, end_point, color, 2)
                cv2.circle(self.__frame, start_point, 3, color, cv2.FILLED)
                cv2.circle(self.__frame, end_point, 3, color, cv2.FILLED)

                if Developer.isTesting:
                    mp_drawing.draw_landmarks(
                        self.__frame,
                        results.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
                    )

            # val = (abs(landmarks[2]) /1000)
            # if val > 0.13 and val < 0.25:
            #     scale = val

            return (start_point, end_point)