from ui.Home import Home
from flet import *

class Navigator:

    @classmethod
    def push(cls,page):


        Home.instance.stack.controls.append(
            page
        )
        cls.update()
        print(f"Push")

    @classmethod
    def pop(cls):
        isNotRoot = len(Home.instance.stack.controls) != 1
        if isNotRoot:
            Home.instance.stack.controls.pop()
            cls.update()
            print(f"Pop")
        else:
            print("You can't pop")

    @classmethod
    def update(cls):
        Home.instance.stack.update()