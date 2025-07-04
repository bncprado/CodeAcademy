class Stock:
  def __init__(self, brand, product, qty):
    # self.brand = brand
    # self.product = product
    # self.qty = qty
    self.stock = {
      "brand" : brand,
      "product" : product,
      "qty" : qty
    }

  def check_username(self,user):
    if not isinstance(user, Username):
      print(f"{user} not existent")
    else:
      print(f"{user.username} is a registered employee")

  def log_purchase(self,user,brand,product,qty):
    if isinstance(user,Username):
      self.stock["brand"] = brand
      self.stock["product"] = product
      self.stock["qty"] +=qty
    else:
      print("User not registered. Program will quit")
      exit()

  def log_sell(self,user,brand,product,qty):
    if isinstance(user,Username):
      self.stock["brand"] = brand
      self.stock["product"] = product
      self.stock["qty"] -=qty
    else:
      print("User not registered. Program will quit")
      exit()

  def __repr__(self):
    pass

class Username:
  def __init__(self, first_name, last_name, username, password, ):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.password = password

  def buy_stock(self):
    pass

  def sell_stock(self):
    pass

  def check_stock(self):
    pass

  def __repr__(self):
    pass

user1 = Username("Bruno", "Prado", "bncprado", "123321")

stock1 = Stock("Apple", "iPhone", 2)


stock1.log_purchase(user1,"Apple","iPhone",7)
print(stock1.stock)
stock1.log_purchase(user1,"Apple","iPhone",1)
print(stock1.stock)
stock1.log_sell(user1,"Apple","iPhone",2)
print(stock1.stock)



# stock1.log_sell("user1","Apple","iPhone",3)
# print(stock1.stock)