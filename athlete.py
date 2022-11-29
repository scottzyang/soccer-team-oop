
class Athlete:
  def __init__(self, name, age, nation, yoe, salary):
    self.name = name
    self.age = age
    self.nation = nation
    self.yoe = yoe
    self.salary = salary

  def introduction(self):
    print(f'Hello my name is {self.name}, I am {self.age} years old. I am from {self.nation}')

  # possibly add another method
  def contract_increase(self, percentage_increase):
    increase = self.salary * (percentage_increase / 100)
    self.salary += increase


# test --------------------------------------------------------------------------------
athlete = Athlete('Christian Pulisic', 24, 'USA', 8, 250000)
print(athlete.name)

# test salary method
print(athlete.salary)
athlete.contract_increase(30)
print(athlete.salary)