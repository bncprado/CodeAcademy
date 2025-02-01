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

""""
24. Now we want to create and maintain a list of attractions. Let's start by defining a list called attractions.

25. Actually, we want attractions to be an empty list for every destination in destinations. You can do this with this code:

attractions = [[], [], [], [], []]

But there are other ways to accomplish the same thing: by looping through destinations or with a list comprehension.

Define attractions to be a list of 5 (one for each test destination) empty lists using a loop or list comprehension.
"""

attractions = []
for i in destinations:
  attractions.append([])

""""
26. Print out your attractions. Save, and then run your code by typing python3 script.py in the terminal.

Does attractions look like:
[[], [], [], [], []]
"""
print(attractions) #yes

""""
27. Now let's create a function called add_attraction(). This function should take two parameters: "destination", the name of the location and "attraction", the attraction.

28. First we should attempt to find the index of the destination. Use "get_destination_index()" with the passed in destination in order to retrieve the index of the destination. Save the results into "destination_index".

29. This task is no longer necessary. It has been left blank so the project tasks stay aligned with the walkthrough video.

Move on to task 30.

30. This task is no longer necessary. It has been left blank so the project tasks stay aligned with the walkthrough video.

Move on to task 31.

31. If the destination does exist, then we already have a list for it in attractions. Use the destination_index to find the appropriate list in attractions and save that list to attractions_for_destination.
"""

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destinations = attractions[destination_index]
  attractions_for_destinations.append(attraction)
  return attractions_for_destinations

""""
32. Append the attraction passed into "add_attraction" to the list "attractions_for_destination".
That's all we want this function to do, so we can return after adding the attraction to the list.

33. Try adding the following attraction:
"['Venice Beach', ['beach']]"
To the “Los Angeles, USA” destination by calling "add_attraction()" with the two as arguments.
"""

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])

""""
34. Print out "attractions". Then save and run your code with python3 script.py. Your print statement should render the following:

[[], [], [['Venice Beach', ['beach']]], [], []]

If it doesn't something went wrong with add_attraction().
"""
print(attractions) #yes

""""
35. Let's add a few more interesting places to go, paste the following code to add a few more attractions:

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
"""
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

""""
36. Let's add this change to our git repo. First add script.py to your git index.

37. Then commit the changes with the message
"Created attractions and functionality for adding new attractions" (done in the codecademy domain, not here in my git)

38. We want to be able to help our travelers find the most interesting places in a new city for them. In order to do that we need to match their interests with the possible locations in a city.
Write a function "called find_attractions()" that takes two parameters: "destination", the name of the destination and "interests", a list of interests.

39. We'll need the city's "destination_index" to look up its attractions in our attractions table.
Create a variable called "destination_index" and save the destination's index to it using "get_destination_index()"

40. Look up that destination's attractions by indexing into "attractions" with "destination_index". Save this into the variable "attractions_in_city".

41. Create a new list called attractions_with_interest. Make it empty when declaring it, we'll save attractions into this list if they match one of our interests.

42. Create a loop over attractions_in_city saving each item in the list into the temporary variable possible_attraction.
"""
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions.append(destination_index)
  attractions_with_interest = []
