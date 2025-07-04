class Item:
  def __init__(instance, product, qty):
    instance.stock = {
      "product" : product,
      "qty" : qty
    }
    instance.not_defined_attribute = "This wasn't passed into the parameters, but it's part of the class"

item1 = Item("iPhone",8)

item1.not_defined_attribute
# stock = {
#       "brand" : "Apple",
#       "product" : "iPhone",
#       "qty" : 5
#     }

# stock["qty"] +=2
# stock["qty"] +=2

# print(stock)


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.cart = []

#     def add_to_cart(self, product):
#         self.cart.append(product)
#         print(f"{product.name} added to {self.username}'s cart.")

# # ---- Usage ----
# p1 = Product("Book", 10.99)
# p2 = Product("Pen", 1.50)

# u1 = User("bruno")
# u1.add_to_cart(p1)
# u1.add_to_cart(p2)

