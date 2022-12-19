import cv2

cap = cv2.VideoCapture(0)

modelsPath = "./assets/model"

MODEL_MEAN_VALUES = (78.4263377603,87.7689143744,144.895847764)
ageList = ['(0,2)', '(4,6)','(8,12)','(15,20)','(25,32)','(38,43)','(48,53)','(60,100)']
genderList = ['Male','Female']


class PredictingGenderAndAge:
    def __init__(self, frame):
        self.frame = frame
        self._loadModel()

    def _loadModel(self):
        self.age_net = cv2.dnn.readNetFromCaffe(f'{modelsPath}/deploy_age.prototxt', f'{modelsPath}/age_net.caffemodel')
        self.gender_net = cv2.dnn.readNetFromCaffe(f'{modelsPath}/deploy_gender.prototxt', f'{modelsPath}/gender_net.caffemodel')
        self.face_cascade = cv2.CascadeClassifier(f'{modelsPath}/haarcascade_frontalface_alt.xml')
        return (self.age_net, self.gender_net, self.face_cascade)

    def start(self):
        # Convert frame from BGR to RGB...
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, h, w) in faces:

            blob = cv2.dnn.blobFromImage(self.frame, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

            # Predict Gender
            self.gender_net.setInput(blob)
            gender_preds = self.gender_net.forward()
            gender = genderList[gender_preds[0].argmax()]
            print(f"Gender : {gender}")

            # Predict Age
            self.age_net.setInput(blob)
            age_preds = self.age_net.forward()
            age = ageList[age_preds[0].argmax()]
            print(f"Age Range: {age}")

            return  (age,gender)
