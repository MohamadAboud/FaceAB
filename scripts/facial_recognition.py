import threading

import cv2
import face_recognition
from scripts.training_model import TrainingModel


class FacialThread(threading.Thread):
    def __init__(self,frame=None):
        super().__init__()
        self.__frame = frame
        self.userName = None

    def run(self):
        val = self.__getName(self.__frame)
        self.userName = val[0] if val != None else None

    def __getName(self,frame) -> str:
        model = TrainingModel.model
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame_rgb)

        face_code = face_recognition.face_encodings(frame_rgb, known_face_locations=faces)

        def predict(distance_threshold=0.6):
            # If no faces in cam.....
            if len(faces) == 0: return None

            closest_distances = model.kneighbors(face_code, n_neighbors=1)

            are_matches = [closest_distances[0][i][0] <= distance_threshold for i in
                           range(len(faces))]

            for pred, loc, rec in zip(model.predict(face_code), faces, are_matches):
                if rec:
                    return pred , loc
                else:
                    return "Unknown",loc

        return predict()

    def run_in_separate_window(self,src=0):
        from utils.edit_frame import drawBox
        cap = cv2.VideoCapture(src)

        while True:
            ret,frame = cap.read()

            val = self.__getName(frame)

            if val != None:
                name,loc = val
                (top, right, bottom, left) = loc
                drawBox(frame, (left,top), (bottom,right))
                # Draw a label with a name below the face
                cv2.rectangle(frame, (left - 40, bottom + 50), (right+40, bottom+10), (255, 255, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name.capitalize(), (left - 30, bottom + 35), font, 0.7, (0, 0, 0), 1)
            else:
                name,loc = None,None






            cv2.imshow("Facial recognition",frame)
            key = cv2.waitKey(1)
            if key == 27 or key == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()