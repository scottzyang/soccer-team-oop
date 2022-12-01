from player import Player
import random


class Defender(Player):
    def __init__(self, name, age, nation, salary, number, preferred_foot, position, in_box):
        super().__init__(name, age, nation, salary, number, preferred_foot, position)
        self.in_box = in_box
        self.pass_success = random.randint(0, 1)

    def tackle(self):
        if self.in_box == True:
            print(f'{self.name} cleared the ball away cleanly!')
        else:
            print(
                f'Ooo! {self.name} might get be getting a card for that tackle!')

    def long_pass(self):
        if self.pass_success == 1:
            print(f'{self.number} with a terrific cross into the area!')
        else:
            print(f"{self.number}'s pass is easily intercepted.")

    # override inherited method from Player
    def change_position(self, defending_position):
        self.position = defending_position

    def introduction(self):
        print(
            f'My name is {self.name}, I play as a {self.position} and I am from {self.nation}.')

# Test
if __name__ == "__main__":
    ream = Defender('Tim Ream', 35, 'USA', 7000000,
                    13, 'left', 'Defender', True)

    # test methods
    ream.long_pass()

    # test positions
    print(ream.position)
    ream.change_position('Center Back')
    print(ream.position)

    # test introduction from Player
    ream.introduction()
