from utils.utils import ChangeNameFolder,DeleteFolder
from ui.widgets.widgets import *
from scripts.data import Data
from ui.core.core import *

saveImagePath = "./data/users"  # + [ user folder -> user-00000 ]

def doneClicked(e):
    nameField.content.error_text = ""
    name = nameField.content.value

    if len(name) == 0:
        nameField.content.error_text = "Name is required"
        nameField.content.update()
        return

    nameField.content.update()
    ChangeNameFolder(
        oldpath= f"{saveImagePath}/user-{Data.UID}",
        newpath= f"{saveImagePath}/{name}",
    )
    print("1")



def deleteClicked(e):
    DeleteFolder(f"{saveImagePath}/user-{Data.UID}")

def on_change(e):
    text = nameField.content.value

    if len(text) != 0:
        nameField.content.error_text = ""

    nameField.content.update()


img = Container(
    height= HEIGHT * 0.35,
    width= WIDTH,
    padding= padding.all(35),
    content= Image(
        src = "images/done.gif",
    )
)

txt1 = Container(
    alignment=alignment.center,
    padding=padding.symmetric(vertical=10),
    content=Text(f"100% recognised",weight=FontWeight.W_500)
)

txt2 = Column([
    Container(
        padding=padding.only(top=35),
        alignment=alignment.center,
        content=Text("Face captured",size= 18, weight=FontWeight.BOLD)
    ),
    Row([
        Text("successfully",color=primaryColor,size= 18, weight=FontWeight.BOLD),
        Text(",enter name",size= 18, weight=FontWeight.BOLD)
    ],alignment=MainAxisAlignment.CENTER)
])

divider = Row([
    Container(
        height= 5,
        width= WIDTH * 0.75,
        border_radius= border_radius.all(10),
        gradient= LinearGradient(
            end=alignment.center_left,
            begin= alignment.center_right,
            colors=[
                primaryColor,
                secondColor,
            ]
        )
    )
],alignment=MainAxisAlignment.CENTER)


nameField = Container(
    padding=padding.only(top=25),
    alignment=alignment.center,
    height= HEIGHT * 0.13,
    content=TextField(
        hint_text="Enetr your name ",
        width= WIDTH * 0.75,
        border_radius=border_radius.all(8),
        content_padding=padding.only(top=5,left=8),
        prefix_icon= icons.PERSON,
        border_color= secondColor,
        focused_border_color= primaryColor,
        max_length= 13,
        autofocus= True,
        error_text= "",
        on_change = on_change
    )
)

buttons = Container(
    alignment=alignment.center,
    height= HEIGHT * 0.13,
    content=Row([
        CustomButton(
            text="Delete",
            dColor = secondColor,
            width = WIDTH * 0.36,
            dTextColor=primaryColor,
            on_click= deleteClicked
        ),

        Container(width=10),

        CustomButton(
            text="Done",
            dColor = primaryColor,
            width = WIDTH * 0.36,
            on_click= doneClicked
        )
    ],alignment= MainAxisAlignment.SPACE_AROUND,width=WIDTH *0.75)
)

def DoneScreen(additional_on_click):

    page = Container(
        height=HEIGHT,
        width=WIDTH,
        bgcolor=backgroundColor,
        content=Column([
            img,
            txt1,
            divider,

            txt2,
            nameField,
            buttons
        ]))

    def test(e):
        doneClicked(e)
        additional_on_click(e)

    buttons.content.controls[2].on_click = test

    return page

