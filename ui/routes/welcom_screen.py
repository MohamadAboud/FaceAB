from ui.core.core import *
from ui.routes.image_taking_screen import ImageScreen
from ui.widgets.widgets import *
from utils.check_file import Check


class WelcomScreen(UserControl):

    instance = None
    @classmethod
    def init(cls):
        WelcomScreen.instance = cls()
        return WelcomScreen.instance

    def __init__(self):
        super().__init__()

        # Buttons --------------------
        self.getStartedButton = CustomButton(
            text=AppString.splashscreen.button1,
            width=AppSize.width * 0.9,
            height=40,
            padding=padding.only(top=15, bottom=25),
            on_click= self.go_to_image_taking_screen
        )

        self.startAndAddButton = Column([
            CustomButtonDropDown(
                text=AppString.splashscreen.button2,
                width=320,
                height=40,
                on_click=self.runApp,
                items=[
                    CustomItem(
                        text="Card",
                        on_click=self.__go_to_card_window
                    ),
                    CustomItem(
                        text="Body",
                        on_click=self.__go_to_body_window
                    ),
                    CustomItem(
                        text="Face",
                        on_click=self.__go_to_face_window
                    ),
                    CustomItem(
                        text="Age ..",
                        on_click=self.__go_to_age_and_gender_window
                    ),
                ],
                hTextColor="white",
            ),

            CustomButton(
                text=AppString.splashscreen.button3,
                width=320,
                height=40,
                dColor=AppColor.secondaryColor,
                dTextColor=AppColor.primaryColor,
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
            height=AppSize.height,
            width=AppSize.width,
            bgcolor=AppColor.backgroundColor,
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
                                    color=AppColor.primaryColor,
                                    weight=FontWeight.BOLD,
                                ),

                                # Face Recognition Application[Text] --------------------
                                Column([
                                    Row([
                                        Text(f"{AppString.splashscreen.subText[0]}".upper(), size=25, weight=FontWeight.BOLD),
                                        Text(f"{AppString.splashscreen.subText[1]}".upper(), size=25, color=AppColor.primaryColor,
                                             weight=FontWeight.BOLD),

                                    ]),
                                    Text(f"{AppString.splashscreen.subText[2]}".upper(), size=25, weight=FontWeight.BOLD)
                                ],spacing=0),

                                # Introduction[Text] --------------------
                                Column([
                                    Row([
                                        Text(f"{AppString.name[:3]}", opacity=0.4),
                                        Text(f"{AppString.name[3:]}", color=AppColor.primaryColor),
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
        from scripts.mind import Mind

        mind = Mind(title="AI")
        mind.run()


    def go_to_image_taking_screen(self,e):
        from ui.navigator import Navigator
        # push ImageScreen
        Navigator.push(ImageScreen.init())
        ImageScreen.instance()

    def __go_to_card_window(self):
        self.runApp('')

    def __go_to_body_window(self):
        print("go_to_body_window")
    def __go_to_face_window(self):
        print("__go_to_face_window")
    def __go_to_age_and_gender_window(self):
        print("__go_to_age_and_gender_window")