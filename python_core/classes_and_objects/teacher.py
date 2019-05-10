from python_core.classes_and_objects.person import Person


class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def print(self):
    print(self.name + ' is ' + str(self.age) + ' old! and graduated in ' + str(self.graduationyear))

