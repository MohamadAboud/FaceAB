from flet import *
from ui.routes.routes import *
from ui.core.core import *


class Home:

    instance = None
    @classmethod
    def init(cls,page:Page):
        Home.instance = cls(page)


    def __init__(self,page:Page):

        # Variable
        self.page = page
        self.stack = Stack([
            WelcomScreen.init(),
            # ImageScreen.init(),
            # TrainingScreen.init(),
        ])

        # Initialize --------------------
        self.page.title = AppString.name
        self.page.bgcolor = AppColor.backgroundColor
        self.page.theme_mode = ThemeMode.DARK
        self.page.window_width = AppSize.width
        self.page.window_height = AppSize.height
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.page.padding = 0
        self.page.margin = 0
        # self.page.scroll = True
        self.page.vertical_alignment = MainAxisAlignment.START


        self.page.add(
            self.stack
        )

        self.page.update()


    def showBanner(self,text,on_click=None):
        def close_banner(e):
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