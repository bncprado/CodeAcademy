""""
For the final code challenge, we are going to create a function that finds the middle item from a list of values. This will be different depending on whether there are an odd or even number of values. In the case of an odd number of elements, we want this function to return the exact middle value. If there is an even number of elements, it returns the average of the middle two elements. Here is what we need to do:

1. Define the function to accept one parameter for our list of numbers
2. Determine if the length of the list is even or odd
3. If the length is even, then return the average of the middle two numbers
4. If the length is odd, then return the middle number

Coding question

Create a function called middle_element that has one parameter named my_list.

If there are an odd number of elements in my_list, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
"""
#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)-1]+my_list[int(len(my_list)/2)]
    return sum / 2
  return my_list[int(len(my_list)/2)]

#exactly the same solution as codecademy

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
