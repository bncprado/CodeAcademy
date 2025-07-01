inventory = {}
print(inventory)
inventory["Category"]="Smartphone"
inventory["Qty"]=5
print(inventory)
inventory.update({f"Qty":inventory["Qty"]-4})
print(inventory)

