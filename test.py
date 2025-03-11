songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
three = [1,2,3,4,5]
for i, x, y in zip(songs, playcounts, three):
  print(i,x,y)