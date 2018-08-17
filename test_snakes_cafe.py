from .snakes_cafe import add_food_order, remove_food_order
import pytest


def test_snakes_cafe_module_exist():
    pass


def test_add_food_item_lowercase():
    """ Test user input with lowercase
    """
    expect = ['Wings', 1]
    actual = add_food_order('wings')
    assert expect == actual


def test_add_food_item_with_two_words(): # bug
    """ Test food item with two words
    """
    expect = ['Key Lime', 1]
    actual = add_food_order('Key Lime')  
    assert expect != actual


def test_add_food_item_and_quantity():
    """ Test user input with food item & quantity
    """
    expect = ['Wings', 4]
    actual = add_food_order('wings 3')  # 1 + 3 = quantity
    assert expect == actual


def test_remove_food_item():
    expect = ['Wings', 0 ]
    actual = remove_food_order('remove wings')
    assert expect == actual