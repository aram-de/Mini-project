# import pytest
# from io import StringIO
# from app4 import Courier



# def test_create_courier():
#     #set up/assemble
#     courier_obj = Courier()
    
#     # Act

#     # Assert
#     assert isinstance(courier_obj, Courier) == True
#     assert courier_obj.type == "couriers"


# def test_courier_as_dict_fresh_courier():
#     #set up/assemble
#     courier_obj = Courier()
    
#     # Act
#     expected = {'name': "", 'phone': ""}
#     actual = courier_obj.asdict()
#     # Assert
#     assert actual == expected

# def test_courier_as_dict__courier_with_data():
#     #set up/assemble
#     courier_obj = Courier()
#     courier_obj.name = "Pedro"
#     courier_obj.phone= "123"

#     # Act
#     expected = {'name': "Pedro", 'phone': "123"}
#     actual = courier_obj.asdict()
#     # Assert
#     assert actual == expected

# def test_courier_as_dict__courier_with_data():
#     #set up/assemble
#     courier_obj = Courier()
#     courier_obj.name = "Pedro"
#     courier_obj.phone= "123"

#     # Act
#     expected = {'name': "Pedro", 'phone': "123"}
#     actual = courier_obj.asdict()
#     # Assert
#     assert actual == expected

# # def update_attributes(self) -> dict:
# #     updatee_as_dict = self.asdict()
# #     for key, value in updatee_as_dict.items():
# #         if key == "status":
# #             updatee_as_dict[key] = "Preparing"
# #         elif key == "courier":
# #             updatee_as_dict[key] = self.choose_courier_for_order()
# #         elif key == "items":
# #             updatee_as_dict[key] = self.choose_items_for_order()
# #         else:
# #             key_4_string = key.replace("_", " ").title()
# #             newValue = input(f"Enter the {key_4_string} ")
# #             while newValue == "":
# #                 newValue = input("Not a valid value. Enter another: ")    
# #             updatee_as_dict[key] = newValue
# #     return  updatee_as_dict