from textwrap import dedent
from uuid import uuid4


WIDTH = 50
TAX = .106
TOTALTAX = 1.10
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
CATEGORIES = ['Appetizers', 'Sides', 'Entrees', 'Drinks', 'Desserts']


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
    print_default_menu()

# function to load a custom menu from csv file


def print_default_menu():  # a default menu from above and an imported csv file
    for category in CATEGORIES:
        print_category_details(category)
    print('*' * 38)
    print('**   What would you like to order?   **')
    print('*' * 38)
    print('type "man" for help')


def print_category_details(category):
    print(category)
    print('-' * 10)
    for foods in MENU:
        if foods['category'].lower() == category.lower():
            print(foods['item'])
    print()


def ask_question():
    return input(' > ').lower().strip()  # check here IF BROKEN INPUT!!!!!!!!


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
        return

        
def add_food_order(user_input): #bug must fix logic when an item has two words cannot split ie Key Lime 20
    whole_string = user_input.split()
    print(whole_string)
    food_item = ' '.join(whole_string[:-1])
    print(food_item)
    try:
        for food in MENU:
            if len(whole_string) > 1 and food_item.lower() == food['item'].lower():  #if user enters a space
                food['quantity'] += int(whole_string[-1])
                return [food['item'], food['quantity']]
            elif food_item.lower() == food['item'].lower():
                food['quantity'] += 1
                return [food['item'], food['quantity']]
    except TypeError:
        print('Enter a valid selection')
        ask_question()
        

def remove_food_order(user_input):
    """ Function that takes a user input argument and compares to the menu data
    """
    item = user_input.split()[1]
    for food in MENU:
        # print(item.lower() + '== ' + food['item'].lower())  # test line
        try:
            if item.lower() == food['item'].lower():
                if food['quantity'] > 0:      
                    food['quantity'] -= 1
                    item_total()
                    print('{} order of {} have been removed'.format(food['quantity'], item))
                    print('Your current total is ${0:.2f}'.format(total_order_price()))
                    return
                else:
                    print('There are {} {} in your order'.format(food['quantity'], item))
                    return
        except ValueError:
            print('Invalid Menu Item')
            return


def item_total():
    for food in MENU:
        food['total'] = int(food['quantity']) * int(food['price'])


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
            print('{0:} x{1:} {2:' '>35}'.format(food['item'], food['quantity'], food['total']))
    print('-' * 50)
    print('{0:} ${1:' '>35}'.format('Subtotal', total_price))
    print('{0:} ${1:' '>35}'.format('Sales Tax', round(total_price * TAX, 2)))
    print('-' * 10)
    print('{0:} ${1:' '>35}'.format('Total', round(total_price * TOTALTAX, 2)))
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
            print_default_menu()
        elif user_input == 'category': 
            print_categories()
        elif user_input.capitalize() in CATEGORIES:
            print_category_details(user_input)
        elif 'remove' in user_input:
            remove_food_order(user_input)
        elif check_input(user_input) is True:
            item_added = add_food_order(user_input)
            print('{} order of {} have been added to the meal'.format(item_added[0], item_added[1]))
            print()
        else:
              print('Type "man" for options')
       



if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        exit()