""""
1. Using a with statement, create a file object pointing to the file just_the_first.txt. Store that file object in the variable first_line_doc.

2. Save the first line of just_the_first.txt into the variable first_line.

3. Print out the variable first_line.
"""
with open("/Volumes/SSD 4TB EXT/Git/CodeAcademy/Computer Science/1. Python/3. Basic Python Data Structures and Objects/5. Files/just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()

print(first_line)

