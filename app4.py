import os.path
import csv
from Item import Item

class Courier(Item):
    def __init__(self) -> None:
        self.type = "couriers"
        self.name = ""
        self.phone = ""
        self.field_names = ['name', 'phone']

    
    def asdict(self):
        return {'name': self.name, 'phone': self.phone}


#NEW CLASS HERE

class Product(Item):   
    def __init__(self) -> None:
        self.type = "products"
        self.name = ""
        self.price = 0
        self.field_names = ['name', 'price']

    
    def asdict(self):
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
        self.status = ""
        self.items = ""
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]

    def asdict(self):
        return {'customer_name': self.customer_name, 'customer_address': self.customer_address,
            'customer_phone' : self.customer_phone, 'courier' : self.courier, 'status' : self.status,
            'items' : self.items}
        
    def update_status(self):
            selected_list = self.get_csv_and_return_as_list_of_dict()
            valid_inputs = self.gen_valid_inputs()
            self.show_items()
            print(f"""Enter the number for the {self.type[:-1]} you want
        to update or x to go to main menu: """)
            updatee = input()
            self.check_valid_input(updatee, valid_inputs)
            updatee = int(updatee)-1
            updatee_as_dict = selected_list[updatee-1]
            new_status = input(f"Enter the new status: ")
            if new_status.strip() != "":
                updatee_as_dict["status"] = new_status
            with open(r"data\{self.type}.csv", "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                list_of_records = (list(records))
            list_of_records[int(updatee)] = updatee_as_dict

            with open(f"data\{self.type}.csv", "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writeheader()
                for dictio in list_of_records:
                    writer.writerow(dictio)
            print(f"{self.type[:-1]} {updatee} has been updated")


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

    def add_item_to_file(self): 
#TODO this function does not add a line the previous line does not have a break line character
        file_exists = os.path.isfile(f"data\{self.type}.csv")
        #field_names = self.get_headers()
        an_item = self.update_attributes()
        #print("data file empty is", data_file.empty)                
        if file_exists and os.stat(f"data\{self.type}.csv").st_size != 0: #file exists and it is not empty
            with open(f"data\{self.type}.csv", "a", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writerow(an_item)
        else: #file either does not exist or is emtpy
            with open(f"data\{self.type}.csv", "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writeheader()
                writer.writerow(an_item)

 

#NEW CLASS STARTS BELOW

class Menu():

    def menu(self):
        main_menu_string = """Choose an option:
    0 to exit
    1 for seeing the products menu
    2 for seeing the courier menu
    3 for seeing the order menu"""
        print(main_menu_string)
        u_input = input()
        print("")
        while u_input not in ("0", "1", "2", "3"):
            print("Not a valid option. Try again.")
            print(main_menu_string)
            u_input = input()
            print("")
        if u_input == "0":
            exit("Program ended")
        elif u_input == "1":
            print("")
            a_product = Product()
            a_product.item_menu()
        elif u_input == "2":
            print("")
            a_courier = Courier()
            a_courier.item_menu()
        elif u_input == "3":
            print("")
            an_order = Order()
            an_order.item_menu()


aMenu = Menu()
aMenu.menu()