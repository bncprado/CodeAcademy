def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date, author, title, original_work)
  return poem_desc

""""
1. The function poem_description is supposed to use .format() to print out some quick information about a poem, but it seems to be causing some errors currently.

Fix the function by using keywords in the .format() method.
"""