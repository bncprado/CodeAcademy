songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# plays = {songs:playcounts for songs,playcounts in zip(songs,playcounts)}

plays={}
for key, value in zip(songs,playcounts):
  plays[key]=value

print(plays)

# plays["Purple Haze"]=1

# plays["Respect"]=94

# library = {"The Best Songs":plays, "Sunday Feelings":{}}

# print(plays)

# print(library)