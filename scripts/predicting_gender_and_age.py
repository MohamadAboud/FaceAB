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
    def __init__(self, frame):
        super().__init__()
        self.__frame = frame
        self.age_and_gender = None,None

        # if not GenderAndAgeThread.isLoaded : self._loadModel()

    def run(self):
        self.age_and_gender = self._getAgeAndGender()


    # def _loadModel(self):
    #     self.age_net = cv2.dnn.readNetFromCaffe(f'{modelsPath}/deploy_age.prototxt', f'{modelsPath}/age_net.caffemodel')
    #     self.gender_net = cv2.dnn.readNetFromCaffe(f'{modelsPath}/deploy_gender.prototxt', f'{modelsPath}/gender_net.caffemodel')
    #     self.face_cascade = cv2.CascadeClassifier(f'{modelsPath}/haarcascade_frontalface_alt.xml')
    #     GenderAndAgeThread.isLoaded = True
    #     return (self.age_net, self.gender_net, self.face_cascade)


    def _getAgeAndGender(self):
        # Convert frame from BGR to RGB...
        gray = cv2.cvtColor(self.__frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, h, w) in faces:

            blob = cv2.dnn.blobFromImage(self.__frame, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

            # Predict Gender
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender = genderList[gender_preds[0].argmax()]

            # Predict Age
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = ageList[age_preds[0].argmax()]

            return  (age,gender)