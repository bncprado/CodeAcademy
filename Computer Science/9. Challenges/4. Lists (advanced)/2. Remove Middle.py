""""
Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an ending index. All elements with an index between the starting and ending index should be removed from the list. Here are the steps:

1. Define the function to accept three parameters: the list, the starting index, and the ending index
2. Get all elements before the starting index
3. Get all elements after the ending index
4. Combine the two partial lists into the result
5. Return the result

Coding question

Create a function named remove_middle which has three parameters named my_list, start, and end.

The function should return a list where all elements in my_list with an index between start and end (inclusive) have been removed.

For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
"""

#Write your function here

def remove_middle(my_list, start, end):
  before = my_list[:start]
  after = my_list[end+1:]
  my_list = before+after
  return my_list

#codecademy code:
# def remove_middle(my_list, start, end):
#   return my_list[:start] + my_list[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))