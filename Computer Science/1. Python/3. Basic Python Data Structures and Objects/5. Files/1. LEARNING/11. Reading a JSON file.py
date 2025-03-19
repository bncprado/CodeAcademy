""""
1. Let’s read a JSON file! Start by importing the json module.

2. Open up the file message.json, saving the file object to the variable message_json.

Open the file in read-mode, without passing any additional arguments to open().

3. Pass the JSON file object as an argument to json.load() and save the resulting Python dictionary as message.

4. Print out message['text'].
"""
import json
with open("Files/message.json") as message_json:
  message = json.load(message_json)
print(message["text"])

