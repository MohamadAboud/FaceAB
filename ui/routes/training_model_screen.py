from flet import *
from ui.core.core import *



class TrainingScreen(UserControl):

    instance = None

    @classmethod
    def init(cls):
        TrainingScreen.instance = cls()
        return TrainingScreen.instance

    def __init__(self):
        super().__init__()

        self.__selectedIndex = 0
        self.__maxDots = 5
        self._createDots()

    def __call__(self, *args, **kwargs):
        # Run [Training Model] scripts...
        try:
            from scripts.training_model import TrainingModel
            TrainingModel.train()
        except Exception as err:
            from utils.dev import Developer
            Developer.log(f"error : {err}")
            # from ui.Home import Home
            # from ui.routes.welcom_screen import WelcomScreen
            # from ui.navigator import Navigator
            # Home.instance.showBanner(
            #     text="Oops, there were some errors while trying to train the model. What would you like me to do?",
            #     on_click=lambda: Navigator.popAllAndPush(WelcomScreen.instance)
            # )


    @property
    def selectedIndex(self):
        return self.__selectedIndex

    @selectedIndex.setter
    def selectedIndex(self, value):
        if value < self.__maxDots:
            self.__selectedIndex = value
        else:
            self.__selectedIndex = 0

    def build(self):
        self.__page = AnimatedSwitcher(
            self._loading(),
            transition=AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=AnimationCurve.BOUNCE_OUT,
            switch_out_curve=AnimationCurve.BOUNCE_IN,
        )

        return self.__page

    def _done(self):

        return Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            height=AppSize.height,
            width= AppSize.width,
            controls=[
                Container(
                    bgcolor=AppColor.primaryColor ,
                    padding=padding.all(16),
                    shape= BoxShape.CIRCLE,
                    content= Icon(
                        icons.DONE,
                        color=AppColor.secondaryColor,
                        scale= 1.8
                    )
                ),

                Container(height=35), # Padding

                # Text ............
                Text(f"{AppString.trainingscreen.text1}".upper(), weight=FontWeight.BOLD, size=16),

                # Text ............
                Text(
                    AppString.trainingscreen.text2,
                    text_align=TextAlign.CENTER,
                    opacity=0.5,  # ( 0 - 1 )
                ),

            ]
        )

    def _loading(self):

        self.progressText = Text(f"{AppString.trainingscreen.progressText1}...".upper(),weight=FontWeight.BOLD,size=16)

        self.progressBar = ProgressBar(
                    #value= 0.5 , # ( 0 - 1 )
                    width = AppSize.width * .8,
                    bgcolor = AppColor.secondaryColor,
                    color= AppColor.primaryColor,
                )


        return Column(
            horizontal_alignment = CrossAxisAlignment.CENTER,
            height=AppSize.height,
            width=AppSize.width,
            controls=[
                Image(
                    src=AppString.trainingscreen.img,
                    height=AppSize.height * .6,
                    width=AppSize.width,
                    fit=ImageFit.COVER,
                ),

                Container(height=20), # Padding

                # Text............
                self.progressText,

                Container(height=5), # Padding

                # ProgressBar .........
                self.progressBar,

                Container(height=5), # Padding

                # Text............
                Text(
                    AppString.trainingscreen.subText,
                    text_align=TextAlign.CENTER,
                    opacity= 0.5, # ( 0 - 1 )
                ),

                Container(height=20), # Padding

                self._dotsIndicator,
            ]
        )

    def _createDots(self):
        self._dotsIndicator = AnimatedSwitcher(
            transition=AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=AnimationCurve.BOUNCE_OUT,
            switch_out_curve=AnimationCurve.BOUNCE_IN,
            opacity= 0.7,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[self._dot(idx) for idx in range(self.__maxDots)]
            )
        )
        return self._dotsIndicator

    def _dot(self,index):
        return Container(
            height=8,
            width=8,
            bgcolor=AppColor.primaryColor if index == self.selectedIndex else AppColor.secondaryColor,
            shape=BoxShape.CIRCLE
        )

    def _switchScreen(self):
        self.__page.content = self._done()
        self.__page.update()

        # await ...
        from ui.navigator import Navigator
        from ui.routes.welcom_screen import WelcomScreen

        # update isFirstTime ...
        from utils.check_file import Check
        Check.init()

        time.sleep(3)
        Navigator.popAllAndPush(WelcomScreen.init())


    # def Test1(self,e):
    #     for i in range(1,101):
    #         self.increaseProgressBar(1)
    #         time.sleep(0.04)
    #
    # def Test2(self,e):
    #     val = self.selectedIndex + 1
    #     self.updateDots(selected=val)

    def updateDots(self,selected):
        self.selectedIndex = selected
        self._dotsIndicator.content = Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[self._dot(idx) for idx in range(self.__maxDots)]
            )
        self._dotsIndicator.update()

    def increaseProgressBar(self,value):
        val = self.progressBar.value

        if val == None: val = 0

        val += value/100

        self.progressText.value = f"{round(val*100,2)}% {AppString.trainingscreen.progressText1}".upper()
        self.progressBar.value = val

        # When the progressBar Completed
        if val >= 1.0:
            ...
        else:
            # Update UI ..................
            self.progressText.update()
            self.progressBar.update()

    def make_sure_to_finish(self):
        self._switchScreen()