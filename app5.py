import os.path
import csv
from pathlib import Path
import time
import sys

pos_status = ("Preparing", "Waiting", "Travelling", "Delivered")


class Item():
    def __init__(self) -> None:
        self.type = "item"
        self.name = ""
        self.age = ""
        self.field_names = ("name", "age")
        self.content = self.get_csv_and_return_as_list_of_dict()


    def write_to_storage(self):
        try:
            file_to_open = Path(f"data/{self.type}.csv")
            with open(file_to_open, "w", newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                    writer.writeheader()
                    for dictio in self.content:
                        writer.writerow(dictio)
        except TypeError as e:
            print("You tried to write an empty list to the file.")
            return e
    
    def delete_item(self):
        self.show_items()
        valid_input = self.gen_valid_inputs()
        if len(valid_input) == 1:
            print("The are no items to delete") 
            self.item_menu() 
        else:
            print(f"Enter the number for the {self.type[:-1]} you want to delete: ")
            deletee = input()
            deletee = self.check_valid_input(deletee,valid_input)
            if deletee == "":
                menu()
            else:                
                file_to_open = Path(rf"data/{self.type}.csv")
                with open(file_to_open, "r") as itemsf:
                    lines = itemsf.readlines()
                    del lines[int(deletee+1)] #needs the plus one to be consistent with the file
                with open(file_to_open, "w") as itemsf:
                    for pos, line in enumerate(lines):
                        itemsf.write(line)
                print(f"{self.type[:-1]} number {deletee+1} is now deleted.")
                self.item_menu()
    


    def gen_valid_inputs(self) -> list:
        list_of_dict = self.get_csv_and_return_as_list_of_dict()
        valid_input = [str(num+1) for num, line in enumerate(list_of_dict)] 
        #TODO there must be a way to do with without the unused line variable
        valid_input.append("x")
        return valid_input


    def check_valid_input(self, user_input : str, valid_inputs : list, from_orders = False) -> int: 
        while (user_input not in valid_inputs and user_input.lower() != "x") or user_input.strip() == "":
            print("Your choice was not valid.")
            user_input = input(f"Please, choose a {self.type[:-1]} by entering the corresponding number above or x to leave: ")
        #TODO bug, X takes to back to courier if you are adding a courier to an order, same for products
        if user_input.lower() == "x" and from_orders == False:
            #if self.type == "products" or self.type == "couriers":
            self.item_menu()
        elif (user_input.lower() == "x" and from_orders == True) or user_input.lower() == "d":    
            print("\n\n\nOrder neither created nor updated \n\n\n")
            order = Order()
            order.item_menu()
        else:
            return (int(user_input) - 1) #-1 so that it matches the index instead of the number in shown list
    


    def get_csv_and_return_as_list_of_dict(self) -> list:
        try:
            file_to_open = Path(rf"data/{self.type}.csv")
            with open(file_to_open, "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                list_of_dict = list(records)
            return list_of_dict
        except FileNotFoundError as e:
            print(rf"No file exists for {self.type}s yet.")
            return e



    def show_items(self) -> int:
        list_of_dict = self.get_csv_and_return_as_list_of_dict()
        if list_of_dict == []:
            print(f"There are no {self.type}s currently in the system")
            return 1
        for num, line in enumerate(list_of_dict):      
            print(f"{self.type[:-1].capitalize()} n.{num+1}")
            for key, value in line.items():
                key_4_string = key.replace("_", " ").title()
                print(f"\t{key_4_string}: {value}")
            print("")
        return 0

        
    def as_dict(self):
        return {'name': self.name, 'age': self.age}


    def collect_attributes(self) -> dict:
        updatee_as_dict = self.as_dict()
        for key, value in updatee_as_dict.items():
            key_4_string = key.replace("_", " ").title()
            newValue = input(f"Enter the {key_4_string} ")
            if newValue == "":
                newValue = value    
            updatee_as_dict[key] = newValue
        return  updatee_as_dict


    def add_item_to_file(self): 
#TODO this function does not add a line the previous line does not have a break line character
        file_exists = os.path.isfile(rf"data\{self.type}.csv")
        an_item = self.collect_attributes()
        file_to_open = Path(rf"data/{self.type}.csv")        
        if file_exists and os.stat(rf"data\{self.type}.csv").st_size != 0: #file exists and it is not empty
            with open(file_to_open, "a", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writerow(an_item)
        else: #file either does not exist or is emtpy
            with open(file_to_open, "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writeheader()
                writer.writerow(an_item)


    def update_item(self):
            selected_list = self.get_csv_and_return_as_list_of_dict()
            valid_inputs = self.gen_valid_inputs()
            self.show_items()
            print(f"""Enter the number for the {self.type[:-1]} you want
        to update or x to go to menu: """)
            updatee = input()
            updatee = self.check_valid_input(updatee, valid_inputs)
            updatee_as_dict = selected_list[updatee]
            for key, value in updatee_as_dict.items():
                key_4_string = key.replace("_", " ")
                if key == 'courier':
                    updatee_as_dict["courier"] = self.choose_courier_for_order()
                elif key == "status":
                    pass
                elif key == "items":
                    updatee_as_dict["items"] = self.choose_items_for_order()
                else:
                    newValue = input(f"Enter the {key_4_string} ")
                    if newValue == "":
                        pass
                    else:
                        updatee_as_dict[key] = newValue
#TODO this code screams function, look into it
            file_to_open = Path(rf"data/{self.type}.csv")
            with open(file_to_open, "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                list_of_records = (list(records))
            list_of_records[int(updatee)] = updatee_as_dict

            with open(file_to_open, "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writeheader()
                for dictio in list_of_records:
                    writer.writerow(dictio)
            print(f"{self.type[:-1]} {updatee + 1} has been updated")
                  


    
    def item_menu(self):
        if self.type == "orders":
            menu_string = f"""Choose an option:
                0 to go to main menu
                1 for seeing the list of {self.type}
                2 to add new {self.type}
                3 to update/replace {self.type}
                4 to update the status of {self.type}
                5 to delete {self.type}"""
            valid_inputs = ("0","1","2","3","4", "5")
        else:
            menu_string = f"""Choose an option:
                0 to go to main menu
                1 for seeing the list of {self.type}
                2 to add a new {self.type}
                3 to update/replace {self.type}
                4 to delete {self.type}"""
            valid_inputs = ("0","1","2","3","4")
        print(menu_string)
        user_input2 = input()
        while user_input2 not in valid_inputs:
            print("Not a valid option. Try again.") 
            print(menu_string)        
            user_input2 = input()
        if user_input2 == "0":
            menu()
        elif user_input2 == "1":
            self.show_items()
            print("")
            self.item_menu()
        elif user_input2 == "2":
            self.add_item_to_file()
            print("")
            self.item_menu()
        elif user_input2 == "3":
            self.update_item()
            print("")
            self.item_menu()
        elif user_input2 == "4" and self.type != "orders":
            self.delete_item()
            print("")
            self.item_menu()
        elif user_input2 == "4" and self.type == "orders":
            self.update_status()
            print("")
            self.item_menu()
        elif user_input2 == "5" and self.type == "orders":
            self.delete_item()
            print("")
            self.item_menu()




class Courier(Item):
    def __init__(self) -> None:
        self.type = "couriers"
        self.name = ""
        self.phone = ""
        self.field_names = ('name', 'phone')
        self.content = self.get_csv_and_return_as_list_of_dict()
    
    def as_dict(self):
        return {'name': self.name, 'phone': self.phone}


#NEW CLASS HERE

class Product(Item):   
    def __init__(self) -> None:
        self.type = "products"
        self.name = ""
        self.price = 0
        self.field_names = ('name', 'price')
        self.content = self.get_csv_and_return_as_list_of_dict()


    
    def as_dict(self):
        return {'name': self.name, 'price': self.price}
        

#NEW CLASS HERE

class Order(Item):
#TODO add method to add products to an order when creating a new order
    def __init__(self) -> None:


        self.type = "orders"
        self.customer_name = ""
        self.customer_address = ""
        self.customer_phone = ""
        self.courier = ""
        self.status = "1"
        self.items = ""
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]
        self.pos_status = ("Preparing", "Waiting", "Travelling", "Delivered")
        self.content = self.get_csv_and_return_as_list_of_dict()

    def as_dict(self):
        return {'customer_name': self.customer_name, 'customer_address': self.customer_address,
            'customer_phone' : self.customer_phone, 'courier' : self.courier, 'status' : self.status,
            'items' : self.items}
        
    def select_valid_status(self):
        indexes = []
        for index, status in enumerate(self.pos_status):
            print(f"{index}. {status}")
            indexes.append(index)
        try:
            new_status = int(input(f"Enter the number for the new status: "))
            while new_status not in indexes:
                print("Not a valid number. It must be one of the numbers in the list above.")
                new_status = int(input(f"Enter the number for the new status: "))
            return new_status
        except:
            print("You must enter just a number from the list above")
            self.select_valid_status()

    def update_status(self):
            selected_list = self.get_csv_and_return_as_list_of_dict()
            valid_inputs = self.gen_valid_inputs()
            self.show_items()
            print(f"""Enter the number for the {self.type[:-1]} you want
        to update or x to go to main menu: """)
            updatee = input()
            updatee = self.check_valid_input(updatee, valid_inputs)
            updatee = int(updatee)
            updatee_as_dict = selected_list[updatee]
            new_status = self.select_valid_status()
            updatee_as_dict["status"] = new_status
            file_to_open = Path(rf"data/{self.type}.csv")
            with open(file_to_open, "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                list_of_records = (list(records))
            list_of_records[int(updatee)] = updatee_as_dict

            with open(file_to_open, "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writeheader()
                for dictio in list_of_records:
                    writer.writerow(dictio)
            print(f"{self.type[:-1]} {updatee+1} has been updated")


    def collect_attributes(self) -> dict:
        updatee_as_dict = self.as_dict()
        for key, value in updatee_as_dict.items():
            if key == "status":
                updatee_as_dict[key] = "1"
            elif key == "courier":
                updatee_as_dict[key] = self.choose_courier_for_order()
            elif key == "items":
                updatee_as_dict[key] = self.choose_items_for_order()
                if updatee_as_dict[key] == "Cancel order due to no item choice":
                    self.item_menu()
            else:
                key_4_string = key.replace("_", " ").title()
                newValue = input(f"Enter the {key_4_string} ")
                while newValue == "":
                    newValue = input("Not a valid value. Enter another: ")    
                updatee_as_dict[key] = newValue
        return  updatee_as_dict


    def choose_courier_for_order(self) -> int:
        an_item = Courier()
        an_item.show_items()
        valid_inputs = an_item.gen_valid_inputs()
        chosen_item = input("Enter the number for your courier of choice: ")
        chosen_item = an_item.check_valid_input(chosen_item,valid_inputs, from_orders = True)
        return int(chosen_item + 1) #+1 to keep consistent with number shown in list

    def choose_items_for_order(self) -> str:
        an_item = Product()
        an_item.show_items()
        valid_inputs = an_item.gen_valid_inputs()
        valid_inputs.append("d")
        item_list_as_str = ""
        while True:
            chosen_item = input("Enter the number for a product you want or d if you are done: ")
            if chosen_item == "d" and item_list_as_str == "":
                print("\n\n\nAn order must contain at least one item.\n\n\n")
                time.sleep(1)
                return "Cancel order due to no item choice"
            elif chosen_item == "d":
                break
            chosen_item = an_item.check_valid_input(chosen_item,valid_inputs, from_orders = True)
            item_list_as_str += str(chosen_item +1) + "," #Plus one needed to keep consistent with number in printed list
        if chosen_item != "":
            return item_list_as_str[:-1] 

 

#MAIN MENU

def menu():
    main_menu_string = """Choose an option:
0 to exit
1 for seeing the products menu
2 for seeing the courier menu
3 for seeing the order menu"""
    print(main_menu_string)
    try:
        user_input = input()
        print("")
        counter = 0
        while user_input not in ("0", "1", "2", "3") and counter < 5:
            print("Not a valid option. Try again.")
            print(main_menu_string)
            user_input = input()
            counter+=1
            print("")
        if user_input == "0" or counter == 5:
            if counter == 5:
                print("Too many invalid inputs")
            sys.exit(0)
        elif user_input == "1":
            print("")
            product = Product()
            product.item_menu()
        elif user_input == "2":
            print("")
            courier = Courier()
            courier.item_menu()
        elif user_input == "3":
            print("")
            order = Order()
            order.item_menu()
    except BaseException  as e:
        print("Thank you for using our CLI")
        return e




menu()

