from flet import *

from ui.core.core import HEIGHT,WIDTH,backgroundColor,primaryColor,secondColor
from ui.widgets.dev import Signature
from ui.widgets.widgets import CustomButton,CustomTextField

# def updateProgressBar():
#     global txt1,progressBar,button
#     value = progressBar.controls[0].value + 0.01
#
#     if value > 1.0:
#         value = 1.0
#         nextButton.content.disabled = False
#         nextButton.content.update()
#
#     txt1.content.value = f"{int(value * 100)}% recognised"
#     txt1.update()
#     progressBar.controls[0].value = value
#     progressBar.controls[0].update()






class ImageScreen(UserControl):
    instance = None
    @classmethod
    def init(cls):
        ImageScreen.instance = cls()
        return ImageScreen.instance

    def __init__(self):
        super().__init__()

        self.progressText = Text("Loading...", weight=FontWeight.W_500)

        self.progressBar = ProgressBar(
                                width=WIDTH * 0.8,
                                color=primaryColor,
                                bgcolor=secondColor,
                            )

        self.button = CustomButton(
            text="Next",
            width=WIDTH * 0.8,
            height=35,
            padding=padding.only(top=8),
            disabled=True,
            on_click=self.go_to_the_training_screen
        )

    def build(self):
        return Stack([
            self._progressscreen(),
            self._namePopUp(),
            self._closePopUpButton()
        ])


    def _progressscreen(self):
        return Container(
            height=HEIGHT,
            width=WIDTH,
            bgcolor=backgroundColor,
            content=Column([
                # Image --------------------
                Container(
                    height=HEIGHT * 0.55,
                    width=WIDTH,
                    bgcolor=secondColor,
                    border_radius=border_radius.only(bottomLeft=35, bottomRight=35),
                    image_src="images/loading.gif",
                    image_fit=ImageFit.COVER,
                    on_click= self.Test
                ),

                Container(height=10),  # Padding

                # Body[Column][Text] --------------------

                Container(
                    padding=padding.symmetric(horizontal=25),
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            # Text --------------------
                            self.progressText,

                            # ProgressBar --------------------
                            self.progressBar,

                            # Text --------------------
                            Text(
                                "Verification Process",
                                size=25,
                                weight=FontWeight.BOLD,
                            ),

                            # Text --------------------
                            Text(
                                "Smile & blink your eyes,then move your\nhead slowly to complete the process",
                                opacity=0.7,
                                text_align=TextAlign.CENTER
                            ),

                            # Text --------------------
                            self.button,

                            Signature(77, 111, 104, 97, 109, 97, 100, 32, 65, 98, 111, 117, 100)
                        ]
                    )
                ),



            ])
        )

    def _namePopUp(self):


        def on_change(e):
            self.textField.controls[1].error_text = ""
            self.textField.controls[1].update()

        self.textField = CustomTextField(
                        title="Name",
                        hint_text="Enter your name",
                        icons=icons.PERSON,
                        # error_text="Test....",
                        on_submit=self._chackUserName,
                        on_change= on_change
                    )

        self.popUp = Container(
            padding=padding.symmetric(horizontal=20,vertical=20),
            bgcolor="white",
            opacity= 0.95,
            top= HEIGHT * 0.15,
            left=WIDTH * 0.05,
            right=WIDTH * 0.05,
            bottom=HEIGHT * 0.173,
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
                            "Sign in",
                            weight=FontWeight.BOLD,
                            scale=1.8,
                            color='black'
                        ),
                    ],alignment=MainAxisAlignment.CENTER),

                    Container(height=10) ,  # Padding

                    # Text --------------------
                    Text(
                        "Lorem ipsum dolor sit amet, \nconsectetur adipiscing elit. Maecenas est felis,",
                        color='black'
                    ),

                    Container(height=10),  # Padding

                    self.textField,

                    Container(height=10),  # Padding

                    CustomButton(
                        text="Done",
                        width= WIDTH * 0.8,
                        dColor="black",
                        dTextColor="white",
                        hColor="#deddd9",
                        on_click=self._chackUserName
                    )

                ]
            )
        )
        return self.popUp

    def _closePopUpButton(self):
        self.closeButton = Container(
            bottom=95,
            left= 150,
            right=150,
            height=35,
            bgcolor="black",
            shape=BoxShape.CIRCLE,
            content=Icon(icons.CLOSE,size=14),
            on_click=self._closePopUp,
            tooltip="Your facial data will be deleted,\n are you sure?",
            offset=transform.Offset(0, 3),
            animate_offset=animation.Animation(1000),
            )
        return self.closeButton

    def _chackUserName(self,e):
        self.textField.controls[1].error_text = ""
        name = self.textField.controls[1].value

        if len(name) == 0:
            self.textField.controls[1].error_text = "Name is required"
            self.textField.controls[1].update()
            return

        self.textField.controls[1].update()

    def _closePopUp(self,e):
        self.popUp.offset = transform.Offset(0, -2)
        self.closeButton.offset = transform.Offset(0, 3)
        self.popUp.update()
        self.closeButton.update()

        time.sleep(1)
        from ui.navigator import Navigator
        Navigator.pop()

    def Test(self,e):
        for i in range(0,101):
            self.increaseProgressBar()
            time.sleep(0.05)

    def increaseProgressBar(self):
        val = self.progressBar.value
        if val == None: val = 0
        else: val += 0.01

        self.progressText.value = f"{int(val * 100)}% recognised"
        self.progressBar.value = val

        # When the progressBar Completed
        if val >= 1.0 :
            self.popUp.offset = transform.Offset(0, 0)
            self.closeButton.offset  = transform.Offset(0, 0)
            self.popUp.update()
            self.closeButton.update()
            # self.button.content.disabled = False
            # self.button.content.update()

        # Update UI ..................
        self.progressBar.update()
        self.progressText.update()

    def go_to_the_training_screen(self, e):
        # from ui.navigator import Navigator
        # ImageScreen.init()
        # Navigator.push(ImageScreen.instance)
        ...