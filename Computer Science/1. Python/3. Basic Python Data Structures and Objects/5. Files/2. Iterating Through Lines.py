""""
1. Using a with statement, create a file object pointing to the file how_many_lines.txt. Store that file object in the variable lines_doc.

2. Iterate through each of the lines in lines_doc.readlines() using a for loop.

Inside the for loop print out each line of how_many_lines.txt.
"""

with open("Computer Science/1. Python/3. Basic Python Data Structures and Objects/5. Files/how_many.lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)