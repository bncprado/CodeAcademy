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
  
print(username_generator("At","ira"))

    