from textwrap import dedent
import sys

WIDTH = 50
MENU = {'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
        'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
        'Desserts': ['Ice Cream', 'Cake', 'Pie'],
        'Drinks': ['Coffee', 'Tea', 'Blood of the Innocent'],
}


def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to my Snakes Cafe'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}

        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
        {'*' * WIDTH}
    '''))

    for k, v in MENU.items():
        print(k)
        print('-' * 10)
        for item in v:
            print(item)
        print()
    
    print('***********************************')
    print('** What would you like to order? **')
    print('***********************************')


def ask_question():
    return input()


def check_input(user_input, menu):
    if user_input.lower() == "quit":
        exit()
        return
    for k, v in menu.items():
        for item in v:
            if user_input.lower() == item.lower():
                return True
    else:
        return False


def run():
    greeting()
    order_counter = 0
    while True:
        order_list = []
        menu_order = ask_question()
        if check_input(menu_order,MENU) is True:
            order_list.append(menu_order)
            if menu_order in order_list:
                order_counter += 1
                print('{} order of {} have been added to your meal'.format(order_counter, menu_order))
                print()

        else:
            ask_question()
              

if __name__ == '__main__':
    run()