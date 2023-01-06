from flet import *
from ui.routes.routes import *
from ui.core.core import *


class Home:
    instance = None

    @classmethod
    def init(cls, page: Page):
        Home.instance = cls(page)

    def __init__(self, page: Page):

        # Variable
        self.page = page
        # Initialize --------------------
        self.page.title = AppString.name
        self.page.bgcolor = AppColor.backgroundColor
        self.page.theme_mode = AppColor.themeMode
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.page.padding = 0
        self.page.margin = 0
        self.page.vertical_alignment = MainAxisAlignment.START
        # for splash screen ....
        page.window_width = AppSize.width * 1.1
        page.window_height = AppSize.height * .35
        page.window_title_bar_hidden = True
        page.window_bgcolor = colors.TRANSPARENT
        page.bgcolor = colors.TRANSPARENT
        page.window_frameless = True
        page.window_center()

        # body --------------------------------
        self.stack = Stack([
            SplashScreen(
                height=self.page.height,
                width=self.page.width,
            )
        ])

        self.page.add(self.stack)
        self.__loadFiles()

    def __initialize(self):
        from utils.check_file import Check
        Check.init()

        try:
            from scripts.training_model import TrainingModel
            TrainingModel.load()
        except:
            ...

    def __loadFiles(self):
        self.page.update()

        # await for loading files .....
        self.__initialize()

        # update window info ...
        self.page.window_width = AppSize.width
        self.page.window_height = AppSize.height
        self.page.window_title_bar_hidden = False
        self.page.bgcolor = AppColor.backgroundColor
        self.page.window_center()

        # push Welcome Screen....
        self.stack.controls = [WelcomScreen.init()]
        self.stack.update()

    def showBanner(self, text, on_click=None):
        def close_banner(_):
            self.page.banner.open = False
            self.page.update()

            if on_click: on_click()

        self.page.banner = Banner(
            bgcolor=colors.AMBER_100,
            leading=Icon(icons.ERROR, color=colors.RED, size=40),
            content=Text(
                text,
                color="black"
            ),
            actions=[
                TextButton("Retry", on_click=close_banner),
                TextButton("Cancel", on_click=close_banner),
            ],
        )
        self.page.banner.open = True
        self.page.update()
