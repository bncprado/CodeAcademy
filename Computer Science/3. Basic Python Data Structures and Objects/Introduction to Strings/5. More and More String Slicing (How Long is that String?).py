first_name = "Reiko"
last_name = "Matsuki"

""""
Copeland's Corporate Company also wants to update how they generate temporary passwords for new employees.

Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates the last three letters of each and returns them as a string.
"""

def password_generator(first_name,last_name):
  new_name = first_name[-3:]+last_name[-3:]
  return new_name

""""
2. Test your function on the provided first_name and last_name and save it to the variable temp_password.
"""
temp_password = password_generator(first_name,last_name)

print(temp_password)