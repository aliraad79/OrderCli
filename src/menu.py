from utils import printItems, get_user_input
from enum import Enum


class MenuItem(Enum):
    Pela = 0
    Dizi = 1
    Chicken = 2
    Steak = 3
    Pizaa = 4

    def get_available_items():
        return [
            MenuItem.Pela.name,
            MenuItem.Dizi.name,
            MenuItem.Chicken.name,
            MenuItem.Steak.name,
        ]


def go_to_menu() -> MenuItem:
    printItems(MenuItem.get_available_items())
    choice = get_user_input("Which one do you want? : ")
    user_food = MenuItem(choice)

    print(f"You Choose {user_food.name}")

    return user_food
def exit() -> MenuItem:
    printItems("exit")
    return