password = "AbeSimp"

test = ""

# for i in range(password):
#   test = test + password[i]
 
for i in range(len(password)):
  test += password[i]

# print(test)

print(password[-1:]+password[0:-1])