spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

""""
1. The organization has sent you over the full text for William Carlos Williams poem Spring Storm. They want you to break the poem up into its individual lines.

Create a list called spring_storm_lines that contains a string for each line of Spring Storm.
"""

spring_storm_lines = spring_storm_text.split("\n")

for i in spring_storm_lines:
  print (i)