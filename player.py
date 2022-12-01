from athlete import Athlete

class Player(Athlete):
  def __init__(self, name, age, nation, salary, number, preferred_foot, position):
    super().__init__(name, age, nation, salary)
    self.number = number
    self.preferred_foot = preferred_foot
    self.position = position


  def change_position(self, new_position):
    if new_position.lower() == 'attacker' or new_position.lower() == 'defender':
      self.position = new_position
    else:
      print('Please change to a valid position')


  def change_number(self, new_number):
    self.number = new_number


# test --------------------------------------------------------------------------------
if __name__ == "__main__":
  beckham = Player('David Beckham', 26, 'England', 650000, 23, 'right', 'Attacker')
  print(beckham.name)

  # changes position
  print(beckham.position)

  beckham.change_position('Attacker')

  print(beckham.position)

  # changes number
  print(beckham.number)
  beckham.change_number(11)
  print(beckham.number)

  # test inherited methods
  print(beckham._salary)
  beckham._contract_increase(25)
  print(beckham._salary)