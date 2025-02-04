""""
1. Let's replicate a function you are already familiar with, len().

Write a new function called get_length() that takes a string as an input and returns the number of characters in that string. Do this by iterating through the string. Do not use the len() function!
"""



def get_length(string):
  leng = 0
  for i in string:
    leng+=1
  return leng