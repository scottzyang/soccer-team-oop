
class Athlete:
  def __init__(self, name, age, nation, salary):
    self.name = name
    self.age = age
    self.nation = nation
    # Salary is protected and only accessible by subclasses
    self._salary = salary

  def introduction(self):
    print(f'Hello my name is {self.name}, I am {self.age} years old. I am from {self.nation}')

  # Protected method because player and coach class inherits this method and would require access.
  def _contract_increase(self, percentage_increase):
    increase = self._salary * (percentage_increase / 100)
    self._salary += increase


# test --------------------------------------------------------------------------------
athlete = Athlete('Christian Pulisic', 24, 'USA', 250000)
print(athlete.name)

# test salary method
print(athlete._salary)
athlete._contract_increase(30)
print(athlete._salary) 