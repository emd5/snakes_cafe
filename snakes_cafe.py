from textwrap import dedent
from uuid import uuid4


WIDTH = 50
TAX = .106
TOTALTAX = 1.10
MENU = {'Appetizers': [{ 'Wings': 20.99},
                        {'Cookies': 1.50},
                        {'Spring Rolls': 2.00},
                        {'Armadillo eggs': 4.35},
                        {'Jalapeno Poppers': 10.50},
                        {'Fries': 2.00}],
        'Entrees': [{'Salmon': 20.99},
                     {'Steak': 1.50},
                     {'Meat Tornado': 2.00},
                     {'A Literal Garden': 4.35},
                     {'Surf and Turf': 10.50},
                     {'Ribeye': 2.00}
                     ],
        'Desserts': [{'Ice cream': 1.99},
                      {'Cake': 2.50},
                      {'Pie': 2.99},
                      {'Cupcake': 3.35},
                      {'Macaroon': 5.50},
                      {'Coconut': 1.00}
                      ],
        'Drinks': [{'Coffee': 20.99},
                    {'Tea': 1.50},
                    {'Blood of the Innocent': 2.00},
                    {'Whiskey': 4.35},
                    {'Vodka': 10.50},
                    {'Sparkling Wine': 2.00}
                    ],
        'Sides': [{'Veggies': 5.99},
                   {'Fries': 2.50},
                   {'Potato': 2.00},
                   {'Garlic': 9.35},
                   {'Biscuits': 6.50},
                   {'Mashed Tots': 7.00}
                    ],
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
    print_menu()


def print_menu():
    for k,v in MENU.items():
        print(k)
        print('-' * 10)
        for item in v:
            for key in item.keys():
                print(key)
                # print(food_items.get('price'))
        print()
    print('*' * 35)
    print('** What would you like to order? **')
    print('*' * 35)


def ask_question():
    return input()


def check_input(user_input):
    """Validates user input, otherwise exits program
    """
    if user_input.lower() == "quit":
        exit()
        return
    for k, v in MENU.items():
        for item in v:
            for key in item.keys():
                if user_input.lower() == key.lower():
                    return True
    else:
        return False


def find_item_price(user_input):
    for key, value in MENU.items():
        for price in value:
            for k, v in price.items():
                if user_input == k.lower():
                    return(v)


def create_order(user_input, order_items):
    if user_input not in order_items.keys():
        order_items[user_input] = 1
    else:
        order_items[user_input] += 1
    return order_items


def find_item_price(user_input):
    for key, value in MENU.items():
        for price in value:
            for k, v in price.items():
                if user_input == k.lower():
                    return(v)


def calculate_item_price(order_dict):
    receipt = []
    for k, v in order_dict.items():
        price = find_item_price(k)
        count = order_dict[k]
        total = price * count
        receipt_dict = {'item': k, 'count': v, 'total': total}
        receipt.append(receipt_dict)
    return receipt


def calculate_total_price(receipt_dict):
    sum_total = 0
    for price in receipt_dict:
       sum_total += price['total']
    return sum_total


def print_receipt(order_list):
    total = calculate_item_price(order_list)
    total_price = calculate_total_price(total)
    print('*' * 50)
    print('The Snakes Cafe')
    print('"Eatability Counts"')
    print()
    print('Order: ' + str(uuid4()))  # UUID
    print('=' * 50)
    for items in total:
        print('{} x{} {:>40}'.format(items['item'], items['count'], items['total']))
        #items, count, price
    print('-' * 50)
    #subtotal
    print('Subtotal {:>40}'.format(total_price))
    #Sales Tax
    print('Sales Tax {:>40}'.format(total_price * TAX))
    print('-' * 10)
    print('Total {:>40}'.format(total_price* TOTALTAX))
    print('*' * 50)


def run():
    """The function which excutes the program
    """

    greeting()
    order_list = {}

    while True:
        menu_order = ask_question()
        if menu_order == 'order':
            print_receipt(order_list)
        elif menu_order == 'menu':
            print_menu()
        elif menu_order == 'category':
            print('category')
        elif 'remove' in menu_order:
            #remove single item from list
            pass
        elif check_input(menu_order) is True:
            order_list = create_order(menu_order,order_list)
            print('{} order of {} have been added to the meal'.format(order_list[menu_order], menu_order))
            print()
        else:
            ask_question()

        # for food in order_list:
        #     if food['items'] == menu_order:
        #         print('{} order of {} have been added to your meal'.format(food['count'], food['items']))


if __name__ == '__main__':
    run()