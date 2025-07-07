class Shop:
  
  def __init__(self, brand, model, qty):
    self.brand = brand
    self.model = model
    self.qty = qty
    
  def add_stock(self, qty=int):
    self.qty += qty
    print(f"You've added {qty} pieces of {self.brand}'s {self.model} to your stock")

  def remove_stock(self, qty=int):
    self.qty -= qty
    print(f"You've removed {qty} pieces of {self.brand}'s {self.model} to your stock")

  def check_stock(self):
    # print (f"You have {self.qty} pieces of {self.brand}'s {self.product} in your stock")
    return self.qty

class Shopper:
  

  def __init__(self, first_name, last_name, username):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.basket = [["Apple", "iPhone", 5],["Samsung", "Galaxy", 12]]

  def add_to_basket(self,item,qty):
    # if self.basket == []:
    #   self.basket.append([item.brand,item.model,qty])
    # else:
      for i in self.basket:
        if item.brand in i[0] and item.model in i[1]:
          i[2] += qty
          return
      self.basket.append([item.brand, item.model, qty])  
 
       
  def remove_from_basket(self):
    pass

  def check_out(self):
    pass



item1 = Shop("Apple", "iPhone", 5)
item2 = Shop("Acer", "Aspire", 12)

shopper1 = Shopper("Bruno", "Prado", "bncprado")
shopper1.add_to_basket(item1,5)
print(shopper1.basket)
shopper1.add_to_basket(item2, 12)
print(shopper1.basket)
shopper1.add_to_basket(item1,5)
print(shopper1.basket)
shopper1.add_to_basket(item2, 12)
print(shopper1.basket)

