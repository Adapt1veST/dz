class Animals:
    def __init__(self, weight = 6):
        self.age = 5
        self.weight = weight

cat = Animals()
dog = Animals(weight=10)
print(cat.weight)
print(cat.age)
print(dog.weight)
print(dog.age)

class Student:
  def __init__(self, age = 12, money = 100, gpa = 9):
      self.age = age
      self.money = money
      self.gpa = gpa

nick = Student()
kate = Student(age=10, money = 120, gpa = 10)
max = Student(age=13, money = 200, gpa = 12)
print(nick.age, nick.money, nick.gpa)
print(kate.age, kate.money, kate.gpa)
print(max.age, max.money, max.gpa)
