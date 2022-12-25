from math import pi
from flet import *

from ui.core.core import AppColor,Language
from utils.dev import Developer
from utils.utils import CameraSource


class DynamicTaps(UserControl):

    def __init__(self,height,width,content:Control):
        super().__init__()
        self.height = height
        self.width = width
        self.content = content
        self.__cap = None

        # Make size of content equals max size...
        self.content.height = height
        self.content.width = width

    def build(self):
        self.dynamicTaps = self.__DynamicTaps()
        self.dynamicDisplay = self.__DynamicDisplay()

        return Stack(
            height=self.height,
            width=self.width,

            controls=[
                self.content,

                Container(
                    top=35,
                    height=self.height * .8,
                    width=self.width * 0.8,
                    content=Column(
                        controls=[
                            self.dynamicTaps,
                            self.dynamicDisplay,
                        ]
                    )
                )
            ]
        )

    def __DynamicTaps(self):
        self.__iconSettings = self.__IconSettingsTip()
        self.__iconLanguage = self.__IconLanguageTip()
        self.__iconCam = self.__IconCamTip()

        return Container(
            height=50,
            width= self.width * .52,
            bgcolor=AppColor.negativeBackgroundColor,
            offset=transform.Offset(-0.78, 0),
            animate_offset=animation.Animation(1000),
            on_hover=self.on_hover,
            border_radius=border_radius.only(
                topRight=35,
                bottomRight=35,
            ),
            content=Row(
                alignment=MainAxisAlignment.END,

                controls=[
                    Container(width=1),  # Padding

                    self.__PersonTip(),

                    Container(width=1),  # Padding

                    self.__iconCam,

                    Container(width=1),  # Padding

                    self.__iconLanguage,

                    Container(width=1),  # Padding

                    self.__iconSettings,

                    Container(width=0.1),  # Padding
                ]
            )
            )

    def __DynamicDisplay(self):
        return Card(
            margin=margin.only(left=self.width * 0.1),
            height=self.height * 0.5,
            width=self.width * 0.5,
            animate_opacity=300,
            opacity=0,
            elevation=10,
            content=Container(
                alignment=alignment.center,
                border_radius=border_radius.all(12),
                image_fit=ImageFit.COVER,
                bgcolor=AppColor.backgroundColor
            )
        )

    ###############################| Tips |###############################

    def __IconSettingsTip(self):
        return Container(
            rotate=transform.Rotate(0, alignment=alignment.center),
            animate_rotation=animation.Animation(300, AnimationCurve.BOUNCE_OUT),
            content=Icon(icons.SETTINGS,color=AppColor.backgroundColor),
            on_click=self.__settingsClick,
            tooltip="Settings",
        )

    def __IconLanguageTip(self):
        return Container(
                padding=padding.all(1),
                alignment=alignment.center,
                height=25,
                width=25,
                shape=BoxShape.CIRCLE,
                ink=True,
                on_click=self.__languageClick,
                tooltip="Language",
                content=AnimatedSwitcher(
                    Text(
                        Language.currentLanguageCode,
                        color=AppColor.backgroundColor,
                        weight=FontWeight.BOLD,
                    ),
                    transition=AnimatedSwitcherTransition.SCALE,
                    duration=500,
                    reverse_duration=100,
                    switch_in_curve=AnimationCurve.BOUNCE_OUT,
                    switch_out_curve=AnimationCurve.BOUNCE_IN
                ),
            )

    def __IconCamTip(self):
        return Container(
            shape=BoxShape.CIRCLE,
            height=25,
            width=25,
            on_click=self.__camClick,
            on_long_press= self.__camLongPress,
            on_hover=self.__camHover,
            tooltip=f"Camera",
            content=Icon(icons.VIDEOCAM,color=AppColor.backgroundColor)
        )

    def __PersonTip(self):
        return Container(
            shape=BoxShape.CIRCLE,
            height=25,
            width=25,
            tooltip="Mohamad Aboud",
            content=Icon(icons.PERSON, color=AppColor.backgroundColor)
        )

    ###############################| Events |###############################

    def on_hover(self,e):
        self.dynamicTaps.offset = transform.Offset(0, 0) if self.dynamicTaps.offset == transform.Offset(-0.78, 0) else transform.Offset(-0.78, 0)
        self.__iconSettings.rotate.angle += (pi / 2)*2
        self.__iconSettings.update()
        self.dynamicTaps.update()

    def __settingsClick(self,e):
        Developer.log("Settings Cliked", mode='info')

    def __languageClick(self, e):
        Language.changeLanguage()
        # self.__iconLanguage.content.content = Text(Language.currentLanguageCode, color=AppColor.backgroundColor,
        #                                            weight=FontWeight.BOLD, )
        # self.__iconLanguage.content.update()
        # Developer.log("Language Cliked",mode='info')

    def __camClick(self,e):
        CameraSource.changeCamera(src=CameraSource.camNumber +1)
        self.__camHover('')
        self.__camHover('')

    def __camLongPress(self,e):
        CameraSource.changeCamera(src=0)
        self.__camHover('')
        self.__camHover('')


    def __camHover(self, e):
        self.dynamicDisplay.opacity = 0 if self.dynamicDisplay.opacity == 1 else 1
        self.dynamicDisplay.update()
        if self.__cap is not None :
            self.__cap = None
        else:
            self.dynamicDisplay.content.image_src = '/images/cam_loading.gif'
            self.dynamicDisplay.content.update()
            self.__openCamera()


    def __openCamera(self):
        import cv2
        import base64

        Developer.log(f"Camera Source: {CameraSource.camNumber}", mode='info')
        self.__cap = cv2.VideoCapture(CameraSource.camNumber)


        while  True:
            try:
                ret, image = self.__cap.read()
                if not ret:
                    break

                _, encode_image = cv2.imencode('.jpg', image)
                image_bytes = encode_image.tobytes()
                base64_image = base64.b64encode(image_bytes).decode('utf-8')

                self.dynamicDisplay.content.image_src_base64 = base64_image
                self.dynamicDisplay.content.update()
            except:
                self.dynamicDisplay.content.image_src_base64 = None
                self.dynamicDisplay.content.update()
                break