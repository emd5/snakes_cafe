from textwrap import dedent
from uuid import uuid4
import csv


WIDTH = 50
TAX = .106
TOTALTAX = 1.10
CATEGORIES = ['Appetizers', 'Sides', 'Entrees', 'Drinks', 'Desserts']


class Order:

    def __init__(self):
        self.receipt = {'subtotal': 0}
        self.id = str(uuid4())

    def __repr__(self):
        return 'Order {} | Items: {} | Total: {}'.format(self.id, self.receipt['subtotal'], len(self.receipt))

    def __len__(self):
        return len(self.receipt)

    def order_uuid(self):
        """
        Generates a UUID for each order for the receipt
        """
        return uuid4()

    def add_item(self, user_input, menu_list):
        """
        Validates user input against the menu data, if the item does
        not exceed the item in stock, add item to the order, otherwise false
        takes an item name and a quantity as arguments.There should be a
        default value for quantity if none is given
        """
        for food in menu_list:
            if user_input[0].lower() == food['item'].lower() and (food['quantity'] + user_input[1]) < food['stock']:
                food['quantity'] += user_input[1]
                print()
                print('{} order of {} have been added to the meal'.format(user_input[1], user_input[0]))
                print()
            elif user_input[0].lower() == food['item'].lower() and (food['quantity'] + user_input[1]) > food['stock']:
                print()
                print('The amount you chose {} is greater than the amount in stock {}'.format(user_input[1], food['stock']))
                print()

    def remove_item(self, user_input, menu_list):
        """
        takes an item name and a quantity as arguments. There should be a
        default value for quantity if none is given.
        """
        item = user_input[0]
        amount = user_input[1]

        for food in menu_list:
            try:
                if item.lower() == food['item'].lower():
                    if food['quantity'] > 0:
                        food['quantity'] -= amount
                        print()
                        print('You have {} order(s) of {} in your order'.format(food['quantity'], item))
                        print('Your current subtotal is ${0:.2f}'.format(total_order_price(menu_list)))
                        print()
                        return
                    else:
                        print()
                        print('There are {} {} in your order'.format(food['quantity'], item))
                        print()
                        return
            except ValueError:
                print('Invalid Menu Item')
                return

    def display_order(self, menu_list):
        """
        Prints the user’s current order to the console
        """
        item_total(menu_list)
        total_price = total_order_price(menu_list)
        print('*' * 50)
        print('The Snakes Cafe')
        print('"Eatability Counts"')
        print()
        print('Order: ' + str(self.id))
        print('=' * 50)
        for food in menu_list:
            if int(food['quantity']) > 0:
                print('{:' '<10} x{:' '<29} ${:>.2f}'.format(food['item'], str(food['quantity']), float(food['total'])))
        print('-' * 50)
        print('{:' '<41} ${:.2f}'.format('Subtotal', total_price))
        print('{:' '<41} ${:.2f}'.format('Sales Tax', round(total_price * TAX, 2)))
        print('-' * 10)
        print('{:' '<41} ${:.2f}'.format('Total', round(total_price * TOTALTAX, 2)))
        print('*' * 50)

    def print_receipt(self, menu_list):
        """
        Creates a file containing the text of the user’s full order
        """
        total_price = total_order_price(menu_list)
        subtotal = '{:' '<41} ${:.2f}'.format('Subtotal', total_price)
        tax = '{:' '<41} ${:.2f}'.format('Sales Tax', round(total_price * TAX, 2))
        total = '{:' '<41} ${:.2f}'.format('Total', round(total_price * TOTALTAX, 2))

        create_receipt = open('./receipts/order-' + self.id+'.txt', 'w+')
        create_receipt.write('*' * 50 + '\n')
        create_receipt.write('The Snakes Cafe \n')
        create_receipt.write('" Eatability Counts "\n')
        create_receipt.write('\n')
        create_receipt.write('Order: ' + str(self.id) + '\n')
        create_receipt.write('*' * 50 + '\n')
        create_receipt.write('\n')
        for food in menu_list:
            if int(food['quantity']) > 0:
                create_receipt.write('{:' '<10} x{:' '<29} ${:>.2f}\n'.format(food['item'], str(food['quantity']), float(food['total'])))
        create_receipt.write('-' * 50 + '\n')
        create_receipt.write(subtotal + '\n')
        create_receipt.write(tax + '\n')
        create_receipt.write('-' * 10 + '\n')
        create_receipt.write(total + '\n')
        create_receipt.write('*' * 50 + '\n')

        create_receipt.close()


def greeting():
    """
    A displays a greeting when program is executed
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


def help_file_menu_message():
    """
    A help message for user to input valid csv file otherwise displays
    default menu
    """
    print('')
    print('Enter a <file name.csv> to see a custom menu')
    print('or type "default" for our menu')
    print('')


def ask_question():
    """
    Prompt for user input and is case-insensitive and strips any before or trailing whitespace
    """
    return input(' > ').lower().strip()  # check here IF BROKEN INPUT!!!!!!!!


def print_menu(menu_list):
    """
    Displays the menu
    """
    for category in CATEGORIES:
        print_category_details(category, menu_list)
    print('*' * 38)
    print('**   What would you like to order?   **')
    print('*' * 38)


def print_category_details(category, menu_list):
    """
    Displays the menu details when user enters a menu category
    """
    print('-' * 10)
    print(category)
    print('-' * 10)
    for foods in menu_list:
        if foods['category'].lower() == category.lower():
            print('{:<25}{:>20.2f}'.format(foods['item'], foods['price']))
    print()


def print_categories():
    """
    A function that prints a list of categories from the menu
    """
    print('-'* 20)
    print('Here are a list of the category Menus')
    print('-'* 20)
    for category in CATEGORIES:
        print(category)


def print_manual():
    """
    Displays a help feature for the user to input options
    """
    print('Type "menu" for list details')
    print('Type "category" for menu categories')
    print('Type any categories for for a detailed list of items')
    print('Type any <food items> to add to your order')
    print('Type "remove" <food item> to remove an item')


def check_input(user_input, menu_list):
    """
    Function that excepts an item and/or quantity and validates both
    """
    if user_input.lower() == "quit":
        exit('***   Thank you for Eating with Us! *** ')
        return
    if 'remove' in user_input.lower():
        user_input = user_input.replace('remove ', '')
    if any(char.isdigit() for char in user_input):
        whole_string = user_input.split()
        food_item = ' '.join(whole_string[:-1])
        if int(whole_string[-1]) < 1:
            print('You must enter a positive number')
        else:
            for foods in menu_list:
                if foods['item'].lower() == food_item.lower():
                    return [food_item, int(whole_string[-1])]
    else:
        for foods in menu_list:
            if foods['item'].lower() == user_input.lower():
                return [user_input, 1]


def is_item_in_menu(user_input, menu_list):
    """
    Add all food items into a new list, then validate user input is in list
    """
    food_list = []
    for food in menu_list:
        food_list.append(food['item'].lower())
    if user_input.lower() in food_list:
        return True
    else:
        print("Item not found")


def item_total(menu_list):
    """
    Calculates the order total amount
    """
    for food in menu_list:
        food['total'] = int(food['quantity']) * float(food['price'])


def total_order_price(menu_list):
    """
    Calculate the total amount
    """
    item_total(menu_list)
    sum_total = 0
    for food in menu_list:
        sum_total += food['total']
    return sum_total


def build_menu(menu_input):
    """
    Imports a csv file and generates a menu
    """
    MENU = []

    try:
        with open(menu_input, 'r') as rows:
            read = csv.DictReader(rows)
            for row in read:
                item = {}
                item['category'] = row['category']
                item['item'] = row['item']
                item['quantity'] = int(row['quantity'])
                item['price'] = float(row['price'])
                item['stock'] = int(row['stock'])
                MENU.append(item)
            # print_menu()
            return MENU
    except (TypeError, FileNotFoundError):
        print('File not found or not a CSV file')


def run():
    """
    Function runs the program
    """
    MENU = []
    greeting()
    help_file_menu_message()

    while not MENU:
        user_input = ask_question()
        if user_input == "default":
            MENU = build_menu('default.csv')
            print_menu(MENU)
        elif user_input == 'custom.csv':
            MENU = build_menu('custom.csv')
            print_menu(MENU)
        while True:
            user_input = ask_question()
            if user_input == 'order':
                order.display_order(MENU)
            elif user_input == 'receipt':
                order.print_receipt(MENU)
                print('Receipt printed')
            elif user_input == 'menu':
                print_menu(MENU)
            elif user_input == 'man':
                print_manual()
            elif user_input == 'category':
                print_categories()
            elif user_input.capitalize() in CATEGORIES:
                print_category_details(user_input, MENU)
            elif 'remove' in user_input:
                remove_user_order = check_input(user_input, MENU)
                order.remove_item(remove_user_order, MENU)
            elif check_input(user_input, MENU) is not None:
                user_order = check_input(user_input, MENU)
                is_item_in_menu(user_order[0], MENU)
                order.add_item(user_order, MENU)
            else:
                print('Invalid Input. Type "man" for options')


if __name__ == '__main__':
    order = Order()
    try:
        run()
    except KeyboardInterrupt:
        exit()
