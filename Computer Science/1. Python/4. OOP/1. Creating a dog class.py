# You can start with the
# Cat class or erase this
# and use your own!
class Cat:
  def __init__(self, input_name, input_breed, input_age = 0):
    self.name = input_name
    self.breed = input_breed
    self.age = input_age
    self.is_cuddly = True
  
  # Create method to change
  # at least one attribute.
  # Ex: def change_att(self):
  def birthday(self):
    self.age +=1
    print(f"{self.name} is celebrating one more year. {self.name} is {self.age} years old now!")


# Create your new pet.
new_cat = Cat("Leo", "Tabby", 3)

# Call your method on your
# new pet here.

new_cat.birthday()

