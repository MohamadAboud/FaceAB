import flet as ft
from flet import *

def CustomLoadingButton(text,padding=None,maxheight=40,minheight=50,maxwidth=200,minwidth = 50,on_click=None):

    def startAnimation(e):
        global check
        btn.width = minwidth if btn.width == maxwidth else maxwidth
        btn.height = minheight if btn.height == maxheight else maxheight
        btn.border_radius = border_radius.all(12) if btn.border_radius == border_radius.all(50) else border_radius.all(50)

        if on_click:
            on_click()

        btn.update()



    btn = Container(
        padding = padding if padding else ft.padding.symmetric(horizontal=8),
        alignment=alignment.center,
        width=maxwidth,
        height=maxheight,
        border_radius=border_radius.all(12),
        bgcolor = "red",
        animate = animation.Animation(1000, AnimationCurve.EASE_OUT),
        on_click = startAnimation,

        content= Text(text)
    )

    return btn


def CustomAlart():
    w,h = 150,200

    dlg = ft.AlertDialog(
        title = Container(
            height = h,
            width = w,
            padding = ft.padding.all(10),
            bgcolor = "green",
        ),
        content=Container(
            height = h,
            width = w,
            padding = ft.padding.all(10),
            bgcolor = "red",
        ),

    )

    return dlg



def Home(page: Page):
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
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def open_dlg(e):
        dlg = CustomAlart()
        page.dialog = dlg
        dlg.open = True
        page.update()

    btn = ElevatedButton(
        text="Open Diloag",
        on_click = open_dlg
    )

    page.add(
        btn
    )





app(
    target=Home,
)