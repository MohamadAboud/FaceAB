from ui.Home import Home
from utils.dev import Developer


class Navigator:

    @classmethod
    def push(cls,page):
        Home.instance.stack.controls.append(
            page
        )
        cls.update()
        Developer.log(f"Push",mode='info')

    @classmethod
    def pop(cls):
        isNotRoot = len(Home.instance.stack.controls) != 1
        if isNotRoot:
            Home.instance.stack.controls.pop()
            cls.update()
            Developer.log("Pop", mode='info')
        else:
            Developer.log("You can't pop", mode='warning')

    @classmethod
    def update(cls):
        Home.instance.stack.update()

    @classmethod
    def pushReplacement(cls,page):
        Home.instance.stack.controls.pop()
        Home.instance.stack.controls.append(page)

        cls.update()
        Developer.log("pushReplacement", mode='info')

    @classmethod
    def popAllAndPush(cls,page):
        Home.instance.stack.controls = [page]
        cls.update()
        Developer.log("Pop All And Push", mode='info')

    @classmethod
    def restart(cls):
        from ui.routes.welcom_screen import WelcomScreen

        Home.instance.stack.controls = [WelcomScreen.init()]
        cls.update()
        Developer.log("Restart...", mode='info')