import time
import cv2

from utils.dev import Developer


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

            self.__cardBigFrame = self.__cardBigImg.copy()
            self.__showResult(frame)

            cv2.imshow(self.title,frame)
            cv2.imshow("My Card",self.__cardBigFrame)

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q') or key & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def __getCardOffset(self,points):
        if points == None : return None

        start_point, end_point = points
        xOffsetCard, yOffsetCard = end_point[0] - self.__cardImg.shape[1] // 2, end_point[1]
        return (xOffsetCard, yOffsetCard)

    def __cardInfo(self,frame,offset):
        if offset == None : return None

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

    def __addInfoToCard(self,frame,cardOffset,name,age_gender):
        bigFrame = self.__cardBigFrame

        name = name if name is not None else "UNKNOWN"

        if age_gender is not None:
            age= age_gender[0] + " Years"
            gender = age_gender[1]
        else:
            age, gender = "---- Years","---"

        if cardOffset is not None:
            w,h = cardOffset[0]+self.__newWidthCard//2, cardOffset[1]+self.__newHeightCard//2

            self.__putText(frame,name,offset=(w - 17 , h ),fontScale=0.14)
            self.__putText(frame,age,offset=(w - 17 , h + 10),fontScale=0.13)
            self.__putText(frame,gender,offset=(w -7 , h + 20))

        self.__putText(bigFrame, name, offset=(25, 275), fontScale=0.7)
        self.__putText(bigFrame, age, offset=(50, 300), fontScale=0.6)
        self.__putText(bigFrame, gender, offset=(90, 330), fontScale=0.7)



        if len(name) > 13: raise ValueError("Length must be 13 characters or less")

    def __putText(self,frame,text:str,offset:tuple,fontScale = 0.12):
        if self.draw is not True :return

        # Black color
        color = (0, 0, 0)
        # font
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, text, offset, font,
                            fontScale, color, 1, cv2.LINE_AA)


    def __showResult(self,frame):
        try:
            from scripts.scripts import BodyDetectorThread, FacialThread, GenderAndAgeThread

            body = BodyDetectorThread(frame=frame, isDraw=self.draw)
            facial = FacialThread(frame)
            pred = GenderAndAgeThread(frame)

            # Start the thread
            body.start()
            facial.start()
            pred.start()

            # Wait for the thread to finish
            body.join()
            facial.join()
            pred.join()

            cardOffset = self.__getCardOffset(points=body.points)
            self.__cardInfo(frame, cardOffset)
            self.__addInfoToCard(
                frame=frame,
                cardOffset=cardOffset,
                name= facial.userName,
                age_gender= pred.age_and_gender
            )

        except Exception as err:
            Developer.log(f"error : {err}",mode='error')