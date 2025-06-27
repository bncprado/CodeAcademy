#This is an SHOP app
import pandas as pd

df = pd.read_csv("stock.csv")

print(df)

class Stock:
  
  products = []

  def __init__(self, kind, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price
    self.kind = kind

  def buy(self):
    pass
  
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








