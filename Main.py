from random import randint  # Import randint function from random class
from Item import Item  # Import Item class from Item.py
from ShoppingCart import ShoppingCart  # Import ShoppingCart class from ShoppingCart.py

# Keep track of the program process
done = False

# Store array to store the Store's items
store = []

# Store item's names
itemNames = ["HDMI cable", "Keyboard", "Headphone", "RAM", "Mouse", "USB", "HDD", "CD_ROM", "Monitor"]

# Function to generate random store's items
def make_store_items(amt):
    storeitems = 0
    while storeitems <= amt:
        # 1@param: generate a random number from 1 to 50
        # 2@param: generate a random name getting from itemNames array
        item = Item(randint(1, 50), itemNames[randint(0, len(itemNames) - 1)])  # Creat Item
        store.append(item)  # Add item to store
        storeitems += 1  # Keep track of the amt

# Function to Build a Store
def creat_store(storefile):
    # If Python can't find a storefile it will throw an exception
    try:
        fx = open(storefile, "r")
        str1 = ""
        str1 = fx.read()
    except IOError:
        print("No Existing Store... generating items")
        make_store_items(4)

# Function to list items of Store
def list_store():
    iid = 0
    for x in store:
        print(iid, x.name, x.price)
        iid += 1

# Function to print a menu to user
def print_menu():
    print("Type C to view cart items")
    print("Type R to view cart items")
    print("Type an item number to buy it")
    print("Type P to get the total price")

# Function to handle what user input
def handle_input(in_var, cart):
    char_inputs = ["C", "R", "P"]

# creat_store("myfile")
# make_store_items(4)
# list_store()
#
# cart1 = ShoppingCart()
# createstore("cart1.cartfile")
# while(done == False):
#     liststore()

