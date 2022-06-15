class TicTacToe:
    diagonal_list1 = [0, 4, 8]
    diagonal_list2 = [2, 4, 6]
    def __init__(self):
        self.board = [i for i in range(9)]
        self.current_winner = False
    def cur_board(self):
            print("\n")
            print("\t     |     |")
            print("\t  {}  |  {}  |  {}".format(self.board[0], self.board[1], self.board[2]))
            print('\t_____|_____|_____')

            print("\t     |     |")
            print("\t  {}  |  {}  |  {}".format(self.board[3], self.board[4], self.board[5]))
            print('\t_____|_____|_____')

            print("\t     |     |")

            print("\t  {}  |  {}  |  {}".format(self.board[6], self.board[7], self.board[8]))
            print("\t     |     |")
            print("\n")
    def choosing(self, player):
        if self.current_winner is False:
            print("Board rn: ")
            print(type(self.board[1]))
            self.cur_board()
            try:
                print("Write a block to spot your sign: ")
                move = int(input())
            except ValueError:
                print("Wrong input! Write a number of a block!")
            if move < 0 or move > 8:
                print("Wrong Input!!! Try Again")
            # Check if the box is not occupied already
            if self.board[move] == 'x' or self.board[move] == 'o':
                print("Place already filled. Try again!!")
            else:
                self.board[move] = player.player
                print("Nice choice! Board rn looks this way:")
                self.cur_board()
            if self.win(player) is True:
                self.current_winner = True
                print(f"We have a winner! PLayer {player.player} have won this majestic game!")
                return True

    def win(self, player):
        if self.board[0] == player.player and self.board[1] == player.player and self.board[2] == player.player:
            return True
        if self.board[3] == player.player and self.board[4] == player.player and self.board[5] == player.player:
            return True
        if self.board[6] == player.player and self.board[7] == player.player and self.board[8] == player.player:
            return True
        if self.board[0] == player.player and self.board[4] == player.player and self.board[8] == player.player:
            return True
        if self.board[2] == player.player and self.board[4] == player.player and self.board[6] == player.player:
            return True
        if self.board[0] == player.player and self.board[3] == player.player and self.board[6] == player.player:
            return True
        if self.board[1] == player.player and self.board[4] == player.player and self.board[7] == player.player:
            return True
        if self.board[2] == player.player and self.board[5] == player.player and self.board[8] == player.player:
            return True
        return False
