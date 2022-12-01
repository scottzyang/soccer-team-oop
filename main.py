from attacker import Attacker
from defender import Defender
from freeagents import players
from coach import Coach
from team import Team

# create current roster from free agents
current_roster = list()
for player in players:
  if player['position'] == 'Defender':
    new_player = Defender(player['name'], player['age'], player['nation'], player['salary'], player['number'],player['preferred_foot'], player['position'], player['in_box'])
  else:
    new_player = Attacker(player['name'], player['age'], player['nation'], player['salary'], player['number'],player['preferred_foot'], player['position'], player['skill_move'])
  current_roster.append(new_player)

# print name of each player on roster
for player in current_roster:
  print(f'{player.name}: {player.position}')

# create new team
united_states = Team('United States', current_roster)
print(f'Team Name: {united_states.team_name}')