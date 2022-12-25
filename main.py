from ui.Home import *
from flet import app as runApp




if __name__ == '__main__':
    # -----------------------------
    runApp(
        target=Home.init,
        assets_dir="assets"
    )