""""
Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

1. Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
2. Test if the index is invalid. If it's invalid then return the original list
3. If the index is valid then get all values up to the index and store it as a new list
4. Append the value at the index times 2 to the new list
5. Add the rest of the list from the index onto the new list
6. Return the new list

Coding question

Create a function named double_index that has two parameters: a list named my_list and a single number named index.

The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.

If index is not a valid index, the function should return the original list.

For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)

After writing your function, un-comment the call to the function that we've provided for you to test your results.
"""
#Write your function here
#my solution
def double_index(my_list,index):
  if index+1 > len(my_list):
    return my_list
  else:
    my_list[index]*=2
    return my_list




#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12],))