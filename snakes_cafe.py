from textwrap import dedent

WIDTH = 50
MENU = [{'Appetizers': [{'items':'Wings', 'price' : 20.99},
                        {'items':'Cookies', 'price' : 1.50},
                        {'items':'Spring Rolls', 'price' : 2.00},
                        {'items':'Armadillo eggs', 'price' : 4.35},
                        {'items':'Jalapeno Poppers', 'price' : 10.50},
                        {'items':'Fries', 'price' : 2.00}]},
         {'Entrees': [{'items':'Salmon', 'price' : 20.99},
                        {'items':'Steak', 'price' : 1.50},
                        {'items':'Meat Tornado', 'price' : 2.00},
                        {'items':'A Literal Garden', 'price' : 4.35},
                        {'items':'Surf and Turf', 'price' : 10.50},
                        {'items':'Ribeye', 'price' : 2.00}
                      ]},
        {'Desserts': [{'items':'Ice cream', 'price' : 1.99},
                        {'items':'Cake', 'price' : 2.50},
                        {'items':'Pie', 'price' : 2.99},
                        {'items':'Cupcake', 'price': 3.35},
                        {'items':'Macaroon', 'price': 5.50},
                        {'items':'Coconut', 'price' : 1.00}
                      ]},
        {'Drinks': [{'items':'Coffee', 'price' : 20.99},
                        {'items':'Tea', 'price' : 1.50},
                        {'items':'Blood of the Innocent', 'price' : 2.00},
                        {'items':'Whiskey', 'price' : 4.35},
                        {'items':'Vodka', 'price' : 10.50},
                        {'items':'Sparkling Wine', 'price' : 2.00}
                      ]},
        {'Sides': [{'items':'Veggies', 'price' : 5.99},
                        {'items':'Fries', 'price' : 2.50},
                        {'items':'Potato', 'price' : 2.00},
                        {'items':'Garlic', 'price' : 9.35},
                        {'items':'Biscuits', 'price' : 6.50},
                        {'items':'Mashed Tots', 'price' : 7.00}
                      ]},
        ]


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
    for item in MENU:
        for k, v in item.items():
            print(k)
            print('-' * 10)
            for food_items in v:
                print(food_items.get('items'))
            print()

    print('*' * 35)
    print('** What would you like to order? **')
    print('*' * 35)


def ask_question():
    return input()


def check_input(user_input):
    """validates user input, otherwise exits program
    """
    if user_input.lower() == "quit":
        exit()
        return
    for food in MENU:
        for k, v in food.items():
            for food_items in v:
                if user_input.lower() == food_items.get('items').lower():
                    return True
    else:
        return False


def create_order(user_input, order_items):
    if user_input not in order_items.keys():
        order_items[user_input] = 1
    else:
        order_items[user_input] += 1
    return order_items


def run():
    greeting()
    order_list = {}

    while True:
        menu_order = ask_question()

        if menu_order == 'order':
            #create print_order function
            pass
        elif menu_order == 'menu':
            greeting()
        elif 'remove' in menu_order:
            #remove single item from list
            pass
        elif check_input(menu_order) is True:
            order_list = create_order(menu_order,order_list)
            print('{} order of {} have been added to the meal'.format(order_list[menu_order],menu_order))
        else:
            ask_question()


if __name__ == '__main__':
    run()