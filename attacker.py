from player import Player

class Attacker(Player):
  def __init__(self, name, age, nation, yoe, salary, number, preferred_foot, position, skill_move):
    super().__init__(name, age, nation, yoe, salary, number, preferred_foot, position)
    self.skill_move = skill_move
