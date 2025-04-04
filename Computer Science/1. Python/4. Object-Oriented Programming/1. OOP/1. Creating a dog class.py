# LESSON 1 - # Create your class here
class Cat:
# LESSON 1 -   # Create a __init__ method
  def __init__(self, input_name, input_age = 0, input_friendliness=True):
    self.name = input_name
    self.age = input_age
    self.isfriendly = input_friendliness
    self.friends = []

#LESSON 4 - # Describe your class with "__repr__()"
  def __repr__(self):
    if self.isfriendly == True and len(self.friends)<=1:
      return f"{self.name} is a very friendly cat. He's {self.age} yo and has {len(self.friends)} friend"
    elif self.isfriendly == True and len(self.friends)>=1:
      return f"{self.name} is a very friendly cat. He's {self.age} yo and has {len(self.friends)} friends"
    else:
      return f"{self.name} is a bitter cat. He's {self.age} yo and it's anti-social"

#LESSON 2
  # Create method to change at least one attribute
  def birthday(self):
    self.age +=1
    print(f"Today is {self.name}'s birthday. He's {self.age} year old now. HAPPY BIRTHDAY!")

#LESSON 3
  # Create method where two pets interact.
  # Ex: def name(self, pet):
  def become_friends(self,other_cat):
    if other_cat.isfriendly:
      self.friends.append(other_cat)
      other_cat.friends.append(self)
      print(f"{self.name} and {other_cat.name} are now friends")
    else:
      print(f"{other_cat.name} doesn't want to befriend any other cat")

# LESSON 1 -  # Create a new pet!
cat_one = Cat("Doce")

# LESSON 3 - # Create another pet!
cat_two = Cat("Azedo",63,False)
cat_three = Cat("DeBuenas",44,True)
cat_four = Cat("Sussa",35,True)

#LESSON 2 - # Call your method on your new pet here
cat_one.birthday()

#LESSON 3 - Call your method below
cat_one.become_friends(cat_two)
cat_one.become_friends(cat_three)
cat_one.become_friends(cat_four)


#LESSON 4 - Describing your classes
print(cat_one)
print(cat_three)
print(cat_two)
print(cat_four)