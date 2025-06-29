class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self,grade):
    if type(grade) == Grade:
        self.grades.append(grade)

  def __repr__(self):
    return f"Student: {self.name}\nYear: {self.year}\nGrades: {self.grades}"

roger = Student("Roger van der Weyden",10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

  def __repr__(self):
    return str(self.score)

grade_100 = Grade(100)

pieter.add_grade(grade_100)

print(pieter)

strn="string"

print(type(Student))