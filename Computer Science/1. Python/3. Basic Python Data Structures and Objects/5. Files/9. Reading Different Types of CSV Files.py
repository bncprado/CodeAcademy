""""
1. Import the csv module.

2. Open up the file books.csv in the variable books_csv.

3. Create a DictReader instance that uses the @ symbol as a delimiter to read books_csv. Save the result in a variable called books_reader.

4. Create a list called isbn_list, iterate through books_reader to get the ISBN number of every book in the CSV file. Use the ['ISBN'] key for the dictionary objects passed to it.
"""

import csv
with open("/Volumes/SSD 4TB EXT/Git/CodeAcademy/Computer Science/1. Python/3. Basic Python Data Structures and Objects/5. Files/books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [row["ISBN"] for row in books_reader]
  # for row in books_reader:
  #   isbn_list.append(row["ISBN"])
  
print(isbn_list)