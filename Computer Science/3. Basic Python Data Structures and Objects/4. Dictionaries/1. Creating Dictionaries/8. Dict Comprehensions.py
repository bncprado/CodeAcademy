drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# zipped_drinks = zip(drinks,caffeine)

# drinks_to_caffeine = {}

# for i in zipped_drinks:
#   drinks_to_caffeine[i[0]]=i[1]
#EVERYTHING COMMENTED ABOVE CAN BE THE SAME AS:

drinks_to_caffeine = {drinks:caffeine for drinks, caffeine in zip(drinks, caffeine)}

print(drinks_to_caffeine)