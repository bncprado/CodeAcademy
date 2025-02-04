""""
1. Copeland's Corporate Company has finalized what they want their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.

Let's start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a user_name. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

For example, if the employee's name is Abe Simpson the function should generate the username AbeSimp.
"""

def username_generator(first_name,last_name):
  user_name = ""
  if len(first_name)>3 and len(last_name)>4:
    user_name = first_name[:3]+last_name[:4]
    return user_name
  elif len(first_name)>3 and len(last_name)<=4:
    user_name = first_name[:3]+last_name
    return user_name
  elif len(first_name)<=3 and len(last_name)>4:
    user_name = first_name+last_name[:4]
    return user_name
  else:
    user_name = first_name+last_name
    return user_name
  
print(username_generator("Abe","Simpson"))

""""
2. Great work! Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.

Start by defining a function called password_generator that takes one parameter user_name and defines an empty string named password within the function body.

3. Inside password_generator, create a for loop that iterates through the indices of user_name by going from 0 to len(user_name).

The loop should create the password by shifting all the letters of user_name one to the right. To do so, add the letter at the previous index of user_name to password with each pass of the loop.

After the for loop but still within the definition of password_generator, return the password.
"""
def password_generator(user_name):
  password = ""
  for i in range(user_name):
    password = password + user_name[i]
  return password

print(password_generator("AbeSimp"))
