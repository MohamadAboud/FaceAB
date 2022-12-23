from flet import *

from ui.core.core import AppColor,AppSize
from ui.core.core import AppString
from ui.widgets.dev import Signature
from ui.widgets.widgets import CustomButton,CustomTextField
from utils.utils import ChangeNameFolder


class ImageScreen(UserControl):
    instance = None
    @classmethod
    def init(cls):
        ImageScreen.instance = cls()
        return ImageScreen.instance

    def __init__(self):
        super().__init__()

        self.progressText = Text(AppString.imagescreen.progressText1, weight=FontWeight.W_500)

        self.progressBar = ProgressBar(
                                width=AppSize.width * 0.8,
                                color=AppColor.primaryColor,
                                bgcolor=AppColor.secondaryColor,
                            )

        # self.button = CustomButton(
        #     text="Next",
        #     width=WIDTH * 0.8,
        #     height=35,
        #     padding=padding.only(top=8),
        #     disabled=True,
        #     on_click=self.go_to_the_training_screen
        # )

    def __call__(self, *args, **kwargs):
        from scripts.scripts import StartTakeImages
        # Run [TakeImages] scripts...
        StartTakeImages()

    def build(self):
        return Stack([
            self.__progressscreen(),
            self.__namePopUp(),
            self.__closePopUpButton()
        ])

    ##############################| UI |##############################

    def __progressscreen(self):
        return Container(
            height=AppSize.height,
            width=AppSize.width,
            bgcolor=AppColor.backgroundColor,
            content=Column([
                # Image --------------------
                Container(
                    height=AppSize.height * 0.55,
                    width=AppSize.width,
                    bgcolor=AppColor.secondaryColor,
                    border_radius=border_radius.only(bottomLeft=35, bottomRight=35),
                    image_src=AppString.imagescreen.img,
                    image_fit=ImageFit.COVER,
                    # on_click= self.Test
                ),

                Container(height=10),  # Padding

                # Body[Column][Text] --------------------

                Container(
                    padding=padding.symmetric(horizontal=25),
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            # Text --------------------
                            Container(
                                on_click=self.openTest,
                                content=self.progressText
                            ),

                            # ProgressBar --------------------
                            self.progressBar,

                            Container(height=10),  # Padding

                            # Text --------------------
                            Text(
                                AppString.imagescreen.text1,
                                size=25,
                                weight=FontWeight.BOLD,
                            ),

                            Container(height=5),  # Padding

                            # Text --------------------
                            Text(
                                AppString.imagescreen.text2,
                                opacity=0.7,
                                text_align=TextAlign.CENTER
                            ),

                            Container(height=15),  # Padding

                            Signature(77, 111, 104, 97, 109, 97, 100, 32, 65, 98, 111, 117, 100)
                        ]
                    )
                ),



            ])
        )

    def __namePopUp(self):


        def on_change(e): # INFO: To refresh the UI when typing
            self.textField.controls[1].error_text = ""
            self.textField.controls[1].update()

        self.textField = CustomTextField(
                        title=AppString.imagescreen.PopUp.textFieldTitle,
                        hint_text=AppString.imagescreen.PopUp.textFieldHintText,
                        icons=icons.PERSON,
                        # error_text="Test....",
                        on_submit=self.__submit,
                        on_change= on_change
                    )

        self.popUp = Container(
            padding=padding.symmetric(horizontal=20,vertical=20),
            bgcolor="black",
            opacity= 0.95,
            top=AppSize.height * 0.15,
            left=AppSize.width  * 0.05,
            right=AppSize.width * 0.05,
            bottom=AppSize.height  * 0.173,
            border_radius=border_radius.all(12),
            clip_behavior=ClipBehavior.ANTI_ALIAS_WITH_SAVE_LAYER,
            offset=transform.Offset(0, -2),
            animate_offset=animation.Animation(1000),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.START,
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    # Text --------------------
                    Row([
                        Text(
                            AppString.imagescreen.PopUp.title,
                            weight=FontWeight.BOLD,
                            scale=1.8,
                            color='white'
                        ),
                    ],alignment=MainAxisAlignment.CENTER),

                    Container(height=10) ,  # Padding

                    # Text --------------------
                    Text(
                        AppString.imagescreen.PopUp.subText,
                        color='white',
                        size=17,
                    ),

                    Container(height=10),  # Padding

                    self.textField,

                    Container(height=10),  # Padding

                    CustomButton(
                        text=AppString.imagescreen.PopUp.buttonText1,
                        width=AppSize.width * 0.8,
                        dColor="white",
                        hColor="#deddd9",
                        dTextColor="#808080",
                        hTextColor="black",
                        on_click=self.__check_and_go_to_the_welcome_screen
                    ),

                    CustomButton(
                        text= AppString.imagescreen.PopUp.buttonText2,
                        width= AppSize.width * 0.8,
                        dColor="black",
                        dTextColor="white",
                        hColor="#deddd9",
                        on_click=self.__check_and_go_to_the_training_screen
                    ),
                ]
            )
        )
        return self.popUp

    ##############################| Private methods |##############################

    def __closePopUpButton(self):

        self.closeButton = Card(
            bottom=95,
            left=150,
            right=150,
            elevation=10,
            height=35,
            tooltip=AppString.imagescreen.PopUp.closeTooltip,
            offset=transform.Offset(0, 3),
            animate_offset=animation.Animation(1000),
            content=Container(
                bgcolor="white",
                shape=BoxShape.CIRCLE,
                on_click=self.__destroy_the_process,
                content=Icon(icons.CLOSE,size=14),
            )
        )

        return self.closeButton

    def __closePopUp(self):
        # close the popup
        self.popUp.offset = transform.Offset(0, -2)
        self.closeButton.offset = transform.Offset(0, 3)
        self.popUp.update()
        self.closeButton.update()

        # wait for animation to finish
        time.sleep(1)

    def __chackUserName(self,method=None):
        self.textField.controls[1].error_text = ""
        name = self.textField.controls[1].value

        if len(name) == 0:
            self.textField.controls[1].error_text = AppString.imagescreen.PopUp.textFieldError
            self.textField.controls[1].update()
            return

        self.textField.controls[1].update()


        # change folder name ...
        errorText = ""
        try:
            from scripts.scripts import Data
            ChangeNameFolder(
                path=AppString.path.saveImg,
                oldname=f"user-{Data.UID}",
                newname=f"{name.lower()}",
            )
            if method: method()
            return

        except FileExistsError:
            errorText = AppString.imagescreen.PopUp.fileNotExistsError
        except OSError:
            errorText = AppString.imagescreen.PopUp.osError
        except Exception as err:
            errorText = AppString.imagescreen.PopUp.error
            print(f"Error : {err}")

        if len(errorText) != 0:
            self.textField.controls[1].error_text = errorText
            self.textField.controls[1].update()

    ##############################| Events |##############################

    def __submit(self,e):
        ...

    def __check_and_go_to_the_welcome_screen(self, e):
        def method():
            # close PopUp
            self.__closePopUp()

            from ui.routes.routes import WelcomScreen
            from ui.navigator import Navigator
            # push WelcomScreen
            Navigator.popAllAndPush(WelcomScreen.init())
            WelcomScreen.instance()

        self.__chackUserName(method=method)

    def __check_and_go_to_the_training_screen(self, e):
        def method():
            # close PopUp
            self.__closePopUp()

            from ui.routes.routes import TrainingScreen
            from ui.navigator import Navigator
            # push TrainingScreen
            Navigator.popAllAndPush(TrainingScreen.init())
            TrainingScreen.instance()

        self.__chackUserName(method=method)

    def __destroy_the_process(self,e):
        # close PopUp ....
        self.__closePopUp()

        # delete the folder and images ....
        from utils.utils import DeleteFolder
        from scripts.scripts import Data
        path = os.path.join(AppString.path.saveImg, f"user-{Data.UID}")
        DeleteFolder(path=path)

        # go to the previous page ....
        from ui.navigator import Navigator
        Navigator.pop()

    ##############################| Public methods |##############################

    def increaseProgressBar(self):
        val = self.progressBar.value
        if val == None: val = 0.01
        else: val += 0.01

        self.progressText.value = f"{int(val * 100)}% {AppString.imagescreen.progressText2}"
        self.progressBar.value = val

        # When the progressBar Completed
        if val >= 1.0 :
            self.popUp.offset = transform.Offset(0, 0)
            self.closeButton.offset  = transform.Offset(0, 0)
            self.popUp.update()
            self.closeButton.update()

        # Update UI ..................
        self.progressBar.update()
        self.progressText.update()

    ##############################| Test |##############################

    def Test(self,e):
        ImageScreen.instance()
    def openTest(self,e):
        self.popUp.offset = transform.Offset(0, 0)
        self.closeButton.offset = transform.Offset(0, 0)
        self.popUp.update()
        self.closeButton.update()