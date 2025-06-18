class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

print(dir(fake_dict))
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__()', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']

fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

print(dir(fun_list))
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


### EXERCISES ###

dir(5)

def this_function_is_an_object(string):
  print("This is a {a} that means {b}".format(a=string,b=string))

this_function_is_an_object("texto")
