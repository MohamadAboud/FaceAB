import cv2
from scripts.pose_detector import BodyDetector


class Mind:

    draw = True

    def __init__(self,title=str,src=0):

        self.title = title
        self.cap = cv2.VideoCapture(src)
        self.cap.set(3,1200)
        self.cap.set(4,720)

        #     for Card.........
        self.__cardImg = cv2.imread("./assets/images/smallCard.jpg", cv2.IMREAD_UNCHANGED)
        self.__cardBigImg = cv2.imread("./assets/images/bigCard.jpg", cv2.IMREAD_UNCHANGED)
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

            try:
                self.__cardBigFrame = self.__cardBigImg.copy()

                cardOffset = self.__getCardOffset(frame)
                self.__cardInfo(frame, cardOffset)
                self.__addInfoToCard(frame=frame, cardOffset=cardOffset)
            except:
                self.__cardBigFrame = self.__cardBigImg.copy()


            cv2.imshow(self.title,frame)
            cv2.imshow("My Card",self.__cardBigFrame)


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

        bigFrame = self.__cardBigFrame
        #########################################################################################################

        name = self.__getName(frame)
        self.__putText(frame,name,offset=(w - 17 , h ),fontScale=0.14)
        self.__putText(bigFrame,name,offset=(25,275),fontScale=0.7)

        age,gender = self.__getAgeAndGender(frame)

        self.__putText(frame,age,offset=(w - 17 , h + 10),fontScale=0.13)
        self.__putText(bigFrame, age, offset=(25, 300), fontScale=0.6)

        self.__putText(frame,gender,offset=(w -7 , h + 20))
        self.__putText(bigFrame, gender, offset=(50, 330), fontScale=0.7)



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
        from scripts.facial_recognition import getName
        name = getName(frame=frame)
        print(f"name = {name}")

        return name

    def __getAgeAndGender(self, frame):
        from scripts.predicting_gender_and_age import PredictingGenderAndAge
        pred = PredictingGenderAndAge(frame)
        age, gender =  pred.start()

        return (age+" Years",gender)