def printItems(items: list):
    for index, i in enumerate(items):
        print(f"{index + 1}. {i}")


def get_user_input(prompt: str):
    for i in range(3):
        try:
            user_choice = input(prompt)
            return int(user_choice)
        except:
            print("Please Enter the option number")
