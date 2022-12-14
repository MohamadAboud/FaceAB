
from flet import *

from ui.core.core import primaryColor,secondColor


def CustomButton(text: str, width=None, height=None , on_click=None , dColor = primaryColor ,hColor = colors.WHITE,dTextColor = secondColor,hTextColor = colors.BLACK,disabled=False,padding = None,expand = False):


    button = Container(
        padding=padding,
        alignment=alignment.center,
        expand=expand,
        content=ElevatedButton(
            text=text,
            width=width,
            height=height,
            disabled=disabled,
            on_click=on_click,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12),
                bgcolor={
                    "hovered": hColor,
                    "focused": dColor,
                    "": dColor,
                    "disabled":"0xB3808080"
                },
                color={
                    "hovered": hTextColor,
                    "focused": dTextColor,
                    "": dTextColor,
                    "disabled": "0x80FFFFFF",
                },
            ),
        )
    )

    return button