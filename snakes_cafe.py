from textwrap import dedent
from uuid import uuid4
import csv


WIDTH = 50
TAX = .106
TOTALTAX = 1.10
# MENU = []
# MENU = [
#   {
#     'category': 'desserts',
#     'item': 'Ice cream',
#     'quantity': 0,
#     'price': 1.95,
#   },
#   {
#     'category': 'desserts',
#     'item': 'Cake',
#     'quantity': 0,
#     'price': 2.50,
#   },
#   {
#     'category': 'desserts',
#     'item': 'Pie',
#     'quantity': 0,
#     'price': 5.50,
#   },
#   {
#     'category': 'desserts',
#     'item': 'Cupcake',
#     'quantity': 0,
#     'price': 6.50,
#   },
#   {
#     'category': 'desserts',
#     'item': 'Macaron',
#     'quantity': 0,
#     'price': 1.50,
#   },
#   {
#     'category': 'desserts',
#     'item': 'Coconut',
#     'quantity': 0,
#     'price': 8.50,
#   },
#   {
#     'category': 'desserts',
#     'item': 'Key lime',
#     'quantity': 0,
#     'price': 9.50,
#   },
#   {
#     'category': 'desserts',
#     'item': 'Pumpkin Pie',
#     'quantity': 0,
#     'price': 3.50,
#   },
#   {
#     'category': 'desserts',
#     'item': 'cream and fruit',
#     'quantity': 0,
#     'price': 3.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Coffee',
#     'quantity': 0,
#     'price': 4.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Tea',
#     'quantity': 0,
#     'price': 1.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Blood of the Innocent',
#     'quantity': 0,
#     'price': 9.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Whiskey',
#     'quantity': 0,
#     'price': 8.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Vodka',
#     'quantity': 0,
#     'price': 4.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Sparkling Wine',
#     'quantity': 0,
#     'price': 1.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Juice',
#     'quantity': 0,
#     'price': 4.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Jungle juice',
#     'quantity': 0,
#     'price': 78.50,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Gin',
#     'quantity': 0,
#     'price': 4.00,
#   },
#   {
#     'category': 'drinks',
#     'item': 'Gin & Tonic',
#     'quantity': 0,
#     'price': 10.00,
#   },
#   {
#     'category': 'sides',
#     'item': 'Veggie fries',
#     'quantity': 0,
#     'price': 4.0,
#   },
#   {
#     'category': 'sides',
#     'item': 'Fries',
#     'quantity': 0,
#     'price': 4.0,
#   },
#   {
#     'category': 'sides',
#     'item': 'Potato',
#     'quantity': 0,
#     'price': 3.00,
#   },
#   {
#     'category': 'sides',
#     'item': 'Garlic',
#     'quantity': 0,
#     'price': 5.00,
#   },
#   {
#     'category': 'sides',
#     'item': 'Biscuits',
#     'quantity': 0,
#     'price': 7.00,
#   },
#   {
#     'category': 'sides',
#     'item': 'Mashed Tots',
#     'quantity': 0,
#     'price': 9.00,
#   },
#   {
#     'category': 'sides',
#     'item': 'Garlic',
#     'quantity': 0,
#     'price': 4.70,
#   },
#   {
#     'category': 'sides',
#     'item': 'Mashed Tots',
#     'quantity': 0,
#     'price': 1.75,
#   },
#   {
#     'category': 'sides',
#     'item': 'Biscuits',
#     'quantity': 0,
#     'price': 3.25,
#   },
#   {
#     'category': 'sides',
#     'item': 'Chicken Bites',
#     'quantity': 0,
#     'price': 2.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Salmon',
#     'quantity': 0,
#     'price': 25.95,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Steak',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Meat Tornado',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'A Literal Garden',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Surf and Turf',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Ribeye',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Lobster',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Clams',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'entrees',
#     'item': 'Mussels',
#     'quantity': 0,
#     'price': 16.25,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Wings',
#     'quantity': 0,
#     'price': 4.25,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Cookies',
#     'quantity': 0,
#     'price': 6.5,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Spring Rolls',
#     'quantity': 0,
#     'price': 1.5,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Armadillo Eggs',
#     'quantity': 0,
#     'price': 2.5,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Jalapeno Pop',
#     'quantity': 0,
#     'price': 9.5,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Fries',
#     'quantity': 0,
#     'price': 8.5,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Alligator Skins',
#     'quantity': 0,
#     'price': 6.5,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Beef Jerky',
#     'quantity': 0,
#     'price': 3.5,
#   },
#   {
#     'category': 'appetizers',
#     'item': 'Eggrolls',
#     'quantity': 0,
#     'price': 3.5,
#   },
# ]
CATEGORIES = ['Appetizers', 'Sides', 'Entrees', 'Drinks', 'Desserts']


class Order:

    def __init__(self, uuid):
        self.receipt = {'subtotal':0}
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return 'Order {} | Items: {} | Total: {}'.format(self.id, self.receipt['subtotal'], len(self.receipt))


    def __len__(self):
        return len(self.receipt)


    def order_uuid():
        return uuid4


    def add_item():
        pass


    def remove_item():
        pass


    def display_order():
        pass


    def print_receipt():
        pass
        # write new file to a relative path
        # with open (f'order-{current.id}.txt', 'w') as f:
        # f.write(receipt_file)


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
    # print_default_menu()
# function to load a custom menu from csv file



    # print('type "man" for help')


def build_menu(menu_csv):
    MENU = []
    with open(menu_csv, 'r') as rows:
        try:
            read = csv.DictReader(rows)
            for row in read:
                item = {}
                item['category'] = row['category']
                item['item'] = row['item']
                item['quantity'] = int(row['quantity'])
                item['price'] = float(row['price'])
                MENU.append(item)
            # print_menu()
            return MENU
        except(IndexError, FileNotFoundError):
            print('File not found or not a CSV file')


def print_menu(menu_list):  # a default menu from above and an imported csv file
    for category in CATEGORIES:
        print_category_details(category, menu_list)
    print('*' * 38)
    print('**   What would you like to order?   **')
    print('*' * 38)


def print_category_details(category, menu_list):

    print(category)
    print('-' * 10)
    for foods in menu_list:
        if foods['category'].lower() == category.lower():
            print(foods['item'])
    print()


def ask_question():
    return input(' > ').lower().strip()  # check here IF BROKEN INPUT!!!!!!!!


def ask_menu_option():
    print('Which menu would you like?')
    print('Enter "default" or "custom"')


def print_categories():
    """A function that prints a list of categories from the menu
    """
    print('-'* 20)
    print('Here are a list of the category Menus')
    print('-'* 20)
    for category in CATEGORIES:
        print(category)


def print_manual():
      print('Type "menu" for menu options')
      print('Type "category" for menu categories')
      print('Type any categories for for a detailed list of items')
      print('Type any <food items> to add to your order')
      print('Type "remove" <food item> to remove an item')


def check_input(user_input, menu_list):
    """Function that returns a boolean when user input is in the menu data,
    otherwise exits program
    """
    if user_input.lower() == "quit":
        exit('***   Thank you for Eating with Us! *** ')
        return

    if any(char.isdigit() for char in user_input):
        whole_string = user_input.split()
        food_item = ' '.join(whole_string[:-1])
        for foods in menu_list:
            if foods['item'].lower() == food_item.lower():
                return [food_item, int(whole_string[-1])]

    # elif not any(char.isdigit() for char in user_input):
    else:
        for foods in menu_list:
            if foods['item'].lower() == user_input.lower():
                return [user_input, 1]


def add_food_order(user_input, menu_list):
    for food in menu_list:
        if user_input[0].lower() == food['item'].lower():
            # print(user_input[0])
            food['quantity'] += user_input[1]


    # try:
    # print(type(user_input))
    # if any(char.isdigit() for char in user_input):
    #     print('1: ' + user_input)
    #     whole_string = user_input.split()
    #     if len(whole_string) > 1:
    #         food_item = ' '.join(whole_string[:-1])
    #     for food in menu_list:
    #         if food_item.lower() == food['item'].lower():
    #             food['quantity'] += int(whole_string[-1])
    #             return [food['item'], food['quantity']]
    # else:
    #     for food in menu_list:
    #         if user_input.lower() == food['item'].lower():
    #             food['quantity'] += 1
    #             return [food['item'], food['quantity']]
    # except TypeError:
    #     print('Enter a valid selection')
    #     ask_question()


def remove_food_order(user_input, menu_list):
    """ Function that takes a user input argument and compares to the menu data
    """
    item = user_input.split()[1]
    for food in menu_list:
        try:
            if item.lower() == food['item'].lower():
                if food['quantity'] > 0:
                    food['quantity'] -= 1
                    item_total(menu_list)
                    print('{} order of {} have been removed'.format(food['quantity'], item))
                    print('Your current total is ${0:.2f}'.format(total_order_price(menu_list)))
                    return
                else:
                    print('There are {} {} in your order'.format(food['quantity'], item))
                    return
        except ValueError:
            print('Invalid Menu Item')
            return


def item_total(menu_list):
    for food in menu_list:
        food['total'] = int(food['quantity']) * float(food['price'])


def total_order_price(menu_list):
    sum_total = 0
    for food in menu_list:
       sum_total += food['total']
    return sum_total


def print_receipt(menu_list):
    item_total(menu_list)
    total_price = total_order_price(menu_list)
    print('*' * 50)
    print('The Snakes Cafe')
    print('"Eatability Counts"')
    print()
    print('Order: ' + str(uuid4()))
    print('=' * 50)
    for food in menu_list:
        if int(food['quantity']) > 0:
            print('{0:} x{1:} {2:' '>35}'.format(food['item'], str(food['quantity']), str(food['total'])))
    print('-' * 50)
    print('{0:} ${1:' '>35}'.format('Subtotal', total_price))
    print('{0:} ${1:' '>35}'.format('Sales Tax', round(total_price * TAX, 2)))
    print('-' * 10)
    print('{0:} ${1:' '>35}'.format('Total', round(total_price * TOTALTAX, 2)))
    print('*' * 50)


def run():
    """The function which excutes the program
    """
    MENU = []
    greeting()
    ask_menu_option()
    while True:
        user_input = ask_question()
        if user_input == "default":
            MENU = build_menu('default.csv')
            print_menu(MENU)
        elif user_input == "custom":
            MENU = build_menu('custom.csv')
            print_menu(MENU)
        elif user_input == 'order':
            print_receipt(MENU)
        elif user_input == 'menu':
            print_menu(MENU)
        elif user_input == 'man':
            print_manual()
        elif user_input == 'category':
                print_categories()
        elif user_input.capitalize() in CATEGORIES:
            print_category_details(user_input, MENU)
        elif 'remove' in user_input:
            remove_food_order(user_input, MENU)
        # elif check_input(user_input, MENU) is True:
        elif check_input(user_input, MENU) is not None:
            user_order = check_input(user_input, MENU)
            add_food_order(user_order, MENU)
            # item_added = add_food_order(user_input, MENU)
            # print(item_added)
            print('{} order of {} have been added to the meal'.format(user_order[1], user_order[0]))
            # print()
        else:
            print('Type "man" for options')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        exit()
