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
            text=AppString.welcomescreen.button1,
            height=40,
            on_click= self.go_to_image_taking_screen
        )

        self.startAndAddButton = Column([
            CustomDropDownButton(
                text=AppString.welcomescreen.button2,
                on_click=self.runApp,
                items=[
                    CustomItem(
                        text="Card",
                        on_click=self.__go_to_card_window
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
            ),

            CustomButton(
                text=AppString.welcomescreen.button3,
                height=40,
                default_bgcolor=AppColor.secondaryColor,
                default_textcolor=AppColor.primaryColor,
                on_click=self.go_to_image_taking_screen
            )
        ])

        if Check.isFirstTime:
            self.button = self.getStartedButton
        else:
            self.button = self.startAndAddButton

    def __call__(self, *args, **kwargs):
        # Do nothing ...
        ...

    def build(self):
        return Container(
            height=AppSize.height,
            width=AppSize.width,
            bgcolor=AppColor.backgroundColor,
            content=Column(
                horizontal_alignment =CrossAxisAlignment.START,
                controls=[
                    # Image --------------------
                    DynamicTaps(
                        height=250,
                        width=350,
                        content=Image(
                            src=AppString.welcomescreen.img,
                            fit=ImageFit.CONTAIN
                        )
                    ),

                    Container(height=10), # Padding

                    # Body[Column][Text] --------------------

                    Container(
                        padding=padding.symmetric(horizontal=25),
                        content=Column(
                            horizontal_alignment=AppString.alignment(),
                            controls=[
                                # Welcome[Text] --------------------
                                Text(
                                    f"   {AppString.welcomescreen.welcomText}",
                                    size=16,
                                    color=AppColor.primaryColor,
                                    weight=FontWeight.BOLD,
                                ),

                                # Face Recognition Application[Text] --------------------
                                Column([
                                    Row([
                                        Text(f"{AppString.welcomescreen.subText[0]}".upper(), size=25, weight=FontWeight.BOLD),
                                        Text(f"{AppString.welcomescreen.subText[1]}".upper(), size=25, color=AppColor.primaryColor,
                                             weight=FontWeight.BOLD),

                                    ],alignment=AppString.alignment()),
                                    Text(f"{AppString.welcomescreen.subText[2]}".upper(), size=25, weight=FontWeight.BOLD)
                                ],spacing=0,horizontal_alignment=AppString.alignment()),

                                # Introduction[Text] --------------------
                                Column([
                                    Row([
                                        Text(f"{AppString.name[:3]}", opacity=0.6),
                                        Text(f"{AppString.name[3:]}", color=AppColor.primaryColor),
                                        Text(f" {AppString.welcomescreen.introText[0]}", opacity=0.6),

                                    ],spacing=0,alignment=AppString.alignment()),
                                    Text(f"{AppString.welcomescreen.introText[1]}", opacity=0.6,
                                         text_align=TextAlign.START)
                                ],spacing=0, opacity=0.6,horizontal_alignment=AppString.alignment()),

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

    def __go_to_card_window(self,_):
        self.runApp('')

    def __go_to_body_window(self,_):
        print("go_to_body_window")
    def __go_to_face_window(self,_):
        from scripts.scripts import FacialThread
        FacialThread().run_in_separate_window()

    def __go_to_age_and_gender_window(self,_):
        from scripts.scripts import GenderAndAgeThread
        GenderAndAgeThread().run_in_separate_window()