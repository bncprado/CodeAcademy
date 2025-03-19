""""
1. In script.py there’s a file object that doesn’t get closed correctly. Let’s fix it by changing the syntax!

Remove this line:

close_this_file = open('fun_file.txt')

And change it to use the with syntax from our previous exercises.

Remember to indent the rest of the body so that we don’t get an IndentError.
"""
# close_this_file = open('/Volumes/SSD 4TB EXT/Git/CodeAcademy/Computer Science/1. Python/3. Basic Python Data Structures and Objects/5. Files/fun_file.txt')

with open("Files/fun_file.txt") as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
