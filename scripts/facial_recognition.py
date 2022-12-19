import cv2
import face_recognition
from scripts.training_model import TrainingModel


def getName(frame):

    model = TrainingModel.model
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(frame_rgb)

    face_code = face_recognition.face_encodings(frame_rgb, known_face_locations=faces)

    def predict(distance_threshold=0.6):
        # If no faces in cam.....
        if len(faces) == 0: return ''

        closest_distances = model.kneighbors(face_code, n_neighbors=1)

        are_matches = [closest_distances[0][i][0] <= distance_threshold for i in
                       range(len(faces))]

        for pred, loc, rec in zip(model.predict(face_code), faces, are_matches):
            if rec:
                return pred
            else:
                return "Unknown"

    return predict()