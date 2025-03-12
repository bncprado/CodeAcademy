# songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# playcounts = [78, 29, 44, 21, 89, 5]
# three = [1,2,3,4,5]
# for i, x, y in zip(songs, playcounts, three):
#   print(i,x,y)

""""
"""

# combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
# print(combo_meals[3])

""""
"""

# oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

# for element in oscars:
#   print(element)

# "Best Picture"
# "Best Actor"
# "Best Actress"
# "Animated Feature"
# # 👏
# # Yes! This loop goes through each key in the dictionary and prints it.

""""
"""

# inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
# print(inventory["iron spear"])

""""
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key:value for key,value in zip(letters, points)}

if "$" not in letters_to_points:
  print("Não")