from player import Player

class Team:
  def __init__(self, team_name, roster):
    self.team_name = team_name
    self.roster = roster

  def add_players(self, new_player):
    self.roster.append(new_player)

  def sell_player(self, sold_player):
    self.roster.remove(sold_player)



# test ------------------------------------------------------

# create new players
# name, age, nation, yoe, salary, number, preferred_foot, position
scott = Player('Scott Yang', 26, 'USA', 3, 41000, 3, 'right', 'CM')
paul = Player('Paul Fletes', 29, 'USA', 4, 41000, 3, 'right', 'Winger')

current_roster = [scott, paul]
chelsea = Team('Chelsea', current_roster)
print(chelsea.roster)

# create additional player and add
pulisic = Player('Christian Pulisic', 24, 'USA', 5, 65000, 10, 'right', 'Winger')
chelsea.add_players(pulisic)
print(chelsea.roster)

chelsea.sell_player(pulisic)
print(chelsea.roster)

# access roster, should output 'Scott Yang'
print(chelsea.roster[0].name)