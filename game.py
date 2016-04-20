from Board import Board
from BTNode import BTNode
from BTree import *

class Game_ei_ai:
    def __init__(self):
        self.data = Board()
        self.root = BTNode(self.data)
        self.get_rt = self.root
        self.tree = BTree(self.get_rt)

    def turn_player(self):
        i, j = (int(k) for k in input("Enter a move: ").split())
        if self.data.cells[j][i] == 0:
            self.data.set_value((j, i), 1)
            print(self)
            return self.data
        else:
            print("You cannot put here")
            return self.turn_player()
    def _play(self):
        if self.data.has_winner() != None and self.tree != None:
            ans = "The end/ "
            if self.data.has_winner() == -1:
                ans += "YOU LOOSE"
            if self.data.has_winner() == 1:
                ans += "YOU WON"
            print(ans)
            return ans
        elif self.tree != None:
            self.turn_player()
            print("-|-|-|-|-|-")
            self.tree.expand()
        #if self.tree.get_best_index() != None:
            i, j = (int(k) for k in self.tree.get_best_index())
            print("^^^^^^^^^^^^^^^^^^^^^^^^^")
            self.data.set_value([i, j], -1)
            print(self)
            return self.data, self.recurse_play()


        else:
            print("The enddddddd")
            return "The endddddd"
    def recurse_play(self):
        self._play()

    def __str__(self):
        repre = "|---|---|---|" + "\n"
        for i in range(3):
            repre += "|"
            for j in range(3):
                if self.data.cells[i][j] == -1:
                    repre += " X " + "|"
                elif self.data.cells[i][j] == 1:
                    repre += " O " + "|"
                else:
                    repre += "   " + "|"
            repre += "\n" + "|---|---|---|" + "\n"
        repre += "^^^^^^"
        return repre

play = Game_ei_ai()
play.recurse_play()
print('A')


