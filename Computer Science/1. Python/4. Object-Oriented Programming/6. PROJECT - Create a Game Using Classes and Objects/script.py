#This is an SHOP app
class Stock:
  
  products = []

  def __init__(self, kind, brand, model, colour, price, qty):
    self.kind = kind
    self.brand = brand
    self.model = model
    self.colour = colour
    self.price = price
    self.qty = qty

  def buy(self):
    
  
  def sell(self):
    pass

  def check_stock(self):
    pass

class User:
  def __init__(self, name, surname, username, password):
    self.name = name
    self.surname = surname
    self.username = username
    self.password = password

  def create_account():
    pass

  def log_in():
    pass

  def change_password():
    pass


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