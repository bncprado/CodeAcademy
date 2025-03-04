""""
Finally, let's create a function that combines two different lists together and then sorts them. To do this, we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:

1. Define the function to accept two parameters, one for each list.
2. Combine the two lists using the + operator.
3. Sort the resultant list after concatenation.
4. Return the sorted list.

Coding question

Write a function named combine_sort() that has two parameters named my_list1 and my_list2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.
"""

# Write your function here
def combine_sort(my_list1, my_list2):
  sorted_list = my_list1+my_list2
  return sorted(sorted_list)

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))