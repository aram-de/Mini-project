import csv

def get_csv_and_return_as_list_of_dict(item_type) -> list:
    list_of_dict = []
    try:
        with open(rf"data\{item_type}.csv", "r") as csv_file:
            records = csv.DictReader(csv_file, skipinitialspace=True)
            for row in records:
                list_of_dict.append(row)
        return list_of_dict
    except:
        print(rf"Failed to load data requested. Try adding one {item_type} first.")



class Order():
    def __init__(self) -> None:
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]
        self.name = "orders"


#class item_container():

#class     
orders_list = get_csv_and_return_as_list_of_dict("orders")



couriers_list = get_csv_and_return_as_list_of_dict("couriers")
products_list = get_csv_and_return_as_list_of_dict("products")
oder_status_list = ['Preparing', 'Waiting for courier', 'On its way', 'Delivered', 'Delivery failed']

def write_list_of_dict_to_csv(item_list : list, item_type : str):
    try:
        with open(rf"data\{item_type}.csv", "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= item_list[0].keys())
            writer.writeheader()
            for dictio in item_list:
                writer.writerow(dictio)
    except:
        print(rf"Failed to load data requested. Try adding one {item_type} first.")

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

class itemMenu:
    #this should be able to get an item list
    #add a product to the list -> returns a list with an additional item
    #select a product -> returns an index position for an item
    #delete a product from the list -> returns a list without the deleted product
    #update a product -> returns a product as dict




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
            print("")
            valid_choices = [num for num in range(5)]
            print(valid_choices)
            while u_input not in valid_choices:
                print("Not a valid option. Try again.")
                print(main_menu_string)
                u_input = int(input())
                print("")
            if u_input == 0:
                return("Program ended st")
                #exit("Program ended")
            elif u_input == 1:
                #print("Opened product menu")
                return "Opened product menu"
                # a_product = "Product()"
                # a_product.item_menu()
            elif u_input == 2:
                print("")
                a_courier = "Courier()"
                a_courier.item_menu()
            elif u_input == 3:
                print("")
                an_order = "Order()"
                an_order.item_menu()
        except:
            print("Invalid input")
            return "Invalid input"
 

#aCourier = Courier()
# aMenu = Menu()
# aMenu.menu()