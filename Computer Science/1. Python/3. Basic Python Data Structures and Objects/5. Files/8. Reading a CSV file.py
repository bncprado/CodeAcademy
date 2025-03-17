"""""
1. Import the csv module.

2. Open up the file cool_csv.csv in the temporary variable cool_csv_file.

3. Using csv.DictReader read the contents of cool_csv_file into a new variable called cool_csv_dict.

4. cool_csv.csv includes a cool fact about every person in the CSV.

For each row in cool_csv_dict print out that row’s "Cool Fact".
"""

import csv

with open("Computer Science/1. Python/3. Basic Python Data Structures and Objects/5. Files/cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)