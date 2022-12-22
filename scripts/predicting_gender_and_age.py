import multiprocessing
import threading

import cv2


modelsPath = "./assets/model"

################################
##########| Vlaues |############
################################
MODEL_MEAN_VALUES = (78.4263377603,87.7689143744,144.895847764)
ageList = ['(0,2)', '(4,6)','(8,12)','(15,20)','(25,32)','(38,43)','(48,53)','(60,100)']
genderList = ['Male','Female']

################################
##########| Model |#############
################################
age_net = cv2.dnn.readNetFromCaffe(f'{modelsPath}/deploy_age.prototxt', f'{modelsPath}/age_net.caffemodel')
gender_net = cv2.dnn.readNetFromCaffe(f'{modelsPath}/deploy_gender.prototxt', f'{modelsPath}/gender_net.caffemodel')
face_cascade = cv2.CascadeClassifier(f'{modelsPath}/haarcascade_frontalface_alt.xml')


class GenderAndAgeThread(threading.Thread):

    # isLoaded = False
    def __init__(self, frame=None):
        super().__init__()
        self.__frame = frame
        self.age_and_gender = None

        # if not GenderAndAgeThread.isLoaded : self._loadModel()

    def __covertFrame(self,frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame

    @property
    def frame(self):
        small_frame = cv2.resize(self.__frame, (0, 0), fx=0.5, fy=0.5)
        return small_frame

    def run(self):
        data = self.__getAgeAndGender(self.__frame)
        if data is not None:
            self.age_and_gender = data[:2]

    def __drwaBox(self,frame,text,loc):
        from utils.edit_frame import drawBox

        (x, y, w, h) = tuple(loc[0])
        (top, right, bottom, left) = (y, x + w, y + h, x)

        drawBox(frame, (left, top), (bottom, right))
        # Draw a label with a text below the face
        cv2.rectangle(frame, (left - 40, bottom + 50), (right + 40, bottom + 10), (255, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, text, (left - 30, bottom + 35), font, 0.7, (0, 0, 0), 1)

    def __getAgeAndGender(self,frame):
        # Convert frame from BGR to RGB...
        gray_frame = self.__covertFrame(frame)
        faces = face_cascade.detectMultiScale(gray_frame, 1.1, 5)

        for (x, y, h, w) in faces:

            blob = cv2.dnn.blobFromImage(frame, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

            # Predict Gender
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender = genderList[gender_preds[0].argmax()]

            # Predict Age
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = ageList[age_preds[0].argmax()]

            self.__frame = frame.copy()
            self.__drwaBox(self.__frame,text=f"{age} | {gender}",loc=faces)

            return  (age,gender,faces)

    def run_in_separate_window(self,src=0):

        cap = cv2.VideoCapture(src)

        while True:
            ret,frame = cap.read()

            data = self.__getAgeAndGender(frame)
            if data is not None:
                age, gender, loc = data
                self.__drwaBox(frame, text=f"{age} | {gender}", loc=loc)


            cv2.imshow("Age and gender classification",frame)
            key = cv2.waitKey(1)
            if key == 27 or key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()