class Shop:
  
  def __init__(self, brand, product, qty):
    self.brand = brand
    self.product = product
    self.qty = qty
    
  def add_stock(self, qty=int):
    self.qty += qty
    print(f"You've added {qty} pieces of {self.brand}'s {self.product} to your stock")

  def remove_stock(self, qty=int):
    self.qty -= qty
    print(f"You've removed {qty} pieces of {self.brand}'s {self.product} to your stock")

  def check_stock(self):
    print (f"You have {self.qty} pieces of {self.brand}'s {self.product} in your stock")

item1 = Shop("Apple", "iPhone", 2)
item1.check_stock()
item1.add_stock(3)
item1.check_stock()
item1.remove_stock(2)

class Shopper:

  basket = {}
  def __init__(self, first_name, last_name, username):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username

  def add_to_basket(self):
    pass

  def remove_from_basket(self):
    pass

  def check_out(self):
    pass



