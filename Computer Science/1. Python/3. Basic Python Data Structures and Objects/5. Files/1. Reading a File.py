""""
1. Use with to open the file welcome.txt. Save the file object as text_file.

2. Read the contents of text_file and save the results in text_data.

3. Print out text_data.
"""
with open("Computer Science/1. Python/3. Basic Python Data Structures and Objects/5. Files/welcome.txt") as text_file:
  text_data = text_file.read()

print(text_data)