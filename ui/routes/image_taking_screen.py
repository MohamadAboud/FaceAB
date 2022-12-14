from flet import *

from ui.core.core import HEIGHT,WIDTH,backgroundColor,primaryColor,secondColor
from ui.widgets.widgets import CustomButton

def updateProgressBar():
    global txt1,progressBar,button
    value = progressBar.controls[0].value + 0.01

    if value > 1.0:
        value = 1.0
        nextButton.content.disabled = False
        nextButton.content.update()

    txt1.content.value = f"{int(value * 100)}% recognised"
    txt1.update()
    progressBar.controls[0].value = value
    progressBar.controls[0].update()

header = Container(
    height= HEIGHT * 0.55,
    width= WIDTH,
    bgcolor= secondColor,
    border_radius= border_radius.only(bottomLeft=35,bottomRight=35),
    image_src= "images/loading.gif",
    image_fit=ImageFit.COVER,
)

txt1 = Container(
    alignment=alignment.center,
    padding=padding.symmetric(vertical=10),
    content=Text(f"0% recognised",weight=FontWeight.W_500)
)

progressBar = Row([
    ProgressBar(
        value=0,
        width= WIDTH * 0.8,
        color= primaryColor,
        bgcolor=secondColor,
    )
],alignment=MainAxisAlignment.CENTER)

txt2 = Container(
    alignment=alignment.center,
    padding=padding.only(top=10,bottom=5),
    content= Text(
        "Verification Process",
        size=25,
        weight = FontWeight.BOLD,
    )
)

txt3 = Container(
    alignment=alignment.center,
    padding=padding.only(left=25,right=25),

    content= Text(
        "Smile & blink your eyes,then move your\nhead slowly to complete the process",
        opacity= 0.7,
        text_align=TextAlign.CENTER
    )
)

nextButton = CustomButton(
    text="Next",
    width=WIDTH * 0.8,
    height=35,
    padding= padding.only(top=8),
    disabled=True,
)

def ImageScreen():
    return Container(
        height = HEIGHT,
        width = WIDTH,
        bgcolor= backgroundColor,
        content= Column([
            header,
            txt1,
            progressBar,
            txt2,txt3,
            nextButton,
        ])
    )