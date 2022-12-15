import flet as ft
from flet import *

from scripts.scripts import TakeImages
from ui.routes.image_taking_screen import updateProgressBar
from ui.routes.routes import *
from ui.core.core import *
from utils.check_file import Check
from ui.widgets.widgets import getStartedButton,buttons


def Home(page: ft.Page):
    global getStartedButton,buttons

    page.title = kTitle
    page.bgcolor = backgroundColor
    page.theme_mode = ThemeMode.DARK
    page.window_width = WIDTH
    page.window_height = HEIGHT
    page.window_resizable = False
    page.window_maximizable = False
    page.padding = 0
    page.margin = 0
    # page.scroll = True
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Screens....................................
    splash = SplashScreen()
    imageScreen = ImageScreen()
    doneScreen = DoneScreen(additional_on_click= lambda e:print("2"))
    loadingScreen = LoadingScreen()


    def openImageScreen():
        page.controls = [imageScreen]
        page.update()
        TakeImages(updateProgressBar)

    # Start SplashScreen #########################################################################
    if Check.isFirstTime:
        # add getStartedButton to splash screen after checking the folders
        splash.content.controls[1].content.controls.insert(3, getStartedButton)

        def getstarted(e):
            getStartedButton.disabled = True
            getStartedButton.update()
            openImageScreen()

        # Get_Started button
        getStartedButton.on_click = getstarted
    else:
        # add [Start Button and Add Face Button] to splash screen after checking the folders
        splash.content.controls[1].content.controls.insert(3, buttons)

        # Start Button
        startButton = splash.content.controls[1].content.controls[3].controls[0].content
        # Add_Face Button
        addFaceButton =  splash.content.controls[1].content.controls[3].controls[1].content

        def start(e):
            print("Start")
        def addFace(e):
            startButton.disabled = True
            startButton.update()
            #--------------------
            addFaceButton.disabled = True
            addFaceButton.update()
            #--------------------
            openImageScreen()

        startButton.on_click = start
        addFaceButton.on_click = addFace

    # End   SplashScreen #########################################################################

    # Start ImageScreen #########################################################################
    def next(e):
        page.controls = [doneScreen]
        page.update()


    nextButton = imageScreen.content.controls[5].content

    nextButton.on_click = next
    # End   ImageScreen #########################################################################






    page.add(
        splash,
    )







def main():
    # Strat User Interface.......... in flutter

    ft.app(
        target=Home,
        assets_dir="assets"
    )