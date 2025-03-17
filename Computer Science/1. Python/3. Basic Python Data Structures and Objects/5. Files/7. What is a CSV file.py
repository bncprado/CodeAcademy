""""
1. CSV files are just plain text files!

Open logger.csv using our standard with syntax, saving the file object in the temporary variable log_csv_file.

2. Print out the contents of logger.csv by calling .read() on the file. Notice that it is parsed as a string.
"""

log_csv_file = open("Computer Science/1. Python/3. Basic Python Data Structures and Objects/5. Files/logger.csv")

print(log_csv_file.read())