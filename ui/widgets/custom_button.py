from flet import *
from typing import List

from flet.border import BorderSide
from flet.border_radius import BorderRadius

from ui.core.core import AppColor,AppSize


class CustomItem:
    def __init__(self,text,icon=None,on_click=None):
        self.text = text
        self.icon = icon
        self.on_click = on_click

class CustomButton(UserControl):

    def __init__(
            self,
            text,
            width = AppSize.width * .8,
            height = 50,
            on_click = None,
            disabled = False,
            padding = None,
            shape = RoundedRectangleBorder(radius=12),

            default_bgcolor= AppColor.primaryColor ,
            hover_bgcolor = AppColor.secondaryColor,

            default_textcolor=AppColor.backgroundColor,
            hover_textcolor=AppColor.negativeBackgroundColor,

            default_shape = RoundedRectangleBorder(radius=12),
            hover_shape = RoundedRectangleBorder(radius=30),

            shadow_color=AppColor.negativeBackgroundColor,
            icon = None,
            tooltip = None,

    ):
        super().__init__()

        self.text = text
        self.width = width
        self.height = height
        self.on_click = on_click
        self.disabled = disabled
        self.padding = padding
        self.shape = shape
        self.default_bgcolor = default_bgcolor
        self.hover_bgcolor = hover_bgcolor
        self.default_textcolor = default_textcolor
        self.hover_textcolor = hover_textcolor
        self.default_shape = default_shape
        self.hover_shape = hover_shape
        self.shadow_color = shadow_color
        self.icon = icon
        self.tooltip = tooltip

    def build(self):
        return ElevatedButton(
            text = self.text,
            height=self.height,
            width=self.width,
            disabled=self.disabled,
            on_click=self.on_click,
            icon=self.icon,
            tooltip=self.tooltip,
            style=ButtonStyle(
                animation_duration = 300,
                shadow_color=self.shadow_color,
                side=BorderSide(
                    width=1,
                    color=self.hover_bgcolor
                ),
                shape={
                    MaterialState.DEFAULT.value: self.default_shape,
                    MaterialState.FOCUSED.value: self.default_shape,

                    MaterialState.HOVERED.value: self.hover_shape,
                },
                elevation={
                    MaterialState.DEFAULT.value: 5,
                    MaterialState.FOCUSED.value: 5,

                    MaterialState.HOVERED.value: 15,

                    MaterialState.DISABLED.value: 0,
                },
                bgcolor={
                    MaterialState.DEFAULT.value: self.default_bgcolor,
                    MaterialState.FOCUSED.value: self.default_bgcolor,

                    MaterialState.HOVERED.value: self.hover_bgcolor,

                    MaterialState.DISABLED.value: "0xB3808080",
                },
                color={
                    MaterialState.DEFAULT.value: self.default_textcolor,
                    MaterialState.FOCUSED.value: self.default_textcolor,

                    MaterialState.HOVERED.value: self.hover_textcolor,

                    MaterialState.DISABLED.value: "0x80FFFFFF",
                },
            ),
        )


class CustomDropDownButton(UserControl):

    def __init__(
            self,
            text,
            items: List[CustomItem],
            width=AppSize.width * .8,
            height=50,
            on_click=None,
            disabled=False,
            padding=None,
            shape=RoundedRectangleBorder(radius=12),

            default_bgcolor=AppColor.primaryColor,
            hover_bgcolor=AppColor.secondaryColor,

            default_textcolor=AppColor.backgroundColor,
            hover_textcolor=AppColor.negativeBackgroundColor,

            default_shape=RoundedRectangleBorder(radius=BorderRadius(topLeft=12,bottomLeft=12,bottomRight=0,topRight=0)),
            hover_shape=RoundedRectangleBorder(radius=BorderRadius(topLeft=30,bottomLeft=30,bottomRight=0,topRight=0)),

            shadow_color=AppColor.negativeBackgroundColor,
            icon=None,
            tooltip=None,
    ):
        super().__init__()

        self.text = text
        self.items = items
        self.width = width
        self.height = height
        self.on_click = on_click
        self.disabled = disabled
        self.padding = padding
        self.shape = shape
        self.default_bgcolor = default_bgcolor
        self.hover_bgcolor = hover_bgcolor
        self.default_textcolor = default_textcolor
        self.hover_textcolor = hover_textcolor
        self.default_shape = default_shape
        self.hover_shape = hover_shape
        self.shadow_color = shadow_color
        self.icon = icon
        self.tooltip = tooltip

    def build(self):
        self.__buttonSide = self.__buttonSide()
        self.__dropdownSide = self.__dropdownSide()
        return Row([
            self.__buttonSide,
            Card(
                margin=1,
                elevation=5,
                content=self.__dropdownSide
            )
        ],spacing=0)


    def __buttonSide(self):
        buttonSide = CustomButton(
            text=self.text,
            width=self.width * .8,
            height=self.height ,
            on_click=self.on_click,
            disabled=self.disabled,
            padding=self.padding,
            shape=self.shape,
            default_bgcolor=self.default_bgcolor,
            hover_bgcolor=self.hover_bgcolor,
            default_textcolor=self.default_textcolor,
            hover_textcolor=self.hover_textcolor,
            default_shape=self.default_shape,
            hover_shape=self.hover_shape,
            shadow_color=self.shadow_color,
            icon=self.icon,
            tooltip=self.tooltip,
        )
        return buttonSide

    def __dropdownSide(self):
        dropdownSide = Container(
            bgcolor=self.default_bgcolor,
            height=self.height,
            width=self.width * .2,
            on_hover=self.__on_hover,
            border_radius=border_radius.horizontal(right=12),
            animate=animation.Animation(300,AnimationCurve.EASE_OUT_SINE),
            content=PopupMenuButton(
                content=Icon(icons.ARROW_DROP_DOWN,color=self.default_textcolor),
                tooltip=self.tooltip,

                items=[PopupMenuItem(text=item.text,icon=item.icon,on_click=item.on_click)  for item in self.items]
            )
        )

        return dropdownSide

    #################################| Events |#################################
    def __on_hover(self,_):
        self.__dropdownSide.bgcolor = self.hover_bgcolor if self.__dropdownSide.bgcolor == self.default_bgcolor else self.default_bgcolor
        self.__dropdownSide.border_radius = border_radius.horizontal(right=30) if self.__dropdownSide.border_radius == border_radius.horizontal(right=12) else border_radius.horizontal(right=12)

        self.__dropdownSide.content.content.color = self.hover_textcolor if self.__dropdownSide.content.content.color == self.default_textcolor else self.default_textcolor
        self.__dropdownSide.update()