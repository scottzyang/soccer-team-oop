from player import Player
import random

class Attacker(Player):
  def __init__(self, name, age, nation, yoe, salary, number, preferred_foot, position, skill_move):
    super().__init__(name, age, nation, yoe, salary, number, preferred_foot, position)
    
    # Skill move is protected, so only coaches and other players have access to it. 
    self._skill_move = skill_move
    self.scoring_chance = random.randint(0, 1)
    self.celebrate = False

  def shoot(self):
    print(f'{self.name} uses their {self.preferred_foot} foot to shoot!')

    if self.scoring_chance == 1:
      print(f'{self.name} has scored!')
      self.celebrate = True
    else:
      print(f'{self.name} has missed!')

  # overrides inherited method from parent class
  def change_position(self, attacking_position):
    self.position = attacking_position
  

  def introduction(self):
    print(f'Hello my name is {self.name}, I play as a {self.position} and I am from {self.nation}.')

# test
weah = Attacker('Tim Weah', 22, 'USA', 6, 25000, 22, 'right', 'Attacker', 'step-over')

# test methods
weah.shoot()

# test positions
print(weah.position)
weah.change_position('Right Winger')
print(weah.position)

# test introduction method from parent
weah.introduction()
