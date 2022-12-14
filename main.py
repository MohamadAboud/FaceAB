from scripts.mind import MindThread
from ui.Home import main
from utils.check_file import Check


def initialize():
    Check.init()


if __name__ == '__main__':
    # mind = MindThread(title="AI")
    # mind.start()

    # -----------------------------

    initialize()
    main()
