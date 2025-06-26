can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for x in can_we_count_it:
  if hasattr(x, "count"):
    print(str(type(x)) + " has the count attribute!")
  else:
    print(str(type(x)) + " does not have the count attribute :(")