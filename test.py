my_list = [1,2,3]
my_list2 = [3,2,1]

matching = []

matching.insert(0,[1,2,])
matching.insert(1,[1,2])

for i in range(len(my_list)):
  if my_list[i]==my_list2[-1-i]:
    print(True)
  else:
    print(False)

