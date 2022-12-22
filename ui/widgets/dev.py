from flet import *

def Signature(*args):

    def on_hover(e):
        sig.opacity = 1 if sig.opacity == 0.4 else 0.4
        sig.scale = 1.5 if sig.opacity == 1 else 1
        sig.content.weight = FontWeight.BOLD if sig.content.weight == FontWeight.W_400 else FontWeight.W_400

        sig.update()

    sig = Container(
        alignment=alignment.center,
        width=350,
        opacity= 0.4,
        animate_opacity=300,
        animate_scale=animation.Animation(600,AnimationCurve.BOUNCE_OUT),
        scale=1,
        content=Text(
            "".join([chr(num) for num in args]),
            color="#547e8b",
            tooltip="Developer:",
            weight=FontWeight.W_400,
            italic=True,
        ),
        on_hover= on_hover
    )
    return sig