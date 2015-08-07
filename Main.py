__author__ = 'Huy'

from random import randint
from Item import Item
from ShoppingCart import ShoppingCart

store = []
itemNames = ["HDMI cable", "keyboard", "headphone", "RAM"]
def make_store_items(amt):
    storeitems = 0
    while storeitems <= amt:
        n_item = Item(randint(1, 50), itemNames[randint(0, len(itemNames))])
        store.append(n_item)
        storeitems += 1

# make_store_items(3)
# for x in store:
#     print(x.name, x.price)

