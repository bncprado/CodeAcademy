

class Microwave:
  def __init__(self,brand:str, power_rating:str):
    self.brand = brand
    self.power_rating = power_rating
    self.turned_on = False
  
  def turn_on(self):
    if self.turned_on:
      print(f"Microwave ({self.brand}) is already turned on.")
    else:
      self.turned_on = True
      print(f"Microwave ({self.brand}) is now turned on.")

  def turn_off(self):
    if self.turned_on:
      self.turned_on = False
      print(f"Microwave ({self.brand}) is now turned off.")
    else:
      print(f"Microwave ({self.brand}) is already turned off.")

  def run(self, seconds=int):
    if self.turned_on:
      print(f"Running ({self.brand}) for {seconds} seconds")
    else:
      print(f"A mystical force whispers: \"Turn on you microwave first\"")

  def __add__ (self,other): 
    ...

smeg = Microwave("Smeg", "B")


smeg.turn_on()
smeg.turn_on()
smeg.run(30)
smeg.turn_off()
smeg.run(30)

bosch = Microwave("Bosch", "D")

bosch.turn_off()
bosch.turn_on()
bosch.turn_on()
bosch.run(566)
bosch.run(34)
bosch.turn_on()
bosch.turn_off()
bosch.turn_off()
bosch.run(34)
bosch.turn_on()

print(smeg+bo)
