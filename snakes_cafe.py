from textwrap import dedent
from uuid import uuid4


WIDTH = 50
TAX = .106
TOTALTAX = 1.10
# MENU = {'Appetizers': [{'Wings': 20.99},
        #                 {'Cookies': 1.50},
        #                 {'Spring Rolls': 2.00},
        #                 {'Armadillo eggs': 4.35},
        #                 {'Jalapeno Poppers': 10.50},
        #                 {'Fries': 2.00},
        #                 {'Alligator Skins': 2.00},
        #                 {'Beef Jerky': 2.23},
        #                 {'Eggrolls': 1.33}],
        # 'Entrees': [{'Salmon': 20.99},
        #             {'Steak': 1.50},
        #             {'Meat Tornado': 2.00},
        #             {'A Literal Garden': 4.35},
        #             {'Surf and Turf': 10.50},
        #             {'Ribeye': 2.00},
        #             {'Lobster': 20.00},
        #             {'Clams': 12.23},
        #             {'Mussels': 15.00}],
        # 'Desserts': [{'Ice cream': 1.99},
        #              {'Cake': 2.50},
        #              {'Pie': 2.99},
        #              {'Cupcake': 3.35},
        #              {'Macaroon': 5.50},
        #              {'Coconut': 1.00},
        #              {'Key Lime': 1.00},
        #              {'Pumpkie Pis': 5.23},
        #              {'Chocolate Chip Cookies': 10.00}],
        # 'Drinks': [{'Coffee': 20.99},
        #              {'Tea': 1.50},
        #              {'Blood of the Innocent': 2.00},
        #              {'Whiskey': 4.35},
        #              {'Vodka': 10.50},
        #              {'Sparkling Wine': 2.00},
        #              {'Juice': 10.00},
        #              {'Jungle Juice': 6.00},
        #              {'Gin': 3.00},
        #              {'Gin & Tonic': 4.00}],
        # 'Sides': [{'Veggies': 5.99},
        #             {'Fries': 2.50},
        #             {'Potato': 2.00},
        #             {'Garlic': 9.35},
        #             {'Biscuits': 6.50},
        #             {'Mashed Tots': 7.00},
        #             {'Garlic': 9.35},
        #             {'Biscuits': 6.50},
        #             {'Mashed Tots': 3.00},
        #             {'Chicken Bites': 9.00}],
        # }


MENU = [
  {
    'category': 'desserts',
    'item': 'Ice cream',
    'quantity': 0,
    'price': 1.95,
  },
  {
    'category': 'desserts',
    'item': 'Cake',
    'quantity': 0,
    'price': 2.50,
  },
  {
    'category': 'desserts',
    'item': 'Pie',
    'quantity': 0,
    'price': 5.50,
  },
  {
    'category': 'desserts',
    'item': 'Cupcake',
    'quantity': 0,
    'price': 6.50,
  },
  {
    'category': 'desserts',
    'item': 'Macaron',
    'quantity': 0,
    'price': 1.50,
  },
  {
    'category': 'desserts',
    'item': 'Coconut',
    'quantity': 0,
    'price': 8.50,
  },
  {
    'category': 'desserts',
    'item': 'Key lime',
    'quantity': 0,
    'price': 9.50,
  },
  {
    'category': 'desserts',
    'item': 'Pumpkin Pie',
    'quantity': 0,
    'price': 3.50,
  },
  {
    'category': 'desserts',
    'item': 'cream and fruit',
    'quantity': 0,
    'price': 3.50,
  },
  {
    'category': 'drinks',
    'item': 'Coffee',
    'quantity': 0,
    'price': 4.50,
  },
  {
    'category': 'drinks',
    'item': 'Tea',
    'quantity': 0,
    'price': 1.50,
  },
  {
    'category': 'drinks',
    'item': 'Blood of the Innocent',
    'quantity': 0,
    'price': 9.50,
  },
  {
    'category': 'drinks',
    'item': 'Whiskey',
    'quantity': 0,
    'price': 8.50,
  },
  {
    'category': 'drinks',
    'item': 'Vodka',
    'quantity': 0,
    'price': 4.50,
  },
  {
    'category': 'drinks',
    'item': 'Sparkling Wine',
    'quantity': 0,
    'price': 1.50,
  },
  {
    'category': 'drinks',
    'item': 'Juice',
    'quantity': 0,
    'price': 4.50,
  },
  {
    'category': 'drinks',
    'item': 'Jungle juice',
    'quantity': 0,
    'price': 78.50,
  },
  {
    'category': 'drinks',
    'item': 'Gin',
    'quantity': 0,
    'price': 4.00,
  },
  {
    'category': 'drinks',
    'item': 'Gin & Tonic',
    'quantity': 0,
    'price': 10.00,
  },
  {
    'category': 'sides',
    'item': 'Veggie fries',
    'quantity': 0,
    'price': 4.0,
  },
  {
    'category': 'sides',
    'item': 'Fries',
    'quantity': 0,
    'price': 4.0,
  },
  {
    'category': 'sides',
    'item': 'Potato',
    'quantity': 0,
    'price': 3.00,
  },
  {
    'category': 'sides',
    'item': 'Garlic',
    'quantity': 0,
    'price': 5.00,
  },
  {
    'category': 'sides',
    'item': 'Biscuits',
    'quantity': 0,
    'price': 7.00,
  },
  {
    'category': 'sides',
    'item': 'Mashed Tots',
    'quantity': 0,
    'price': 9.00,
  },
  {
    'category': 'sides',
    'item': 'Garlic',
    'quantity': 0,
    'price': 4.70,
  },
  {
    'category': 'sides',
    'item': 'Mashed Tots',
    'quantity': 0,
    'price': 1.75,
  },
  {
    'category': 'sides',
    'item': 'Biscuits',
    'quantity': 0,
    'price': 3.25,
  },
  {
    'category': 'sides',
    'item': 'Chicken Bites',
    'quantity': 0,
    'price': 2.25,
  },
  {
    'category': 'entrees',
    'item': 'Salmon',
    'quantity': 0,
    'price': 25.95,
  },
  {
    'category': 'entrees',
    'item': 'Steak',
    'quantity': 0,
    'price': 16.25,
  },
  {
    'category': 'entrees',
    'item': 'Meat Tornado',
    'quantity': 0,
    'price': 16.25,
  }, 
  {
    'category': 'entrees',
    'item': 'A Literal Garden',
    'quantity': 0,
    'price': 16.25,
  },
  {
    'category': 'entrees',
    'item': 'Surf and Turf',
    'quantity': 0,
    'price': 16.25,
  },
  {
    'category': 'entrees',
    'item': 'Ribeye',
    'quantity': 0,
    'price': 16.25,
  },
  {
    'category': 'entrees',
    'item': 'Lobster',
    'quantity': 0,
    'price': 16.25,
  },
  {
    'category': 'entrees',
    'item': 'Clams',
    'quantity': 0,
    'price': 16.25,
  },
  {
    'category': 'entrees',
    'item': 'Mussels',
    'quantity': 0,
    'price': 16.25,
  },
  {
    'category': 'appetizers',
    'item': 'Wings',
    'quantity': 0,
    'price': 4.25,
  },
  {
    'category': 'appetizers',
    'item': 'Cookies',
    'quantity': 0,
    'price': 6.5,
  },
  {
    'category': 'appetizers',
    'item': 'Spring Rolls',
    'quantity': 0,
    'price': 1.5,
  },
  {
    'category': 'appetizers',
    'item': 'Armadillo Eggs',
    'quantity': 0,
    'price': 2.5,
  },
  {
    'category': 'appetizers',
    'item': 'Jalapeno Pop',
    'quantity': 0,
    'price': 9.5,
  },
  {
    'category': 'appetizers',
    'item': 'Fries',
    'quantity': 0,
    'price': 8.5,
  },
  {
    'category': 'appetizers',
    'item': 'Alligator Skins',
    'quantity': 0,
    'price': 6.5,
  },
  {
    'category': 'appetizers',
    'item': 'Beef Jerky',
    'quantity': 0,
    'price': 3.5,
  },
  {
    'category': 'appetizers',
    'item': 'Eggrolls',
    'quantity': 0,
    'price': 3.5,
  },
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
    print_menu()

CATEGORIES = ['Appetizers', 'Sides', 'Entrees', 'Drinks', 'Desserts']


def print_menu():
    for category in CATEGORIES:
        print_category_details(category)
    print('*' * 38)
    print('**   What would you like to order?   **')
    print('*' * 38)


def print_category_details(category):
    print(category)
    print('-' * 10)
    for foods in MENU:
        if foods['category'].lower() == category.lower():
            print(foods['item'])
    print()


def ask_question():
    print('type "man" for help')
    return input('>').lower()  #check here IF BROKEN INPUT!!!!!!!!


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
      print('Type any food items to add to your order [BUGGY]')
      print('Type "remove" <food item> to remove an item [BUGGY]')
      print('Type "remove" <food item> to remove an item [BUGGY]')


def check_input(user_input):
    """Function that returns a boolean when user input is in the menu data, 
    otherwise exits program
    """
    if user_input.lower() == "quit":
        exit('***   Thank you for Eating with Us! *** ')
        return
    for foods in MENU: #to do - add try/ except for invalid user input
        if foods['item'].lower() == user_input.lower():
            return True
    else:
        print('Invalid characters')
        ask_question()
   

def add_food_order(user_input): #bug must fix logic when an item has two words cannot split ie Key Lime 20
    item_quantity = user_input.lower().split()
    try:
        for food in MENU:
            if len(item_quantity) > 1 and item_quantity[0].lower() == food['item'].lower():  #if user enters a space
                food['quantity'] += int(item_quantity[1])
                # print('{} order of {} have been added to the meal'.format(food['quantity'], item_quantity[0]))
                # print()
                return [food['item'], food['quantity']]
            elif item_quantity[0].lower() == food['item'].lower():
                food['quantity'] += 1
                # print('{} order of {} have been added to the meal'.format(food['quantity'], item_quantity[0]))
                # print()
                return [food['item'], food['quantity']]
    except ValueError:
        print('Enter a valid selection')
        return run()


def remove_food_order(user_input):
    """ Function that takes a user input argument and compares to the menu data
    """
    for food in MENU:
        if user_input == food['item']:
            if food['quantity'] > 0:
                food['quantity'] -= 1
                print('{} order of {} have been removed'.format(food['quantity'], user_input))
                print()
                
            else:
                print('There are no {} in your order'.format(item))
    

def item_total():
    for food in MENU:
        food['total'] = int(food['quantity']) * int(food['price']) #create new key & value


def total_order_price():
    sum_total = 0
    for food in MENU:
       sum_total += food['total']
    return sum_total


def print_receipt():
    item_total()
    total_price = total_order_price()
    print('*' * 50)
    print('The Snakes Cafe')
    print('"Eatability Counts"')
    print()
    print('Order: ' + str(uuid4()))
    print('=' * 50)
    for food in MENU:
        if food['quantity'] > 0:
            print("{} x {} {}".format(food['item'], int(food['quantity']), int(food['total'])))
    print('-' * 50)
    #subtotal
    print('Subtotal {:>40}'.format(total_price))
    #Sales Tax
    print('Sales Tax {:>38}'.format(round(total_price * TAX, 2)))
    print('-' * 10)
    print('Total {:>45}'.format(round(total_price * TOTALTAX, 2)))
    print('*' * 50)


def run():
    """The function which excutes the program
    """
    greeting()
    
    while True:
        user_input = ask_question()
        if user_input == 'order':
            print_receipt()
        elif user_input == 'man':
            print_manual()
        elif user_input == 'menu':
            print_menu()
        elif user_input == 'category':  # prints a list of category menu 
            print_categories()
        elif user_input in CATEGORIES:  # must print details of a menu category
            print_category_details(user_input)
        elif 'remove' in user_input:
            remove_food_order(user_input)
        elif check_input(user_input) is True:
            # print('Enter <food item> space <quantity>')
            item_added = add_food_order(user_input)
            print('{} order of {} have been added to the meal'.format(item_added[0], item_added[1]))
            print()
        else:
            ask_question()

        # for food in order_list:
        #     if food['items'] == menu_order:
        #         print('{} order of {} have been added to your meal'.format(food['count'], food['items']))


if __name__ == '__main__':
    run()