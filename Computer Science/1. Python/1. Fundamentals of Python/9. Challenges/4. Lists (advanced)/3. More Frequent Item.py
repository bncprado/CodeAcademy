""""
Let's go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another for the first item we are comparing, and another for the second item. Here are the steps:

1. Define the function to accept three parameters: the list, the first item, and the second item
2. Count the number of times item1 shows up in our list
3. Count the number of times item2 shows up in our list
4. Return the item that appears more frequently in my_list — if both items show up the same number of times, return item1

Coding question

Create a function named more_frequent_item that has three parameters named my_list, item1, and item2.

Return either item1 or item2 depending on which item appears more often in my_list.

If the two items appear the same number of times, return item1.
"""

#Write your function here
def more_frequent_item(my_list, item1, item2): #exact same solution as codecademy
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2
  
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))