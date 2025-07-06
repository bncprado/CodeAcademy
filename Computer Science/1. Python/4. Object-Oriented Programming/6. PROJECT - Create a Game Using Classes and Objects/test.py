basket = {
  "Brand": "Apple",
  "Model": "iPhone",
  "Qty": 4
}

lista = [basket]

if "Apple" in basket.values():
  basket["Qty"] +=5

print(lista)
