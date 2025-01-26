""""
1. We here at The Boredless Tourist believe that mistakes should be easily corrected, so we keep all of our code version controlled using git.
Start by running git init in the terminal.

2. We'll be doing most of our coding in "2. The Boredless Tourist.py" so we want to make sure that we are tracking that in git.
Add it to git's staging area.


3. Lets create the first commit for this project.
Perform a git commit with the message "initial commit"

4. Now let's create some data that we're going to use to test the functionality that we create for The Boredless Tourist.
The first is our list of destinations that we're going to be using.
Create a list with the following destinations and save it into a variable called destinations.

“Paris, France”
“Shanghai, China”
“Los Angeles, USA”
“São Paulo, Brazil”
“Cairo, Egypt”
"""
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

""""
5. And let's define a test traveler to see how our functionality is working so far.
Create a test_traveler variable. Assign to it the following list:

['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical buildings and art. Erin is in China right now, hopefully we can find some good places to show her.
"""

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

""""
6. Looks like we've got some good sample data to get started with. Let's commit these changes.
First, save the file, then add the .py file to the git index using git add.

7. Next, perform a git commit with the message "Added test objects".

Travelling To Faraway Lands

8. Now that we have test data for a traveler and a list of destinations that we can use, we can start building some of the Boredless Tourist's functionality.

When a traveler arrives at a destination, we want to know where they are! Since we use lists for all of our data — we are going to identify each location based on its index in our destinations list. But we need to retrieve that index first.

Define a function called get_destination_index(). It should take a single parameter, destination, the destination as a string.

9. In the body of get_destination_index(), find the index of destination and save the results into a variable called destination_index.

10. In the body of get_destination_index(), after you've defined destination_index, return it.

11. Test out your function. Try to call get_destination_index() with the argument "Los Angeles, USA".
Print out the results.
Save your code and then run it by typing python3 script.py in the terminal. Is the destination index for “Los Angeles, USA” equal to 2?
"""

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index 

print(get_destination_index("Los Angeles, USA"))

""""
12. Try to call get_destination_index() with the argument “Paris, France” instead. 
Since that is the first element on our destinations list, it should return the index 0.
"""

print(get_destination_index("Paris, France"))

""""
13.What happens if we call get_destination_index() with a destination not in our destinations list?
Try it now: call get_destination_index() with the argument “Hyderabad, India”. What happens?
"""
# print(get_destination_index("Hyderabad, India"))

""""
14. If you used the .index() method to get the index of a destination from the list, you'll notice that calling get_destination_index() with data that is missing from our destinations list will raise a ValueError.
Don't add any logic to avoid triggering this ValueError, it's going to be useful for us in the future.

15. Now let's define a function called get_traveler_location().
"get_traveler_location()" is going to take a single parameter, traveler.

16. In the body of get_traveler_location(), access the traveler's destination string and save it into traveler_destination.

17. Use traveler_destination along with get_destination_index() to retrieve the index of the destination where the traveler is. Save the index of the traveler's destination into the variable traveler_destination_index.

18. Make get_traveler_location() return the destination index of the traveler by returning traveler_destination_index.

"""

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

""""
19. Create a variable called test_destination_index. Save the results of calling get_traveler_location() with our test_traveler.
"""

test_destination_index = get_traveler_location(test_traveler)

""""
20. Print out test_destination_index.
"""
print(test_destination_index)

""""
21. Save your code and run it by calling python3 script.py in the terminal.
Is the test_destination_index you created equal to 1?

22. Let's save our work to the git tracker. Add script.py to the git index with git add.

23. And commit your changes with the message
"Added logic to find traveler destinations and convert to internal data"

"""
