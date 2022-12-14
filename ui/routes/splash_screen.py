from flet import *
from ui.core.core import *
from ui.widgets.widgets import *
from utils.check_file import Check

img = Image(
        src= kSplachScreenImgPath,
        height= 250,
        width = 350,
        fit = ImageFit.CONTAIN
    )

txt1 = Container(
    padding= padding.only(top=25,left=12),
    content= Text(
        "Welcome",
        size=16,
        color= primaryColor,
        weight=FontWeight.BOLD,
    )
)

txt2 = Column([
    Row([
        Text("Face".upper(), size=25, weight=FontWeight.BOLD),
        Text("Recognition".upper(), size=25, color=primaryColor, weight=FontWeight.BOLD),

    ]),
    Text("application".upper(),size=25, weight = FontWeight.BOLD)
],spacing=0)

txt3 = Column([
    Row([
        Text(f"{kTitle[:3]}",opacity= 0.4),
        Text(f"{kTitle[3:]}",color=primaryColor),
        Text(" is a facial recognition app which",opacity= 0.4),

    ],spacing=0),
    Text("detects person from your training model",opacity= 0.4,text_align=TextAlign.START)
],spacing=0,opacity= 0.4)









def on_hover(e):
    signature.content.opacity = 1 if signature.content.opacity == 0.3 else 0.3

    signature.content.update()




signature = Container(
    padding=padding.only(top=10),
    alignment=alignment.center,
    width=350,
    content=Text(
        "Mohamad Aboud",
        size=12,
        color="#547e8b",
        opacity=0.3,
        tooltip="Developer:",
        italic=True,
    ),
    on_hover=on_hover
)



body = Container(
    padding=padding.symmetric(horizontal=20),
    content=Column([
        txt1,
        txt2,
        txt3,
        signature
    ])
)

def SplashScreen():
    return Container(
        height=HEIGHT,
        width=WIDTH,
        bgcolor=backgroundColor,
        content=Column([
            img,
            body
        ])
    )

