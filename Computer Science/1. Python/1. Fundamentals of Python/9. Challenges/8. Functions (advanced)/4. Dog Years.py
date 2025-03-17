""""
Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age. This will require a few steps:

1. Define the function called dog_years to accept two parameters: name and age
2. Calculate the age of the dog in dog years
3. Concatenate the string with the dog’s name and age in dog years
4. Return the resulting string

Coding question

Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.

The function should compute the age in dog years and return the following string:

"{name}, you are {age} years old in dog years"

Test this function with your name and your age!
"""
# Write your dog_years function here:
def dog_years(name,age):
  return f"{name}, you are {age*7} years old in dog years"
  
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"