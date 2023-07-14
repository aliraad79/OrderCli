from utils import *


def printHelp():
    print(
        "Hi Welcome to our order sysetm.\nPlease Choose the option you want to continue with."
    )


if __name__ == "__main__":
    main_menu_options = ["See Menu", "Place Order", "Check Order"]
    printHelp()
    printItems(main_menu_options)
