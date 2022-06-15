import random
import tictactoegame
import math
import numpy as np
field = np.array([["_", "_" ,"_"],
                 ["_", "_", "_"],
                  ["_", "_", "_"]])
class Player:
    def __init__(self, num):
        self.num = num
        if num == 1:
            self.player = "x"
        else:
            self.player = "o"

#lets nxt player get his turn
    def get_move(self, game):
        pass

class ComputerPlayer(Player):
    def __init__(self,  num):
        super().__init__(num)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self,  letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
print("type smth to start.")
while input() != "+":
    print("Hello, fellow! Do you want to play some TicTacToe? + or -?")
    if input() == "+":
        player1 = HumanPlayer(1)
        print("Player1 created! Your sign is 'x'.")
        break
    else:
        print("Damn that hurts....")
print("Who you want to play with? Computer(1) or another Player(2)? Input 1 or 2: ")

try:
    answer = int(input())
    if answer == 1:
           player2 = ComputerPlayer(2)
           print("Computer is here! His sign is 'o'.")
    elif answer == 2:
            player2 = HumanPlayer(2)
            print("Player2 created! Your sign is 'o'.")
except ValueError:
    print("Wrong input! Write a number of a block!")
if answer > 2 or answer < 1:
    print("Wrong input! Write 1 for computer as enemy and 2 to allow another player join session.")
game = words.TicTacToe()
i = 0
while game.current_winner is not True or i < 9:
    game.choosing(player1)
    game.choosing(player2)
    i += 1