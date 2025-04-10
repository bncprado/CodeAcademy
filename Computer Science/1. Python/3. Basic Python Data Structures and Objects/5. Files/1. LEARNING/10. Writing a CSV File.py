""""
1. We have a list in the workspace access_log which is a list of dictionaries we want to write out to a CSV file.

Let’s start by importing the csv module.

2. Open up the file logger.csv in the temporary variable logger_csv. Don’t forget to open the file in write-mode.

3. Create a csv.DictWriter instance called log_writer. Pass logger_csv as the first argument and then fields as a keyword argument to the keyword fieldnames.

4. Write the header to log_writer using the .writeheader() method.

5. Iterate through the access_log list and add each element to the CSV using log_writer.writerow().
"""

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open("Files/logger.csv","w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  log_writer.writeheader()
  for i in access_log:
    log_writer.writerow(i)