available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

print(available_items)
#> {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25, 'stamina grains': 15, 'power stew': 30}

print(health_points + available_items.pop("stamina grains", 0)) #it will, at the same time, add the value of "stamina grains" to "health_points" and also remove "stamina grains" from "available_items". If "stamina grains" didn't exist in "available_items", it would add the value of 0, that was declared in the .pop method
#> 35

print(available_items)
#> {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25, 'power stew': 30}

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)