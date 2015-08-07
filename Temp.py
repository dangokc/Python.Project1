make_store_items(3)
for x in store:
    print(x.name, x.price)

# def createstore(storefile):
#     try:
#         fx = open(storefile, "r")
#         str1 = ""
#         str1 = fx.read()
#     except IOError:
#         print("No Existing Store... generating items")
#         make_store_items(4)
#
# def liststore():
#     iid = 0
#     for x in store:
#         print(iid, x.name, x.price)
#         iid += 1
#
# make_store_items(3)__author__ = 'Huy'
