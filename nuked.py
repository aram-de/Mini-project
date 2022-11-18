import csv
import sys

# def get_csv_and_return_as_list_of_dict(item_type) -> list:
#     list_of_dict = []
#     try:
#         with open(rf"data\{item_type}.csv", "r") as csv_file:
#             records = csv.DictReader(csv_file, skipinitialspace=True)
#             for row in records:
#                 list_of_dict.append(row)
#         return list_of_dict
#     except:
#         print(rf"Failed to load data requested. Try adding one {item_type} first.")



class Order():
    def __init__(self) -> None:
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]
        self.name = "orders"


#class item_container():

#class     
# orders_list = get_csv_and_return_as_list_of_dict("orders")



# couriers_list = get_csv_and_return_as_list_of_dict("couriers")
# products_list = get_csv_and_return_as_list_of_dict("products")
# oder_status_list = ['Preparing', 'Waiting for courier', 'On its way', 'Delivered', 'Delivery failed']

# def write_list_of_dict_to_csv(item_list : list, item_type : str):
#     try:
#         with open(rf"data\{item_type}.csv", "w", newline='') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames= item_list[0].keys())
#             writer.writeheader()
#             for dictio in item_list:
#                 writer.writerow(dictio)
#     except:
#         print(rf"Failed to load data requested. Try adding one {item_type} first.")

#write_list_of_dict_to_csv([ {'name' : "melon", 'age' : 3},  {'name' : "melon2", 'age' : 23}], 'orders')





# class Menu():

#     def menu(self):
#         main_menu_string = """Choose an option:
#     0 to exit
#     1 for seeing the products menu
#     2 for seeing the courier menu
#     3 for seeing the order menu"""
#         print(main_menu_string)
#         try:
#             u_input = int(input())
#             print("")
#             valid_choices = [num for num in range(5)]
#             print(valid_choices)
#             while u_input not in valid_choices:
#                 print("Not a valid option. Try again.")
#                 print(main_menu_string)
#                 u_input = int(input())
#                 print("")
#             if u_input == "0":
#                 print("Program ended st")
#                 exit("Program ended")
#             elif u_input == "1":
#                 print("")
#                 a_product = "Product()"
#                 a_product.item_menu()
#             elif u_input == "2":
#                 print("")
#                 a_courier = "Courier()"
#                 a_courier.item_menu()
#             elif u_input == "3":
#                 print("")
#                 an_order = "Order()"
#                 an_order.item_menu()
#         except:
#             print("Invalid input")
#             return "Invalid input"


# class Item():
#     def create_item():
#         list_of_items


#         #add item should be in list
#         #takes the list, which is self, creates new object, appends to list

# class Item_list():
#     def add_item(self):


# class Courier(Item):
#     def __init__(self) -> None:
#         self.type = "couriers"
#         self.name = input("Enter a name")
#         self.phone = input("Enter a phone number")
#         self.field_names = ['name', 'phone']
    
#     def asdict(self):
#         return {'name': self.name, 'phone': self.phone}


class Item_menu():
    def __init__(self) -> None:
        self.item_type = "orders"    
        self.content = self.get_csv_and_return_as_list_of_dict()
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]


    def get_csv_and_return_as_list_of_dict(self) -> list:
        """ as per name, if fails returns str "No file or data"""
        list_of_dict = []
        #print(f"trying to open data{self.item_type}.csv")
        try:
            with open(rf"data\{self.item_type}.csv", "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                for row in records:
                    list_of_dict.append(row)
            return list_of_dict
        except:
            return(rf"Failed to load data requested. Try adding one {self.item_type} first.")
        
    #Display products -> Returns True if it returned something? False if the list is empty?   
    
    def show_items(self) -> None:
        #list_of_dict = self.get_csv_and_return_as_list_of_dict()
        list_of_dict = self.content
        if list_of_dict == []:
            print(f"There are no {self.item_type}s currently in the system")
            return "No data on file or no file exist"
        for num, line in enumerate(list_of_dict):      
            print(f"{self.item_type[:-1].capitalize()} n.{num+1}")
            for key, value in line.items():
                key_4_string = key.replace("_", " ").title()
                print(f"\t{key_4_string}: {value}")
            print("")
        return "File content displayed"


    #add a product to the list -> returns a list with an additional item
    def add_item(self):
        new_dic = {}
        for field in self.field_names:
            new_dic[field] = input(rf"Enter a {field}: ")
        self.content = self.content.append(new_dic)
        return self.content


    #select a product -> returns an index position for an item
    #delete a product from the list -> returns a list without the deleted product
    #update a product -> returns a product as dict


    def write_list_of_dict_to_csv(self):
        try:
            with open(rf"data\{self.item_type}.csv", "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.content[0].keys())
                writer.writeheader()
                for dictio in self.content:
                    writer.writerow(dictio)
        except:
            print(rf"Failed to load data requested. Try adding one {self.item_type[:-1]} first.")





#NEW CLASS STARTS BELOW

class Menu():

    def menu(self):
        main_menu_string = """Choose an option:
    0 to exit
    1 for seeing the products menu
    2 for seeing the courier menu
    3 for seeing the order menu"""
        print(main_menu_string)
        try:
            u_input = int(input())
            valid_choices = [num for num in range(4)]
            while u_input not in valid_choices:
                print("Not a valid option. Try again.")
                print(main_menu_string)
                u_input = int(input())
                print("")
            if u_input == 0:
                sys.exit(0)
            elif u_input == 1:
                print("Opened product menu")
                return "Opened product menu"
                # a_product = "Product()"
                #a_product.item_menu()
            elif u_input == 2:
                print("")
                #a_courier = "Courier()"
                a_courier = Item_menu()
            elif u_input == 3:
                print("pass")
                pass
        except SystemExit:
            print("Thank you for using our CLI")
            return("Exited on purpose")
        except:
            print("Invalid input")
            return "Invalid input"
 

# aCourier = Courier()
aMenu = Menu()
aMenu.menu()