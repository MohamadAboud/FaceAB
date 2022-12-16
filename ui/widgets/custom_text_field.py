from flet import *

from ui.core.core import primaryColor,backgroundColor


def CustomTextField(title:str,error_text="",hint_text=None,icons=None,on_submit=None,on_change=None):
    return Column([
            Text(
                title,
                color="black"
            ),
            TextField(
                hint_text=hint_text,
                hint_style=TextStyle(
                    color="black",
                ),
                bgcolor="red",
                border_radius=border_radius.all(8),
                border_color="#808080",
                focused_border_color=primaryColor,
                content_padding=padding.only(left=8, bottom=5),
                text_style=TextStyle(
                    color="black",
                ),
                max_length=13,
                prefix_icon=icons,
                error_text=error_text,
                error_style= TextStyle(
                    color="red"
                ),
                on_submit=on_submit,
                on_change=on_change
            )
        ])