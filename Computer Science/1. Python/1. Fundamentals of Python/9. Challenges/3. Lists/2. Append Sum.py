""""
For the next challenge, let's create a function that calculates the sum of the last two elements of an input list and appends it to the end of the original list. After doing so, it repeats this process two more times and returns the resulting list.

For example, for the input list [1, 1, 2], the output list should be [1, 1, 2, 3, 5, 8]. Similarly, the output for the input list [1, 23] should be [1, 23, 24, 47, 71].

To complete the challenge, you need to implement the following:

1. Define the function append_sum() to accept a list as its input argument.
2. Add the last and second-to-last elements of the input list.
3. Append the calculated sum to the end of the input list.
4. Repeat the previous two steps two more times for the modified list.
5. Return the modified list.

Coding question

Write a function named append_sum() that has one parameter — a list named named my_list.

The function should add the last two elements of my_list together and append the result to my_list. It should do this process three times and then return my_list.

For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
"""
# Write your function here
def append_sum(my_list):
  last_two = my_list[-1] + my_list[-2]
  my_list.append(last_two)
  last_two = my_list[-1] + my_list[-2]
  my_list.append(last_two)
  last_two = my_list[-1] + my_list[-2]
  my_list.append(last_two)
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))