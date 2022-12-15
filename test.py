import flet as ft
from flet import *


HIEGHT = 650
WIDTH = 350

primaryColor = "#80faff" # FF725E
secondColor  = "#1f4153"
backgroundColor = "#141c26"

def Padding(height,width=None):
    return Container(
        height= height,
        width = width
    )

class LoadingScreen(UserControl):

    def build(self):
        self.__page = AnimatedSwitcher(
        self._loading(),
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

        return self.__page

    def _done(self):

        return Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            height=HIEGHT,
            width= WIDTH,
            controls=[
                Container(
                    bgcolor= primaryColor ,
                    padding=padding.all(16),
                    shape= BoxShape.CIRCLE,
                    content= Icon(
                        icons.DONE,
                        color=secondColor,
                        scale= 1.8
                    )
                ),

                Padding(height=35),

                # Text ............
                Text("Successful!".upper(), weight=FontWeight.BOLD, size=16),

                # Text ............
                Text(
                    "Smile & blink your eyes,then move your\nhead slowly to complete",
                    text_align=TextAlign.CENTER,
                    opacity=0.5,  # ( 0 - 1 )
                ),

            ]
        )

    def _loading(self):

        self.progressBar = ProgressBar(
                    #value= 0.5 , # ( 0 - 1 )
                    width = WIDTH * .8,
                    bgcolor =  secondColor,
                    color= primaryColor,
                )

        return Column(
            horizontal_alignment = CrossAxisAlignment.CENTER,
            height=HIEGHT,
            width=WIDTH,
            controls=[
                Image(
                    src = "https://picsum.photos/id/250/200/300",
                    height= HIEGHT * .6,
                    width= WIDTH,
                    fit=ImageFit.COVER
                ),

                Padding(height=20),

                # Text............
                Text("Loading...".upper(),weight=FontWeight.BOLD,size=16),

                Padding(height=5),

                # ProgressBar .........
                self.progressBar,

                Padding(height=5),

                # Text............
                Text(
                    "Smile & blink your eyes,then move your\nhead slowly to complete",
                    text_align=TextAlign.CENTER,
                    opacity= 0.5, # ( 0 - 1 )
                ),

                TextButton(
                    "Start",
                    on_click=self.on_click,
                    height= 34 ,
                    style= ButtonStyle(
                        bgcolor= primaryColor,
                        color= secondColor
                    )
                )

            ]
        )
    def on_click(self,e):
        value = self.progressBar.value

        if value == None : value = 0

        for i in range(0,101):
            self.progressBar.value = i/100

            self.progressBar.update()
            time.sleep(0.01)

        self.__page.content = self._done()
        self.__page.update()



def main(page:Page):
    page.title = "Test"
    page.bgcolor = "#141c26"
    page.theme_mode = ThemeMode.DARK
    page.window_width = 350
    page.window_height = 650
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 0
    page.margin = 0
    # page.scroll = True
    # page.vertical_alignment = MainAxisAlignment.CENTER

    # create application instance
    loadingScreen = LoadingScreen()

    # add application's root control to the page
    page.add(loadingScreen)



app(
    target=main
)