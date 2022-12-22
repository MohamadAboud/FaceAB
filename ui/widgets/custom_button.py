from flet import *
from typing import List
from ui.core.core import AppColor,AppSize


class CustomItem:
    def __init__(self,text,on_click=None):
        self.text = text
        self.on_click = on_click


def CustomButton(text: str, width=None, height=None , on_click=None , dColor = AppColor.primaryColor ,hColor = "#9d98ca",dTextColor = AppColor.secondaryColor,hTextColor = colors.BLACK,disabled=False,padding = None,expand = False, shape=RoundedRectangleBorder(radius=12),):


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
                shape=shape,
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



def CustomButtonDropDown(text: str,items:List[CustomItem], width=AppSize.width, height=AppSize.height , on_click=None , dColor = AppColor.primaryColor ,hColor = "#9d98ca" ,dTextColor = AppColor.secondaryColor,hTextColor = colors.BLACK,disabled=False):

    def onChange(e):
        val = drop.value
        for item in items:
            if item.text == val:
                print(item.text)
                if item.on_click is not None:
                    item.on_click()


    def on_hover(e):
        l = len(s.controls)
        allButton.bgcolor = hColor if l > 1 else dColor
        s.controls = [drop] if l > 1 else [drop,arrow]
        s.update()
        allButton.update()



    drop = Dropdown(
                height=height,
                width= width * 0.175,
                value="Card",
                content_padding=padding.only(left=5),
                alignment=alignment.center,
                border_radius=border_radius.only(
                    topRight=12,
                    bottomRight=12,
                ),
                border_color=hColor,
                color=hColor,
                opacity=0.01,
                focused_color=hColor,
                focused_bgcolor= hColor,
                disabled=disabled,
                on_change=onChange,
                options= [dropdown.Option(item.text) for item in items ]
            )

    arrow = Container(
                        alignment=alignment.center,
                        content=Icon(icons.ARROW_DROP_DOWN,color=dTextColor)
                    )

    s = Stack([drop,arrow])

    allButton = Container(
        height=height,
        width=width * 0.175,
        bgcolor=dColor,
        on_hover=on_hover,
        border_radius=border_radius.only(
            topRight=12,
            bottomRight=12,
        ),
        content=s
    )

    return Row(
        alignment= MainAxisAlignment.CENTER,
        vertical_alignment= CrossAxisAlignment.CENTER,
        spacing=0,
        controls=[
            CustomButton(
                text=text,
                width=width * 0.7,
                height=height,
                on_click=on_click,
                disabled=disabled,
                hColor=hColor,
                shape=RoundedRectangleBorder(
                    radius=border_radius.only(
                        topLeft=12,
                        bottomLeft=12,
                    )
                ),
            ),
            allButton
        ]
    )
