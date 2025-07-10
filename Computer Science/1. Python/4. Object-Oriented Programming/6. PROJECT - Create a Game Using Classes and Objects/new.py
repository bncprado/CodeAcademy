class Shop:
  
  def __init__(self, brand, model, qty):
    self.brand = brand
    self.model = model
    self.qty = qty
    
  def __repr__(self):
    return f"Shop(brand='{self.brand}', model='{self.model}', qty={self.qty})"
    
  def add_stock(self, qty):
    self.qty += qty
    print(f"You've added {qty} pieces of {self.brand}'s {self.model} to your stock")

  def remove_stock(self, qty):
    self.qty -= qty
    print(f"You've removed {qty} pieces of {self.brand}'s {self.model} to your stock")

  def check_stock(self,shopper):
    if isinstance(shopper,Shopper):
      print (f"Hi {shopper.first_name}. We have {self.qty} pieces of {self.brand}'s {self.model} in your stock")
      return self.qty
    else:
      print(f"{shopper} is not registered")
      exit()

  def list_inventory(self):
    print(f"{self.brand} {self.model}: {self.qty} in stock")

class Shopper:
  
  def __init__(self, first_name, last_name, username):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.basket = []

  def __repr__(self):
    return f"Shopper(first_name='{self.first_name}', last_name='{self.last_name}', username='{self.username}', basket={self.basket})"

  def add_to_basket(self,item,qty):
    if isinstance(item,Shop):
      if qty > item.qty:
        print(f"We have only {item.qty} {item.brand} {item.model} available in stock. Please, adjust the quantity")
      else:
        for brand_model_qty in self.basket:
          if item.brand == brand_model_qty[0] and item.model == brand_model_qty[1]:
            brand_model_qty[2] += qty
            item.remove_stock(qty)
            
            return
        self.basket.append([item.brand, item.model, qty])
        item.qty -= qty 
    else:
      print(f"{item.capitalize()} is not in our inventory")
 
  def remove_from_basket(self,item,qty):
    if isinstance(item,Shop):
      for brand_model_qty in self.basket:
          if brand_model_qty[0] == item.brand and brand_model_qty[1] == item.model and brand_model_qty[2] >= qty:
            brand_model_qty[2] -= qty
            item.add_stock(qty)
            return
          elif brand_model_qty[0] == item.brand and brand_model_qty[1] == item.model and brand_model_qty[2] < qty:
            print(f"You have only {brand_model_qty[2]} {brand_model_qty[0]}\'s {brand_model_qty[1]} in your basket. You can't remove {qty} of them")
    else:
      print(f"{item.capitalize()} is not in our inventory")

  def change_username(self,username):
    print(f"The username {self.username} has now been changed to {username}")
    self.username = username
    


item1 = Shop("Apple", "iPhone", 20)
item2 = Shop("Samsung","Galaxy",20)
shopper1 = Shopper("Bruno","Prado","bncprado")
shopper2 = Shopper("Bruna", "Zanotto", "brunet_tza")

item1.add_stock(10)
item2.add_stock(10)
print(item1.qty)
print(item2.qty)
item1.remove_stock(10)
item2.remove_stock(10)
print(item1.qty)
print(item2.qty)
item1.check_stock(shopper1)
item1.check_stock(shopper2)

shopper1.add_to_basket(item1, 12)
print(shopper1.basket)
shopper2.add_to_basket(item1,8)
print(shopper2.basket)
shopper1.add_to_basket(item2, 12)
print(shopper1.basket)
shopper2.add_to_basket(item2,1)
print(shopper2.basket)

shopper1.remove_from_basket(item1, 12)
print(shopper1.basket)
shopper2.remove_from_basket(item1,8)
print(shopper2.basket)
shopper1.remove_from_basket(item2, 12)
print(shopper1.basket)
shopper2.remove_from_basket(item2,1)
print(shopper2.basket)

shopper1.change_username("alfredo")
print(shopper1.username)

shopper2.change_username("zequinha")
print(shopper2.username)

