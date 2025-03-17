def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc
#the function above is the corrected one

""""
1. The function poem_description is supposed to use .format() to print out some quick information about a poem, but it seems to be causing some errors currently.

Fix the function by using keywords in the .format() method.
"""

""""
Run poem_description with the following arguments and save the results to the variable my_beard_description:

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

"""
my_beard_description = poem_description("Shel Silverstein","My Beard","Where the Sidewalk Ends","1974")#right answer