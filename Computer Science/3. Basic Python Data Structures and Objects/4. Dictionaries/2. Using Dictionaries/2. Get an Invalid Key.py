zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# print(zodiac_elements["energy"])

zodiac_elements["energy"]="Not a Zodiac element" #this key and value was added after the "if statement"

""""
Because "energy" is not a key in zodiac_elements, a KeyError is thrown in the terminal!

Using an if statement, check if "energy" is a key in zodiac_elements. Nest the existing print() statement within the if statement so that it will only execute if "energy" is a key.

Run your code again. This time, there should be no errors in the terminal!
"""

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])