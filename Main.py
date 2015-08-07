__author__ = 'Huy'

from random import randint
from Item import Item
from ShoppingCart import ShoppingCart

done = False

store = []
itemNames = ["HDMI cable", "keyboard", "headphone", "RAM"]
def make_store_items(amt):
    storeitems = 0
    while storeitems <= amt:
        n_item = Item(randint(1, 50), itemNames[randint(0, len(itemNames))])
        store.append(n_item)
        storeitems += 1

def createstore(storefile):
    try:
        fx = open(storefile, "r")
        str1 = ""
        str1 = fx.read()
    except IOError:
        print("No Existing Store... generating items")
        make_store_items(4)

def liststore():
    iid = 0
    for x in store:
        print(iid, x.name, x.price)
        iid += 1

def printMenu():
    print("Type C to view cart items")
    print("Type R to view cart items")
    print("Type an item number to buy it")
    print("Type P to get the total price")

def handleInput(in_var, cart):
    char_inputs = ["C", "R", "P"]


# make_store_items(4)
# liststore()
#
# cart1 = ShoppingCart()
# createstore("cart1.cartfile")
# while(done == False):
#     liststore()

