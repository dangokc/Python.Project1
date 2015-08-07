class ShoppingCart:
    def __init__(self):
        self.items = []
    def addtocart(self, item):
        self.items.append(item)
    def removefromcart(self, item_index):
        self.items.pop(item_index)
    def pricecart(self):
        price = 0
        for x in self.items:
            price += x.price
        return price
    def list_cart(self):
        cid = 0
        print("Cart Items: ")
        for x in self.items:
            print(x.name, x.price, cid)
            cid += 1
        print("")


