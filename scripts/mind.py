import threading
import cv2

from scripts.pose_detector import BodyDetector


class MindThread(threading.Thread):

    draw = True

    def __init__(self,title=str,src=0):
        threading.Thread.__init__(self)

        self.title = title
        self.cap = cv2.VideoCapture(src)
        self.cap.set(3,1200)
        self.cap.set(4,720)

        #     for Card.........
        self.__cardImg = cv2.imread("./assets/images/card3.jpg", cv2.IMREAD_UNCHANGED)
        self.__cardBigImg = cv2.imread("./assets/images/card3.jpg", cv2.IMREAD_UNCHANGED)
        self.resizeCard(scale=0.2)


    def resizeCard(self, scale):
        heightCard, widthCard, _ = self.__cardImg.shape
        self.__newHeightCard, self.__newWidthCard = int(heightCard * scale), int(widthCard * scale)
        self.__cardImg = cv2.resize(self.__cardImg, (self.__newWidthCard, self.__newHeightCard))

    def run(self):
        self.__startCam()

    def __startCam(self):

        while True:
            ret, frame = self.cap.read()
            if ret is None:
                break

            cardOffset = self.__getCardOffset(frame)
            self.__cardInfo(frame, cardOffset)

            self.__addInfoToCard(frame=frame, cardOffset=cardOffset)


            cv2.imshow(self.title,frame)
            cv2.imshow("card" , self.__cardBigImg)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def __getCardOffset(self,frame):
        start_point, end_point = BodyDetector(frame=frame, isDraw=self.draw).run()
        xOffsetCard, yOffsetCard = end_point[0] - self.__cardImg.shape[1] // 2, end_point[1]
        return (xOffsetCard, yOffsetCard)

    def __cardInfo(self,frame,offset:tuple):
        #  Card ID -------------------------------------------------------------------

        check = (offset[1] + self.__newHeightCard, offset[0] + self.__newWidthCard)
        #   ----left----      ----right----      ----bottom----
        self.draw = check[1] > 50 and check[1] < 950 and check[0] < 540

        if self.draw:
            h = offset[1] + self.__newHeightCard
            w = offset[0] + self.__newWidthCard

            frame[ offset[1]:h , offset[0]:w ] = self.__cardImg

            # cv2.circle(frame, offset, 3, (255, 0, 0), 4)
            # cv2.circle(frame, (w,h), 3, (0, 250, 0), 4)

            cv2.rectangle(frame, offset, (w,h), (0, 255, 0), 4)

    def __addInfoToCard(self,frame,cardOffset):
        w,h = cardOffset[0]+self.__newWidthCard//2, cardOffset[1]+self.__newHeightCard//2

        #########################################################################################################
        nameOffset = (w - 17 , h )
        name = self.__getName(frame)
        self.__putText(frame,name,offset=nameOffset,fontScale=0.14)
        self.__putText(self.__cardBigImg,name,offset=(25,275),fontScale=0.7)

        ageOffset = (w - 17 , h + 10)
        age = self.__getAge(frame)
        self.__putText(frame,age,offset=ageOffset,fontScale=0.13)

        genderOffset = (w -7 , h + 20)
        gender = self.__getGender(frame)
        self.__putText(frame,gender,offset=genderOffset)


        if len(name) > 13: raise ValueError("Length must be 13 characters or less")


    def __putText(self,frame,text:str,offset:tuple,fontScale = 0.12):
        if self.draw is not True :return

        # Black color
        color = (0, 0, 0)
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, text, offset, font,
                            fontScale, color, 1, cv2.LINE_AA)


    # ----------------------------------------------------------------
    def __getName(self,frame):
        name = "Mohamad Aboud"

        return name

    def __getAge(self, frame):
        age = "(20 - 24) Years"

        return age

    def __getGender(self, frame):
        gender = "{:>7}".format("Male")

        return gender