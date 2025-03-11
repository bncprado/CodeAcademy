#FOR LOOPS VS DICT COMPREHENSION

#FOR LOOPS
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays={} #WITH FOR LOOPS, WE NEED TO CREATE AN EMPTY DICT
for key, value in zip(songs,playcounts): #THEN DO THE LOOP
  plays[key]=value #AND ADD THE SONGS LIST AS THE KEY AND THE PLAYCOUNTS LIST AS THE VALUE

print(plays)

#DICTIONARY COMPREHENSION

songs2 = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts2 = [78, 29, 44, 21, 89, 5]

plays2 = {key:value for key, value in zip(songs2, playcounts2)} #WITH DICT COMPREHENSION, WE CAN CREATE THE DICT STRAIGHT INTO THE PREVIOUSLY EMPTY DICT


print(plays2)

#IT WILL PRINT EXACTLY THE SAME
