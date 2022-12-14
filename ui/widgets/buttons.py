from flet import *
from ui.core.values.colors import primaryColor,secondColor
from ui.core.values.size import *
from ui.widgets.custom_button import CustomButton

getStartedButton = CustomButton(
        text="Get Started",
        width = WIDTH * 0.9,
        height=40,
        padding=padding.only(top=35, bottom=25),

)

buttons = Column([
    CustomButton(
        text="Start",
        width=320,
        height=40,
        padding=padding.only(top=15)
    ),

    CustomButton(
        text="Add Face",
        width=320,
        height=40,
        dColor= secondColor,
        dTextColor=  primaryColor,
        padding=padding.only(top=5)
    )
])