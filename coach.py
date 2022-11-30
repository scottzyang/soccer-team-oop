from athlete import Athlete


class Coach(Athlete):
    def __init__(self, name, age, nation, yoe, salary, yrs_coaching, trophies, team_managing):
        super().__init__(name, age, nation, yoe, salary)
        self.yrs_coaching = yrs_coaching
        self.trophies = trophies
        self.team_managing = team_managing

    def encourage_player(self):
        print(f'Great pass, now make the run!')

    # Private because only the coach can scold people
    def __scold_player(self):
        print(f"You should have made the pass!")


# test --------------------------------------------------------------------------------
Ancelotti = Coach('Carlo Ancelotti', 63, 'Italy', 42,
                  10500000, 30, 23, 'Real Madrid')
print(Ancelotti.name)

# encourage player
print(Ancelotti.yrs_coaching)
Ancelotti.encourage_player()

# scold player
print(Ancelotti.trophies)
Ancelotti.scold_player()

# test inherited methods
print(Ancelotti.salary)
Ancelotti.contract_increase(10)
print(Ancelotti.salary)
