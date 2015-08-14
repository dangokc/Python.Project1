class ShoppingCart:
    # Class constructor
    def __init__(self):
        self.items = []  # Array items

    # Function to add item into items array
    def addtocart(self, item):
        self.items.append(item)

    # Function to remove item from items array
    def removefromcart(self, item_index):
        self.items.pop(item_index)

    # Function to get the price of all items in Cart
    def pricecart(self):
        price = 0
        for x in self.items:
            price += x.price
        return price

    # Function to list all items in Cart with name, price and id
    def list_cart(self):
        cid = 0
        print("Cart Items: ")
        for x in self.items:
            print(x.name, x.price, cid)
            cid += 1
        print("")


