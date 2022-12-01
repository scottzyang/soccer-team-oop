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
print('Squad ---------------------------------')
for player in current_roster:
  print(f'{player.name}: {player.position}')

# create new team
united_states = Team('United States', current_roster)
print(f'Team Name: {united_states.team_name}')

# create a coach and add to the team.
print('----------------Coach-----------------')
berhalter = Coach('Gregg Berhalter', 45, 'USA', 500000, 15, 4, united_states)
united_states.set_coach(berhalter)
print(united_states.coach.name)

# call methods
# calling methods (inherited and within subclass) for Attacker

# print object at first roster spot
print('----------First Roster Spot-----------')
print(united_states.roster[0])

# shoot method
united_states.roster[0].shoot()

# outputs Attacker, then calls method to override parent method, and changes to Left Winger
print('-----------Position Change------------')
print(united_states.roster[0].position)
united_states.roster[0].change_position('Left Winger')
print(united_states.roster[0].position)

# outputs 10, then calls inherited method to change to 22
print('------------Number Change-------------')
print(united_states.roster[0].number)
united_states.roster[0].change_number(22)
print(united_states.roster[0].number)

# calls inherited contract increase method from parent class
print('----------------Salary----------------')
print(united_states.roster[0]._salary)
united_states.roster[0]._contract_increase(25)
print(united_states.roster[0]._salary)


# player introduction method that overrides inherited method
print('----------------Intro-----------------')
united_states.roster[0].introduction()
