import time
import cv2
from scripts.data import Data
from ui.core.core import AppString
from ui.routes.routes import ImageScreen
from utils.utils import Developer,cropFace,CrateFolder

###############################
############ Model ############
###############################


def save_image(image,count):
    path = f"{AppString.path.saveImg}/user-{Data.UID}/{count}.jpg"
    Developer.log(path)
    cv2.imwrite(path,image)



def StartTakeImages():


    Data.UID = str(time.time())
    CrateFolder(f"{AppString.path.saveImg}/user-{Data.UID}")

    cap = cv2.VideoCapture(0)

    # cap.set(3,WIDTH)
    # cap.set(4,HEIGHT)

    count = 0
    while True:
        ret, frame = cap.read()

        try:
            if count == 100: break

            frame, croppedFace = cropFace(frame)

            count += 1
            ImageScreen.instance.increaseProgressBar()

            if Developer.isTesting: cv2.imshow("DeveloperMode[True]", croppedFace)
            save_image(croppedFace, count)
        except:
            pass


        cv2.imshow("Take Image", frame)

        key = cv2.waitKey(50)
        if Developer.isTesting and key == 27:break

    cap.release
    cv2.destroyAllWindows()

