from ui.core.core import *
from ui.routes.image_taking_screen import ImageScreen
from ui.widgets.widgets import *
from utils.check_file import Check


class SplashScreen(UserControl):

    instance = None
    @classmethod
    def init(cls):
        SplashScreen.instance = cls()
        return SplashScreen.instance

    def __init__(self):
        super().__init__()

        # Buttons --------------------
        self.getStartedButton = CustomButton(
            text=AppString.splashscreen.button1,
            width=WIDTH * 0.9,
            height=40,
            padding=padding.only(top=15, bottom=25),
            on_click= self.go_to_image_taking_screen
        )

        self.startAndAddButton = Column([
            CustomButton(
                text=AppString.splashscreen.button2,
                width=320,
                height=40,
                on_click=self.runApp
            ),

            CustomButton(
                text=AppString.splashscreen.button3,
                width=320,
                height=40,
                dColor=secondColor,
                dTextColor=primaryColor,
                padding=padding.only(top=5),
                on_click=self.go_to_image_taking_screen
            )
        ])

        if Check.isFirstTime:
            self.button = self.getStartedButton
        else:
            self.button = self.startAndAddButton


    def build(self):
        return Container(
            height=HEIGHT,
            width=WIDTH,
            bgcolor=backgroundColor,
            content=Column(
                horizontal_alignment =CrossAxisAlignment.START,
                controls=[
                    # Image --------------------
                    Image(
                        src=AppString.splashscreen.img,
                        height=250,
                        width=350,
                        fit=ImageFit.CONTAIN
                    ),

                    Container(height=10), # Padding

                    # Body[Column][Text] --------------------

                    Container(
                        padding=padding.symmetric(horizontal=25),
                        content=Column(
                            controls=[
                                # Welcome[Text] --------------------
                                Text(
                                    f"   {AppString.splashscreen.welcomText}",
                                    size=16,
                                    color=primaryColor,
                                    weight=FontWeight.BOLD,
                                ),

                                # Face Recognition Application[Text] --------------------
                                Column([
                                    Row([
                                        Text(f"{AppString.splashscreen.subText[0]}".upper(), size=25, weight=FontWeight.BOLD),
                                        Text(f"{AppString.splashscreen.subText[1]}".upper(), size=25, color=primaryColor,
                                             weight=FontWeight.BOLD),

                                    ]),
                                    Text(f"{AppString.splashscreen.subText[2]}".upper(), size=25, weight=FontWeight.BOLD)
                                ],spacing=0),

                                # Introduction[Text] --------------------
                                Column([
                                    Row([
                                        Text(f"{AppString.name[:3]}", opacity=0.4),
                                        Text(f"{AppString.name[3:]}", color=primaryColor),
                                        Text(f" {AppString.splashscreen.introText[0]}", opacity=0.4),

                                    ],spacing=0),
                                    Text(f"{AppString.splashscreen.introText[1]}", opacity=0.4,
                                         text_align=TextAlign.START)
                                ],spacing=0, opacity=0.4),

                                Container(height=10),  # Padding

                                # Buttons --------------------
                                self.button,

                                Signature(77, 111, 104, 97, 109, 97, 100, 32, 65, 98, 111, 117, 100)
                            ]
                        )
                    ),


                ]
            )
        )


    def runApp(self,e):
        print("Run App Cliked")

    def go_to_image_taking_screen(self,e):
        from ui.navigator import Navigator
        ImageScreen.init()
        Navigator.push(ImageScreen.instance)