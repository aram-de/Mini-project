import pytest
import os
from app5 import *
from pathlib import Path


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

def test_main_menu_choose_products_then_show_items_1_2(monkeypatch):
    answers = "0"
    monkeypatch.setattr('builtins.input', lambda : answers)
    actual = menu()
    expected = SystemExit
    assert type(actual) == expected

def test_main_menu_choose_products_then_add_item(monkeypatch):
    """Chooses to open the product menu, then add an item
    called TestCoke with price 4"""
    #setup
    #This fakes manual input
    
    menu()
    answers = iter(["1", "2", "TestCoke", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(answers, None))
    
    product = Product()
    list_of_products = product.get_csv_and_return_as_list_of_dict()
    #action
    print(list_of_products)
    
    assert list_of_products[len(list_of_products)-1] == {'name' : "TestCoke", 'price' : "4"}