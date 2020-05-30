from textwrap import dedent


def print_message(message):
    """Takes in a message and prtint it to console removing indentation

    Arguments:
        message {STR} -- Message to be printed
    """
    print(dedent(message))


def print_menu(menu):
    """For a given menu prints to console categories and  items within each category

    Arguments:
        menu {DICT} -- Menu dictionary
    """
    for category, items in menu.items():
        print('\n')
        print(dedent(category.title()))
        print('----------')
        for item in items.keys():
            print(item.title())


def take_order():
    INTRO = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """

    OUTRO = """
    ***********************************
    ** What would you like to order? **
    ***********************************
    """

    menu = {
        'appetizers': {
            'wings': 0,
            'cookies': 0,
            'spring rolls': 0
        },
        'entrees': {
            'salmon': 0,
            'steak': 0,
            'meat tornado': 0,
            'a literal garden': 0
        },
        'desserts': {
            'ice cream': 0,
            'cake': 0,
            'pie': 0
        },
        'drinks': {
            'coffee': 0,
            'tea': 0,
            'unicorn tears': 0
        },
    }

    print_message(INTRO)
    print_menu(menu)
    print_message(OUTRO)

    # Take user order
    while True:
        user_input = input().lower()
        incorrect_entry = True

        for items in menu.values():
            if user_input in items:
                incorrect_entry = False
                items[user_input] += 1
                print(
                    f'** {items[user_input]} order of {user_input} have been added to your meal **')

        if incorrect_entry:
            print(
                f'Sorry, there\'s no {user_input} item on our menu, please try again')

        if user_input == 'quit':
            break


if __name__ == '__main__':
    take_order()
