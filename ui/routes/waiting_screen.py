from flet import *
from ui.core.core import AppSize,AppString
from ui.widgets.widgets import CustomButton


class WaitingScreen(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            height=AppSize.height,
            width=AppSize.width,
            content=Column([
                self.__appBar(),
                self.__body(),
            ])
        )

    def __appBar(self):
        return Container(
            height=AppSize.height * .6,
            width=AppSize.width,
            content=Column([
                # Dot ....
                Row([
                    Image(
                        src=AppString.waitingscreen.dotImg,
                        height= AppSize.height * .08,
                        width=AppSize.width * .15,
                        fit=ImageFit.CONTAIN
                    )
                ]),

                # waiting image ...
                Image(
                    src=AppString.waitingscreen.img,
                    fit=ImageFit.CONTAIN,
                    expand=True
                )
            ],spacing=0)
        )


    def __body(self):
        return Container(
            expand=True,
            alignment=alignment.center,
            # bgcolor="red",
            content=Column([
                # Text ...
                Text(
                        AppString.waitingscreen.text,
                        text_align=TextAlign.CENTER,
                        weight=FontWeight.BOLD,
                        size= 18
                    ),

                # close button
                # CustomButton(
                #     text="Close".upper(),
                #     default_bgcolor="#4162e6",
                #     hover_bgcolor="red",
                #     hover_textcolor="white",
                #     on_click=self.__on_click,
                #     icon=icons.CANCEL_PRESENTATION
                # )
            ],alignment=MainAxisAlignment.SPACE_EVENLY)
        )


    ##########################################| Events |##########################################
    # def __on_click(self,_):
    #     import cv2
    #     from utils.dev import Developer
    #
    #     Developer.log("Close",mode='info')
    #     cv2.destroyAllWindows()
