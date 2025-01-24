""""
In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers. Let’s look at the steps we need:

1. Define the function to accept two lists of numbers, bases and powers
2. Create a new list that will contain our answers
3. Create a loop that iterates through every base in bases
4. Within that loop, create another loop that iterates through every power in power
5. Within that nested loop, append the result of the current base raised to the current power.
6. After all iterations of both loops are complete, return the list of answers

Questions

Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])

the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.
"""

#Write your function here
def exponents(bases, powers):
  answers = []
  for base in bases:
    for power in powers:
      answers.append(base**power)
  return answers

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))