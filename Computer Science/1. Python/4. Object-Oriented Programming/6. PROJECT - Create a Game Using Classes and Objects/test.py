basket = [["Brand","Model","Qty"],["Apple","iPhone",4],["Apple","iPhone13",4]]

for x in basket[:-1]:
  if "Apple" in x and "iPhone13" in x:
    basket.append(["Apple","iPhone13",4])
    break
  else:
    print(x)

