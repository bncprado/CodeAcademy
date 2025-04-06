"""
1. At Jan van High, the students are constantly calling the school rules into question. Create a Rules class so that we can explain the rules.

In order for your code to run, you have to have something in your class — you can’t have a defined class with no body like the following:

class exampleClass:

For now, make the body of your class pass. This will allow your code to run without error.
"""

""""
2. Give Rules a method .washing_brushes() that returns the string

"Point bristles towards the basin while washing your brushes."

Since we’ve now given this class a method, we can remove the pass that we added in the previous step.
"""

class Rules:
  def washing_brushes(self):
    print("Point bristles towards the basin while washing your brushes.")
  

rule1 = Rules()

rule1.washing_brushes()
