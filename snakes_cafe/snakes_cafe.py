from textwrap import dedent


def print_message(message):
    """Takes in a message and prtint it to console removing indentation

    Arguments:
        message {STR} -- Message to be printed
    """
    print(dedent(message))


def print_menu(menu):
    for category, items in menu.items():
        print('\n')
        print(dedent(category.title()))
        print('----------')
        for item in items.keys():
            print(item.title())


def start_orders():
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

    while True:
        user_input = input().lower()

        for items in menu.values():
            if user_input in items:
                items[user_input] += 1
                print(
                    f'** {items[user_input]} order of {user_input} have been added to your meal **')

        if user_input == 'quit':
            break


if __name__ == '__main__':
    start_orders()
