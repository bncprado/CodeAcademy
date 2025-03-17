user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

#first, a key that exist in the dictionary
tc_id = user_ids.get("teraCoder")

print(tc_id)

#now, a key that doesn't exist

stack_id = user_ids.get("superStackSmash",100000)

print(stack_id) #it would print None if we didn't declare the value of "100000"

test =  user_ids.pop("no", 23)

print(user_ids)

print("keysmithKeith" in user_ids)