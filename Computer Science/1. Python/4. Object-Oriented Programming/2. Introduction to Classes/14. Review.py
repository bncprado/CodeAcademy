class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

print(pieter.grades)


""""
MY CODE

class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self,grade):
    if type(grade) is Grade:
      self.grades.append(grade.score)
    else:
      pass

class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

grade100 = Grade(100)

pieter.add_grade(grade100)

print(pieter.grades)
print(pieter.year)
print(pieter.name)


"""