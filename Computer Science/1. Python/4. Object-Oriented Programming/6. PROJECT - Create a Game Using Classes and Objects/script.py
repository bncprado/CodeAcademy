def master_user_and_password():
  master_user_and_pass = {
  "Username":"M",
  "Password":"P"
  }

  user_name = input("Enter the master username: ").upper().strip()

  i=5

  while i>0 and user_name != master_user_and_pass.get("Username"):
    i-=1
    if i > 1:
      user_name = input("Try again. Please, enter the master username: ").upper().strip()
    elif i==1:
      user_name = input("This is your last change, program will quit if wrong username again: ").upper().strip()
    elif i==0:
      print("Quitting the program")
      exit()

  password = input("Now, enter the master password: ").upper().strip()

  x=5

  while x>0 and password != master_user_and_pass.get("Password"):
    x-=1
    if x > 1:
      password = input("Try again. Please, enter the master password: ").upper().strip()
    elif x==1:
      password = input("This is your last change, program will quit if wrong password again: ").upper().strip()
    elif x==0:
      print("Quitting the program")
      exit()

registered_usernames = []

class User:

  def __init__(self, name:str, surname:str, username:str, password:int):
    self.name = name
    self.surname = surname
    self.username = username
    while self.username in registered_usernames:
      self.username = input(f"{self.username} already in use. Enter a different one: ")
    registered_usernames.append(self.username)
    self.password = password

  def __repr__(self):
    return f"User(name='{self.name}', surname='{self.surname}', username='{self.username}, password='{self.password}')"

  def change_username(self):
    new_username =  input("Please, type your new username: ")
    while new_username in registered_usernames:
      new_username = input("Username already in use, please enter a new one: ")
    registered_usernames.remove(self.username)
    self.username = new_username
    registered_usernames.append(new_username)

  def change_password(self):
    self.password = input("Please, type your new password: ")

  def change_name_and_surname(self):
    self.name = input("Please, enter your new name: ")
    self.surname = input("Please, enter your new surname: ")
    

inventory = {}

class Stock:
  
  def __init__(self, category, brand, model, colour, qty, price):
    inventory["Category"] = self.category = category
    inventory["Brand"] = self.brand = brand
    inventory["Model"] = self.model = model
    inventory["Colour"] = self.colour = colour
    inventory["Qty"] = self.qty = qty
    inventory["Price"] = self.price = price

  def __repr__(self):
    return (f"Stock(category='{self.category}', brand='{self.brand}', model='{self.model}', "
            f"colour='{self.colour}', qty={self.qty}, price={self.price})")
  
  def buy(self, howmany):
    inventory.update({"Qty":inventory["Qty"] + howmany})

  def sell(self, howmany):
    inventory.update({"Qty":inventory["Qty"] - howmany})
    
  def check_stock(self):
    print("You have {} {} {} in the inventory".format(inventory.get("Qty"),inventory.get("Colour"),inventory.get("Model")))
    
print(inventory)
iphone15 = Stock("Smartphone", "Apple", "iPhone 15", "Black", 5, 799)
print(iphone15)
print(inventory)
iphone15.buy(5)
print(inventory)
iphone15.sell(4)
print(inventory)
iphone15.check_stock()
print(inventory)

user1 = User("Bruno", "Prado", "bncprado", "Vale3")
print(user1)
user1.change_username()
print(user1)
user1.change_password()
print(user1)
user1.change_name_and_surname()
print(user1)
