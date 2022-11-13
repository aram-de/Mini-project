import json
import ast
import os.path
import csv

class Menu():

    def menu():
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
            product_menu()
        elif u_input == "2":
            print("")
            courier_menu()
        elif u_input == "3":
            print("")
            order_menu()

    def get_couriers():
        couriers = []
        with open("data\couriers.txt", "r+") as courierf:
            for line in courierf:
                couriers.append(line.strip("\n"))
        return couriers


        
class Item():
    # def __init__(self) -> None: 

    def get_headers(self) -> list:
        #TODO each object order, courier or product has an attribute header
        file_exists = os.path.isfile(f"data\{self.type}.csv")
        if not file_exists and self.type == "orders":
            field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items']
        elif not file_exists and self.type == "couriers":
            field_names = ['name', 'phone']
        elif not file_exists and self.type == "products":
            field_names = ['name', 'price']
        else:
            with open(f"data\{self.type}.csv", "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                field_names = records.fieldnames
                print(len(list(records)))
                print(field_names)
        return field_names
    

    def get_csv_and_return_as_list_of_dict(self) -> list:
        list_of_dict = []
        with open(f"data\{self.type}.csv", "r") as csv_file:
            records = csv.DictReader(csv_file, skipinitialspace=True)
            for row in records:
                list_of_dict.append(row)
        return list_of_dict

    def show_items(self) -> None:
        list_of_dict = get_csv_and_return_as_list_of_dict(self.type)
        for num, line in enumerate(list_of_dict):      
            print(f"{self.type[:-1].capitalize()} n.{num}")
            for key, value in line.items():
                key = key.replace("_", " ").strip().title()
                print(f"\t{key}: {value}")
            print("")

    def gen_valid_inputs(self) -> list:
        list_of_dict = get_csv_and_return_as_list_of_dict(self.type)
        valid_input = [str(num) for num, line in enumerate(list_of_dict)] 
        #TODO there must be a way to do with without the unused line variable
        valid_input.append("x")
        return valid_input

        
        #TODO each object order, courier or product has an attribute header
        #TODO each object has a method to create a new one that collects the relevant values
    def asdict(self):
        pass

    def add_item_to_file(self): 
#TODO this function does not add a line the previous line does not have a break line character
        file_exists = os.path.isfile(f"data\{self.type}.csv")
        #field_names = self.get_headers()
        an_item = self.asdict()
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


    def check_valid_input(user_input : str, valid_inputs : list, item_type : str) -> str: 
        while user_input not in valid_inputs and user_input.capitalize() != "X" :
            print("Your choice was not valid or x to go back to the main menu.")
            user_input = input(f"Please, choose a {item_type} by entering their corresponding number above: ")
        if user_input.lower() == "x":
            return ""
        else:
            return user_input




    def check_existing_input(user_input : str, selected_list : list, item_type : str) -> str: 
        while user_input in selected_list and user_input.capitalize() != "X" :
            print(f"That {item_type} already exists.")
            user_input = input(f"Please, enter a new {item_type} or x to return to the main menu: ")
        if user_input.lower() == "x":
            return ""
        else:
            return user_input



    def update_item(self):
        print("")
        valid_inputs = show_items_and_gen_valid_inputs(selected_list, name_of_selected_list)
        print(f"Enter the number for the {name_of_selected_list[:-1]}you want to replace: ")
        replacee = input()
        replacee = check_valid_input(replacee, valid_inputs, name_of_selected_list[:-1])        
        if replacee == "":
            menu()
        else:
            replacement = input(f"Enter the {name_of_selected_list[:-1]}you want to replace your choice with: ")#
            replacement = check_existing_input(replacement, selected_list, name_of_selected_list)

            if replacement == "":
                menu()
            else:
                old_item = selected_list[int(replacee)]
                with open(f"data\{name_of_selected_list}.txt", "r") as itemsf:
                    lines = itemsf.readlines()
                if int(replacee) == len(lines)-1:
                    lines[int(replacee)] = f"{replacement}"
                else:
                    lines[int(replacee)] = f"{replacement}\n"
                print(f"{old_item} has replaced {lines[int(replacee)]}")
                with open(f"data\{name_of_selected_list}.txt", "w") as itemsf:
                    itemsf.writelines(lines)
    


    def delete_item(selected_list, name_of_selected_list):
        print("")
        valid_input = show_items_and_gen_valid_inputs(selected_list, name_of_selected_list)
        print("")
        print("Enter the number for the item you want to delete: ")
        deletee = input()
        deletee = check_valid_input(deletee, valid_input, name_of_selected_list[:-1])
        if deletee == "":
            menu()
        else:
            with open(f"data\{name_of_selected_list}.txt", "r") as itemsf:
                lines = itemsf.readlines()
                del lines[int(deletee)]
            with open(f"data\{name_of_selected_list}.txt", "w") as itemsf:
                for pos, line in enumerate(lines):
                    #needed because otherwise deleting the last item would add a blank like
                    if pos == len(lines)-1:
                        itemsf.write(line.strip())
                    else:
                        itemsf.write(line)
            print(f"{name_of_selected_list[:-1]}number {deletee} is now deleted.")
            menu()

    
    def item_menu():
        couriers = []
        with open("data\couriers.txt", "r+") as courierf:
            for line in courierf:
                couriers.append(line.strip("\n"))
        courier_menu_string = """Choose an option:
    0 to go to main menu
    1 for seeing the list of couriers
    2 to add a new courier
    3 to update/replace a courier
    4 to delete a courier"""
        print(courier_menu_string)
        u_input2 = input()
        while u_input2 not in ("0","1","2","3","4"):
            print("Not a valid option. Try again.") 
            print(courier_menu_string)        
            u_input2 = input()
        if u_input2 == "0":
            menu()
        elif u_input2 == "1":
            show_items_and_gen_valid_inputs(couriers, "couriers")
            print("")
            courier_menu()
        elif u_input2 == "2":
            print(create_new_item(couriers, "couriers"))
            print("")
            courier_menu()
        elif u_input2 == "3":
            update_item(couriers, "couriers")
            print("")
            courier_menu()
        elif u_input2 == "4":
            delete_item(couriers, "couriers")
            print("")
            courier_menu()

class Courier(Item):
    def __init__(self) -> None:
        self.type = "couriers"
        self.name = "Peter"
        self.phone = "Some address"
        self.field_names = ['name', 'phone']

    
    def asdict(self):
        return {'name': self.name, 'phone': self.phone}


class Product(Item):   
    def __init__(self) -> None:
        self.type = "products"
        self.name = "ProductName"
        self.price = 83475.1
        self.field_names = ['name', 'price']

    
    def asdict(self):
        return {'name': self.name, 'price': self.price}
        
class Order(Item):
    def __init__(self) -> None:

        # order = {}
        # order["customer_name"] = input("Enter the customer name: ")
        # order["customer_address"] = input("Enter the customer address: ")
        # order["customer_phone"] = input("Enter the customer phone: ")
        # order["status"] = "PREPARING"
        self.type = "orders"
        self.customer_name = "Peter"
        self.customer_address = "Some address"
        self.customer_phone = "666"
        self.courier = "A courier"
        self.status = "PREPARING"
        self.items = "1, 3, 5 "
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]

    def asdict(self):
        return {'customer_name': self.customer_name, 'customer_address': self.customer_address,
            'customer_phone' : self.customer_phone, 'courier' : self.courier, 'status' : self.status,
            'items' : self.items}

        # couriers = get_couriers()
        # valid_inputs = show_items_and_gen_valid_inputs(couriers, "couriers")
        # chosen_courier= input("Pleanse, choose a courier by entering their corresponding number above: ")
        # chosen_courier = check_valid_input(chosen_courier, valid_inputs, name_of_selected_list)   
        # if chosen_courier == "":
        #     print("chosen courier came empty")
        #     order_menu()
        #     return None
        # else:
        #     order["courier"] = couriers[int(chosen_courier)]
        return order

    


    def item_menu(self):
        orders = []
        with open("data\orders.txt", "r+") as orderf:
            for line in orderf:
                orders.append(line.strip("\n"))
        order_menu_string = """Choose an option:
    0 to go to main menu
    1 for seeing the list of orders
    2 to add a new order
    3 to update order status
    4 to to change an order
    5 to delete an order"""
        print(order_menu_string)
        u_input2 = input()

        while u_input2 not in ("0","1","2","3","4","5"):
            print("Not a valid option. Try again.") 
            print(order_menu_string)        
            u_input2 = input()
            
        if u_input2 == "0":
            menu()
        elif u_input2 == "1":
            show_items_and_gen_valid_inputs(orders, "orders")
            print("")
            order_menu()
        elif u_input2 == "2":
            print(create_new_item(orders, "orders"))
            print("")
            order_menu()
        elif u_input2 == "3":
            update_order(orders, "orders", True)
            print("")
            order_menu()
        elif u_input2 == "4":
            update_order(orders, "orders")
            print("")
            order_menu()
        elif u_input2 == "5":
            delete_item(orders, "orders")
            print("")
            order_menu(orders, "orders")

    def update_item(self, selected_list, name_of_selected_list, status = False):
        valid_input = show_items_and_gen_valid_inputs(selected_list, name_of_selected_list)
        print(f"""Enter the number for the {name_of_selected_list[:-1]}you want
to update or x to go to main menu: """)
        updatee = input()
        while updatee not in valid_input:
            print(f"Not a valid option. Try again.\nChoose an option:")
            updatee = input(f"""Enter the number for the {name_of_selected_list[:-1]}you want
to update or x to go back to main menu: """)        
        if str(updatee).lower() == "x":
            menu()
        else:
            updatee_str = selected_list[int(updatee)].replace("'", "\"")
            updatee_as_dict = json.loads(updatee_str)
        
        
        if status: #If we are updating the status, comes passed from the order menu as optional param
            new_status = input(f"Enter the new status: ")
            if new_status.strip() != "":
                updatee_as_dict["status"] = new_status
        
        else:
            name = input("Enter the customer name: ")
            if name.strip() != "":
                updatee_as_dict["customer_name"] = name
            address = input("Enter the customer address: ")
            if address.strip() != "":
                updatee_as_dict["customer_address"] = address
            phone = input("Enter the customer phone: ")
            if phone.strip() != "":
                updatee_as_dict["customer_phone"] = phone
            
            couriers = get_couriers()
            valid_inputs = show_items_and_gen_valid_inputs(couriers, "courier")
            chosen_courier= input("Pleanse, choose a courier by entering their corresponding number above: ")
            chosen_courier = check_valid_input(chosen_courier, valid_inputs, "courier")
            if chosen_courier == "":
                order_menu()
            else:
                updatee_as_dict["courier"] = couriers[int(chosen_courier)]
        
        
        with open(f"data\{name_of_selected_list}.txt", "r") as itemsf:
                lines = itemsf.readlines()
        if int(updatee) == len(lines)-1:
            lines[int(updatee)] = str(updatee_as_dict)
        else:
            lines[int(updatee)] = f"{str(updatee_as_dict)}\n"
        with open(f"data\{name_of_selected_list}.txt", "w") as itemsf:
                itemsf.writelines(lines)
        print(f"Order {lines[int(updatee)]} has been updated")

# anOrder = Order()
# anOrder.add_item_to_file()


aProduct = Product()
aProduct.add_item_to_file()

# aCourier = Courier()
# aCourier.add_item_to_file()


# aMenu = menu()
# aMenu.menu()







    
        

 #   menu()


# def test_always_passes():
#     assert True

# def test_always_fails():
#     assert False