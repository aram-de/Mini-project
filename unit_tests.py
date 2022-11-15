
import unittest
from unittest import mock
from io import StringIO
from app4 import Courier


class TestCourier(unittest.TestCase):
    def setUp(self) -> None:
       aCourier = Courier()
       return aCourier
 
    def test_create_courier(self):
        #set up/assemble
        courier_data = self.setUp()
        
        # Act
        #courier_obj = Courier()

        # Assert
        self.assertIsInstance(courier_data, Courier)
        self.assertEqual(courier_data.type, "couriers" )


    def test_courier_as_dict_fresh_courier(self):
        #set up/assemble
        courier_obj = self.setUp()
        
        # Act
        expected = {'name': "", 'phone': ""}
        actual = courier_obj.asdict()
        # Assert
        self.assertEqual(actual, expected )

    def test_update_courier(self):
        #set up/assemble
        courier_obj = self.setUp()
        courier_obj.name = "Pedro"
        courier_obj.phone= "123"
        courier_obj2 = self.setUp()
        # Act
        expected = {'name': "", 'phone': ""}
        actual = courier_obj.asdict()
        # Assert
        self.assertEqual(actual, expected )

def update_attributes(self) -> dict:
        updatee_as_dict = self.asdict()
        for key, value in updatee_as_dict.items():
            if key == "status":
                updatee_as_dict[key] = "Preparing"
            elif key == "courier":
                updatee_as_dict[key] = self.choose_courier_for_order()
            elif key == "items":
                updatee_as_dict[key] = self.choose_items_for_order()
            else:
                key_4_string = key.replace("_", " ").title()
                newValue = input(f"Enter the {key_4_string} ")
                while newValue == "":
                    newValue = input("Not a valid value. Enter another: ")    
                updatee_as_dict[key] = newValue
        return  updatee_as_dict