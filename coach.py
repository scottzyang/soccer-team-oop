from athlete import Athlete


class Coach(Athlete):
    def __init__(self, name, age, nation, salary, yrs_coaching, trophies, team_managing):
        super().__init__(name, age, nation, salary)
        self.yrs_coaching = yrs_coaching
        self.trophies = trophies
        self.team_managing = team_managing

    def encourage_player(self):
        print(f'Great pass, now make the run!')

    # Private because only the coach can scold people
    def __scold_player(self):
        print(f"You should have made the pass!")
    
    # if the coach is TRULY angry, only then can he access the scold method to scold someone
    def angry(self):
        self.__scold_player()


# test --------------------------------------------------------------------------------
Ancelotti = Coach('Carlo Ancelotti', 63, 'Italy',
                  10500000, 30, 23, 'Real Madrid')
print(Ancelotti.name)

# encourage player
print(Ancelotti.yrs_coaching)
Ancelotti.encourage_player()

# scold player
print(Ancelotti.trophies)
# Ancelotti.__scold_player() does not work, since it is a private method that can only be accessible within the class
Ancelotti.angry()

# test inherited methods
print(Ancelotti._salary)
Ancelotti._contract_increase(10)
print(Ancelotti._salary)
