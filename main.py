from ui.Home import *
from flet import app as runApp
from utils.utils import Developer

if __name__ == '__main__':
    # In the test case, you can set the isTesting to True
    Developer.isTesting = True  # isTesting is bool [ True, False ]
    # Start the UI -----------------------------
    runApp(
        target=Home.init,
        assets_dir="assets"
    )
