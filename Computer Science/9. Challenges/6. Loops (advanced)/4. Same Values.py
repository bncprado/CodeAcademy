""""
In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index. These are the steps we need to accomplish this:

1. Define our function to accept two lists of numbers
2. Create a new list to store our matching indices
3. Loop through each index to the end of either of our lists
4. Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
5. Return our list of indices

Coding question

Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
"""
def same_values(lst1, lst2):
  matching_indices = []
  for i in range(len(lst1)):
    if lst1[i]==lst2[i]:
      matching_indices.append(i)
  for i in range(len(lst2)):# codecademy didn't loop through the second list. So the requirement to "loop through each index" was unnecessary. 
    continue
  return matching_indices
    

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))