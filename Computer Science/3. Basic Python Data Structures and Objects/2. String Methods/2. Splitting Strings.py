""""
1. In the code editor is a string of the first line of the poem Spring Storm by William Carlos Williams.

Use .split() to create a list called line_one_words that contains each word in this line of poetry.

"""

line_one = "The sky has given over"

line_one_words = line_one.split() #default value will split anything separated by a blank space
#=> created a list with every word of line_one variable

print(line_one_words)

""""
Split method will not only split by the typed argument, but also REMOVE the argument from the given string
"""

word = "banana"

word_split = word.split("a")
#=>['b', 'n', 'n', '']

print(word_split)



