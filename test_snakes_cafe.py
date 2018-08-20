from snakes_cafe import snakes_cafe, order
import pytest


@pytest.fixture
def load_menu():
    MENU = []
    try:
        with open('default.csv', 'r') as rows:

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
    except (FileNotFoundError) as e:
        print(e + 'File not found or not a CSV file')


def test_snakes_cafe_module_exist():
    assert snakes_cafe


def test_add_food_item_lowercase():
    """ Test user input with lowercase
    """

    expect = ['Wings', 1]
    actual = order.add_item('wings')
    assert expect == actual


def test_add_food_item_with_two_words(): # bug
    """
    Test food item with two words
    """
    expect = ['Key Lime', 1]
    actual = order.add_item('Key Lime')
    assert expect == actual


def test_add_food_item_and_quantity():
    """
    Test user input with add food item & quantity
    """
    expect = ['Wings', 4]
    actual = order.add_item('wings 3')  # 1 + 3 = quantity
    assert expect == actual


def test_remove_food_item():
    """
    Test user input when remove a food item
    """
    expect = ['Wings', 0 ]
    actual = order.remove_item('remove wings')
    assert expect == actual

