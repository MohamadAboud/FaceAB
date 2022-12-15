from flet import *

from ui.core.core import *

header = Container(
    height= HEIGHT * 0.6,
    width=WIDTH,
    bgcolor="green",
    image_src= "https://picsum.photos/seed/picsum/200/300",
    image_fit= ImageFit.COVER,
)

body = Container(
    padding=padding.all(20),
    content=Column([
    Container(),
    Text("Loading..."),
    ProgressBar(
        width= WIDTH * 0.8,
        color= primaryColor,
        bgcolor=secondColor,
    ),
    Text("Smile & blink your eyes,then move your\nhead slowly to complete the process",text_align=TextAlign.CENTER)
],
    alignment=MainAxisAlignment.CENTER,
    horizontal_alignment=CrossAxisAlignment.CENTER,
    spacing= 30,
    expand=True
)
)

def LoadingScreen():
    return Container(
        height=HEIGHT,
        width=WIDTH,
        bgcolor=backgroundColor,
        content=Column([
            header,
            body
        ])
    )