
# Mini-project

## Generation's Data Engineering Bootcamp Mini Project

This project is intended to be a CLI management system for ordering from a pop-up cafe place. The requirements changed weekly in order to both represent changing requirements from a client and also support our learning journey by adding complexity as we progressed.

# Requirements

## Week 1

 - create a product (string) and add it to a list
 - view all products with an index attached
 - STRETCH update or delete a product using an index value to choose

Because during a presentation we were told that the program should be able to handle invalid input, I implemented a 7 function version of it that did input validation inside each function that took inputs (should have done try and catch for simplicity's sake, but at some point someone (in a previous life and probably when writing Java) told me off for using try and catch because of it being very inefficient and I carried that thought with me) .

## Week 2 

 - create a product, **courier or order** and add it to a list
 - view all products, **couriers or orders** index attached
 - **add data persitence** using text files
 - STRETCH  update or delete a product, **courier or order** by choosing its index

Orders were required to be stored as dictionaries with the following structure
{ 
"customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334", 
 "status": "preparing" 
 }

There was some confusion this week because we got two different sets of requirements.

Added the functions to add, update and delete couriers and orders and added code to read and write from/to text files. I should have turned that code into its own function, but did not. 

The function to create and update orders had a line of code for each key and assigned an input as the value for those keys.  

Refactored some of my code by separating the code to generate a list of valid inputs and check if the input was valid into a single function.

## Week 3 

 - create a product, courier or order and add it to a list
 - view all products, couriers or orders 
 - add data persistence using text files
 **- update the status of an order**
 - STRETCH update or delete a product, courier or order by index

Modified the functions to create or update orders by adding an additional optional parameter with "status" with the default value "False", this allowed me to reuse that function to change only the status if the function call included True as the value for the "status" parameter.

This week I realised I had to let the customer **choose the courier using an index** instead of typing the name of their choice. This was **implicit in the pseudocode** of the update for week 2 that I had overseen until this point. Not sure if that makes it a requirement.

On this week I decided that showing an index zero in my menus for the lists of order, couriers and products was unsightly, so I modified the code so that it would start the count at 1. 

This had huge consequences throughout my code for two reasons:

 - I had to adjust whenever I took an input to select by index by subtracting one so that the displayed choice would match the actual index choice.
Eg: 
Menu displays: 
	 - 1. Melon
   
	 - 2. Coke

	Actual list index positions are 0 for Melon and 1 for Coke, so if the client enters 1 because they chose Melon, I need to pass zero to functions.
	
2. I had to do many data type changes since I had been using strings for many numeric values that I initially had not thought I would have to do any calculations with. 

The dance of subtracting one or adding one to keep values appropriate for each function and the UI and moving from strings to integers triggered bugs that took too long to sort out (famous in my home 8 hours of coding on the down low on a Sunday). 

## Week 4
 - create a product, courier or order and add it to a list
 - view all products, couriers or orders 
 - add data persistence using **csv files**
 - update the status of an order
 - **BONUS list orders by status or courier**

This week I decided to attempt making my project object oriented, since there was only the implementation of CSV files as storage was a new requirement. I decided to pass on the listing orders by status or courier for the time being.

I decided I would create a menu class, an item class that would have some abstract methods and most of the methods needed and then have a class for order, product and courier.

In hindsight, I should have created a class list of Items and then list of products, list of couriers and list of orders. This would have prevented the logical weirdness of having to create an empty object order/courier/product before being able to do anything, while creating an empty list would have make sense and some of the methods I created (or should have created) make more sense in the context of a list (delete, writing to file, reading from file).

The move to CSV again caused problems with the line numbers, which is linked to the index values so hell broke loose again with my input validation which at this point is two functions, one that produces the valid inputs and one that checks that the input is valid.

## Week 5
As of 2022-11-16

Without new requirement yet, I have moved to do testing using pytest. ~~I have broken down my main file into a file for the Item class, which is too long~~ and created a file to test the courier class.

As of 2022-11-17

Breaking the file into parts resulted in circular import hell, so everything is back to a huge ugly file. 

As of 2022-11-22

We received the requirements for week 5. It they were to

-**add an index to each item**. Although this seems relatively easy to implement, this week and week six were optional and I decided to focus on trying to implement my program using a repository pattern.

-**read and write the data to and from a database for products and couriers.** This seemed more challenging and interesting, but being optional I also left it aside. 

## Week 6

As of 2022-11-22

The new requirement was to **use a database to store the persistent data for orders too**. Once more, this requirement was optional and I decided to leave it aside to focus on implementing the repository pattern. 

Unfortunately, I was not able to implement the repository pattern successfully. 

## Approach to meet requirements

I read the requirements section that were weekly delivered to us and tried to have a function for each thing that the software was supposed to do. 

This proved to be a poor strategy since there were some "requirements" that were implicit in the pseudocode and I had to reimplement some functions based on the pseudocode.

![UML diagram showing the classes I used](https://i.ibb.co/GT3qVb0/architecture.jpg)

If you check the graphic above you can see that I have methods to perform all the functions required by the "client" 

1. show_items: displays the items be it orders, products or couriers.
2. add_item_to_file: adds a new item and stores it persistently.
3. delete_items: deletes an item and stores that deletion persistently.
4. update_item: allows you to update an item and stores it persistently.

Specifically for the order class it was required that you can update the status of an order, add or update the courier and add items for the order all of them by choosing an index from a list. These features are supported by the following methods

  1. select_valid_status
   2. choose_courier_for_order
   3. choose_items_for_order

There are obviously other methods in place which help the methods that perform the functions required by the "client".


## Desired improvements (TODO?)
As of 2022-11-22 

I have restarted this program several times trying to implement a repository pattern, but ended up with circular imports and short on time to fix them.

Separate reading and writing from and to file to its own function. This I actually implemented in the failed repository pattern implementation and would like to backport it to this version.

Break the massive single file program into several file for more comfortable editing. Again something that I attempted too late and resulted in circular imports.

Refactor to use integers for all menu options to avoid so many (possibly all) back and forth changes between data types. This was achieved in the failed attempt to do a repository pattern version of the project.

Refactor to use try, excepts to validate my data. I started doing this in the failed repository pattern version of the project. I thought it would simplify data validation hugely, but it also resulted in some limitations that I had not foreseen. For example, challenging behaviour if you tried to recursively call a method in the exception. 

It would be nice to complete the requirements from weeks five and six and the optional requirements that I abandoned along the way.

Since I have talked quite a bit about the failed attempt to use the repository pattern, I have uploaded it in case anyone is curious. It can be found here 

https://github.com/aram-de/failedRepositoryPattern


## TECHNOLOGIES

 1. Python (required by "client")  Database (mysql running on a docker)
  2. Optional and not currently implemented.

## Most enjoyed

Moving to an OOP implementation. Even though the architecture is poor and shows my lack of knowledge of architectural patterns, there was a certain satisfaction in doing OOP after 7 years without touching it. Plus I felt a bit smug inheriting all those methods.
