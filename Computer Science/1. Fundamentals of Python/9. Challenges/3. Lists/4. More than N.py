""""
Our factory produces a variety of different flavored snacks. The different types of snacks are represented by their id and are kept on a conveyor belt. We want to check if we have enough items of a certain snack in our inventory. For this, we need to write a Python function that does the following.

The function should accept a list of numbers representing the ids of snack on the conveyor belt as its first input, the id of snack we are looking for as its second input, and the desired number of that type of snack on the conveyor belt as its third input.
The function should return True if the snack we are searching for appears more times in the list than the desired number given in the third parameter. Otherwise, it should return False.

Following are the steps we need to implement the above scenario:
1. Define the function to accept three parameters: a list of numbers, a number to look for, and a number for the number of instances.
2. Count the number of occurrences of item i.e. the second parameter in my_list i.e. the first parameter.
3. If the number of occurrences is greater than n i.e. the third parameter, return True. Otherwise, return False.

Coding question

Create a function named more_than_n() that has three parameters named my_list, item, and n.

The function should return True if item appears in the list more than n times. The function should return False otherwise.
"""

# Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))