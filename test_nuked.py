# # import pytest
import os
# # # #from io import StringIO
# # # #from app4 import Courier
from nuked import *

aMenu = Menu()

a_product = Product()
a_product.item_menu()

def test_get_file_returns_list():
    a_list = get_csv_and_return_as_list_of_dict("orders")
    expected = list
    actual = type(a_list)
    assert expected == actual


def test_get_file_returns_list_of_dict():
    a_list = get_csv_and_return_as_list_of_dict("orders")
    expected = dict
    for item in a_list:
        actual = type(item) 
        assert expected == actual


# #Integration

def test_write_to_csv_writes():
    #set up
    an_item_type = 'orders'
    os.remove(f"data/{an_item_type}.csv") #delete file
    aDict_list = [{'name' : "melon", 'age' : "3"},  {'name' : "melon2", 'age' : "23"}]
    an_item_type = 'orders'

    #action
    write_list_of_dict_to_csv(aDict_list, an_item_type)

    assert aDict_list == get_csv_and_return_as_list_of_dict("orders")


def test_main_menu_invalid_input(monkeypatch):
    answers = "Hello"
    monkeypatch.setattr('builtins.input', lambda : answers)
    actual = aMenu.menu()
    expected = "Invalid input"
    assert actual == expected


# def test_main_menu_choose_one(monkeypatch):
#     answers = 1
#     monkeypatch.setattr('builtins.input', lambda : answers)
#     actual = aMenu.menu()
#     expected = "Opened product menu"
#     assert actual == expected

def test_main_menu_choose_one(monkeypatch, mocker):
    answers = 1
    monkeypatch.setattr('builtins.input', lambda : answers)
    mocked_func = mocker.patch('test.hello')

    actual = aMenu.menu()
    expected = "Opened product menu"
    assert actual == expected


def test_main_menu_choose_zero(monkeypatch):
    answers = iter([0])
    monkeypatch.setattr('builtins.input', lambda : next(answers))
    actual = aMenu.menu()
    expected = "Program ended st"
    assert actual == expected

def test_hello(mocker):
    mocked_func = mocker.patch('test.hello')
    my_function()
    mocked_func.assert_called_once_with('Sam')