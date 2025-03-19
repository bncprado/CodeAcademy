""""
1. We’ve got a file, cool_dogs.txt, filled with all the cool dogs we know. Somehow while compiling this list we forgot about one very cool dog. Let’s fix that problem by adding him to our cool_dogs.txt.

Open up our file cool_dogs.txt in append-mode and assign it to the file object cool_dogs_file.

2. Inside your with block, add “Air Buddy\n” to cool_dogs.txt. Air Buddy is a Golden Retriever that plays basketball, which more than qualifies him for this list. The \n character moves to the next line after appending the string.
"""

with open("Files/cool_dogs.txt","a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy\n")