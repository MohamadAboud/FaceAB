from flet import *
from ui.core.core import AppColor,AppString

class SplashScreen(UserControl):

    def __init__(self,height,width):
        super().__init__()
        self.img = AppString.splachscreen.img
        self.height = height
        self.width = width

    def build(self):
        return Container(
            height=self.height,
            width=self.width,
            bgcolor=AppColor.backgroundColor,
            content=Column(
                spacing=15,
                horizontal_alignment =CrossAxisAlignment.CENTER,
                controls=[
                    # Image --------------------
                    Image(
                        src=self.img,
                        height=self.height * .2,
                        width=self.width,
                        fit=ImageFit.COVER
                    ),

                    Text(
                        "Loading ....",
                        weight=FontWeight.W_400,
                        size= 25,
                    ),

                    ProgressBar(
                        width=self.width,
                        color=AppColor.primaryColor,
                        bgcolor=AppColor.secondaryColor,
                    )

                ]
            )
        )