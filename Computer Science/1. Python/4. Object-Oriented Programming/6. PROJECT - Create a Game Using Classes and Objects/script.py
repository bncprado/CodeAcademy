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

# master_user_and_password()
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
    
user1 = User("Bruno", "Prado", "bncprado", "Vale3")

inventory = {}

print(inventory)

class Stock:
  
  def __init__(self, category, brand, model, colour, qty, price):
    self.category = category
    self.brand = brand
    self.model = model
    self.colour = colour
    self.qty = qty
    self.price = price
    

  def buy(self, price, qty):
    inventory["Category"] = self.category
    inventory["Brand"] = self.brand
    inventory["Model"] = self.model
    inventory["Price"] = price
    inventory["Qty"] = qty

  def sell(self, howmany):
    inventory.update({"Qty":inventory["Qty"]-howmany})
    

  def check_stock(self):
    # inventory["Category"] = self.category
    # inventory["Brand"] = self.brand
    # inventory["Model"] = self.model
    # inventory["Colour"] = self.colour
    # inventory["Price"] = price
    # inventory["Qty"] = qty
    pass

iphone15 = Stock("Smartphone", "Apple", "iPhone 15", "Blue")
print(inventory)
iphone15.buy(799,5)
print(inventory)
iphone15.sell(4)
print(inventory)
iphone15.buy(799,5)
print(inventory)



"""
import csv

# 1. Read the current data into a list
with open("stock.csv", mode="r", newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

rows.append(["Mobile","Apple","iPhone 15",699])

with open("stock.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)



# 2. Modify the data
# Example: Add a new person


# # Example: Remove Bob
# rows = [row for row in rows if row["name"] != "Bob"]

# # 3. Write it back (overwrite file)
# with open("people.csv", mode="w", newline='') as file:
#     fieldnames = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerows(rows)
"""