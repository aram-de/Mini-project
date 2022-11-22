import pytest
import os
# # # #from io import StringIO
# # # #from app4 import Courier
from app5 import *
from pathlib import Path

from unittest.mock import patch
from unittest.mock import Mock



# @patch("app5.Product")
# @patch("builtins.input")

# def test_main_menu_choose_one(mock_input, mock_product):
#     a_product = Mock()
#     mock_input.return_value = 1

#     #a_mocker = mocker.patch.object(Product.item_menu(Product), return_value=None)
#     #answers = 1
#     #monkeypatch.setattr('builtins.input', lambda : answers)
#     #TEST IF A METHOD HAS BEEN CALLED
#     assert mock_product.call_count == 1

##TEST GET FILE

#happy

def test_get_file_returns_list_for_all_valid_object_types():
    an_item1 = Order()
    an_item2 = Courier()
    an_item3 = Product()
    expected = list
    content = an_item1.get_csv_and_return_as_list_of_dict()
    actual = type(content)
    assert expected == actual
    content = an_item2.get_csv_and_return_as_list_of_dict()
    actual = type(content)
    assert expected == actual
    content = an_item3.get_csv_and_return_as_list_of_dict()
    actual = type(content)
    assert expected == actual


def test_get_file_returns_list_of_dict():
    an_item1 = Order()
    an_item2 = Courier()
    an_item3 = Product()
    a_list1 = an_item1.get_csv_and_return_as_list_of_dict()
    a_list2 = an_item2.get_csv_and_return_as_list_of_dict()
    a_list3 = an_item3.get_csv_and_return_as_list_of_dict()
    expected = dict
    for item in a_list1:
        actual = type(item) 
        assert expected == actual
    for item in a_list2:
        actual = type(item) 
        assert expected == actual
    for item in a_list3:
        actual = type(item) 
        assert expected == actual

# # # #unhappy

def test_get_file_returns_error_when_it_fails():
    an_item = Item() 
    an_item.type = "ITEM2" #this fails because we are trying
    #to get an object with attribute type item2 of which there's none
    #mock data
    expected = FileNotFoundError#(2, 'No such file or directory')
    #with pytest.raises(FileNotFoundError):
    actual = an_item.get_csv_and_return_as_list_of_dict()
    assert expected == type(actual)


# # # ##TEST SHOW ITEM

# # #happy
def test_show_items_when_there_are():
    an_item = Product()
    #an_item.type = "ITEM"
    #stub data
    an_item.content = [{'name' : "melon", 'age' : 3},  {'name' : "melon2", 'age' : 23}]
    expected = 0
    actual = an_item.show_items() 
    assert expected == actual

# # #unhappy
def test_show_items_when_content_empty():
    an_item = Product()
    #3 lines below make the file for product empty
    file_to_open = Path(rf"data/{an_item.type}.csv")        
    with open(file_to_open, "w", newline='') as csvfile:
        pass
    #stub data
    an_item.content = []
    #os.remove(f"data/{an_item.type}.csv") #delete file so that we use mock data
    expected = 1 #means it failed because the file was empty.
    actual = an_item.show_items() 
    assert expected == actual
    #Put something back in file for other tests 
    an_item.content = [{'name' : "melon", 'price' : "3"},  {'name' : "melon2", 'price' : "23"}]
    an_item.write_to_storage()


# # #TESTING WRITING

# # #HAPPY
def test_write_to_csv_writes():
    #set up
    an_item = Item()
    file_to_open = Path(rf"data/{an_item.type}.csv")
    file_exists = os.path.isfile(file_to_open)
    if file_exists:
        os.remove(f"data/{an_item.type}.csv") #delete file so that we use mock data
    else:
    #Mock data
        an_item.content = [{'name' : "melon", 'age' : "3"},  {'name' : "melon2", 'age' : "23"}]
        #action
        an_item.write_to_storage()
        assert an_item.content == an_item.get_csv_and_return_as_list_of_dict()

def test_write_to_storage_fails():
    """ test failes because he data passed is not a list of dict"""
    #set up
    an_item = Item()
    file_to_open = Path(rf"data/{an_item.type}.csv")
    file_exists = os.path.isfile(file_to_open)
    if file_exists:
        os.remove(f"data/{an_item.type}.csv") #delete file so that we use mock data
    else:
        expected =  TypeError 
        #Mock data: overwrite object content with None  
        an_item.content = None
        #action
        an_item.write_to_storage() #writing nothing to file
        assert expected == type(an_item.write_to_storage())


# #TESTING ADDING ITEM
# #happy

def test_add_item_succeeds(monkeypatch):
    an_item_menu = Item()
    #setup
    #This fakes manual input
    answers = iter(["testAdd", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(answers, None))
    
    item_plus_added_content = list(an_item_menu.content).append({'name' : "testAdd", 'age' : "3"})

    #action
    assert item_plus_added_content == an_item_menu.add_item_to_file()






# UNCOMMENT ABOVE HERE    

# unhappy NOT WORKING
# def test_collect_attributes_user_enters_nothing(monkeypatch):
#     an_item = Courier()
#     an_item.item_menu()
#     #setup
#     original_item_content = list(an_item.content)
#     #This fakes multiple manual inputs
#     manual_inputs = iter(["", ""])
#     monkeypatch.setattr('builtins.input', lambda _: next(manual_inputs, None))
#     #action
#     assert original_item_content == an_item.collect_attributes()


#Testing get product indexes if it succeeds returns index list





#TESTING selecting ITEM
#happy

# def test_selecting_item_success(monkeypatch):
    












# def test_run_it(my_fixture):
#     ...
#     with mock.patch("my_project.main.MyHelperService.my_method1") as method1_mock:
#         resp = _import.main(req)
#         method1_mock.assert_called_once()

# def test_sleep_awhile(monkeypatch, mocker):
#     m = mocker.patch("src.example.time.sleep", return_value=None)
#     sleep_awhile(3)
#     m.assert_called_once_with(3)

# def test_main_menu_choose_one(monkeypatch, mocker):
#     menu()
#     a_mocker = mocker.patch.object(Product.item_menu(Product), return_value=None)
#     answers = 1
#     monkeypatch.setattr('builtins.input', lambda : answers)
#     #TEST IF A METHOD HAS BEEN CALLED
#     a_mocker.assert_called_once() 







# def print_name(): # No DI
#     name = input("Please enter your name: ")
#     print(f"Hello {name}!") # Dependency
# @patch("builtins.input")
# @patch("builtins.print")
# def test_print_name(mock_print, mock_input):
#     # Arrange
#     mock_input.return_value = "John"
#     # Act
#     print_name() 
#     # Assert
#     mock_print.assert_called_with("Hello John!") # Passes
#     assert mock_input.call_count == 1
#     assert mock_print.call_count == 1

# # def test_main_menu_choose_one(monkeypatch, mocker):
# #     answers = 1
# #     monkeypatch.setattr('builtins.input', lambda : answers)
# #     mocked_func = mocker.patch('test.hello')

# #     actual = aMenu.menu()
# #     expected = "Opened product menu"
# #     assert actual == expected


def test_main_menu_invalid_input(monkeypatch):
    answers = "Hello"
    monkeypatch.setattr('builtins.input', lambda : answers)
    actual = menu()
    expected = SystemExit
    assert type(actual) == expected

def test_main_menu_choose_zero(monkeypatch):
    answers = "0"
    monkeypatch.setattr('builtins.input', lambda : answers)
    actual = menu()
    expected = SystemExit
    assert type(actual) == expected
