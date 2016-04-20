import random
import copy
class Board(object):
    '''
    -1 - Human
    1 - Computer
    '''
    def __init__ (self):
        # x -> 1
        # 0 -> -1
        self.cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __str__(self):
        return "\n".join([" ".join([str(i) for i in lst]) for lst in self.cells])

    def has_winner(self):
        """ """
        for i in range(3):
            our_sum = 0
            for j in range(3):
                our_sum += self.cells[i][j]
            if our_sum == 3:
                return 1
            if our_sum == -3:
                return -1
        for j in range(3):
            our_sum = 0
            for i in range(3):
                our_sum += self.cells[i][j]
            if our_sum == 3:
                return 1
            if our_sum == -3:
                return -1
        our_sum = self.cells[0][0] + self.cells[1][1] + self.cells[2][2]
        if our_sum == 3:
            return 1
        if our_sum == -3:
            return -1
        our_sum = self.cells[0][2] + self.cells[1][1] + self.cells[2][0]
        if our_sum == 3:
            return 1
        if our_sum == -3:
            return -1
        for j in range(3):
            for i in range(3):
                if self.cells[j][i] == 0:
                    return None
        return 0
    def make_random_move(self):
        for index in range(3):
            if self.cells[index].count(0) == 1 and sum(self.cells[index]) == 2:
                return (index, self.cells[index].index(0))

        for line in range(3):
            l1 = []
            l1.extend([self.cells[index][line] for index in range(3)])
            if sum([self.cells[index][line] for index in range(3)]) == 2 and l1.count(0) == 1:
                return (line, l1.index(0))

        if sum([self.cells[i][i] for i in range(3)]) == 2 and 0 in [self.cells[i][i] for i in range(3)]:
            return [(i, i) for i in range(3) if self.cells[i][i] == 0][0]

        if sum([self.cells[index][2 - index]for index in range(3)]) == 2 and 0 in [self.cells[index][2 - index]for index\
                                                                                   in range(3)]:
            return [(index, 2 - index)for index in range(3) if self.cells[index][2 - index] == 0][0]

        list_of_moves = []
        for line in range(3):
            for index in range(3):
                if self.cells[line][index] == 0:
                    list_of_moves.append((line, index))
        return random.choice(list_of_moves)

    def make_clever_random_move(self, player):
        lst_comp = []
        lst_human = []
        if player == -1:
            for y in range(3):
                s = 0
                for x in range(3):
                    s += self.cells[y][x]
                if s == -2:
                    for index in range(3):
                        if self.cells[index][y] == 0:
                            lst_comp.append((index,y))
                if s == 2:
                    for index in range(3):
                        if self.cells[y][index] == 0:
                            lst_human.append((y,index))

            for y in range(3):
                s = 0
                for x in range(3):
                    s += self.cells[x][y]
                if s == -2:
                    for index in range(3):
                        if self.cells[index][y] == 0:
                            lst_comp.append((y,index))
                if s == 2:
                    for index in range(3):
                        if self.cells[index][y] == 0:
                            lst_human.append((y,index))
            our_sum_2 = self.cells[0][0] + self.cells[1][1] + self.cells[2][2]
            if our_sum_2 == -2:
                for i in range(3):
                    if self.cells[i][i] == 0:
                        lst_comp.append((i,i))
            if our_sum_2 == 2:
                for i in range(3):
                    if self.cells[i][i] == 0:
                        lst_human.append((i,i))
            our_sum_2 = self.cells[0][2] + self.cells[1][1] + self.cells[2][0]
            if our_sum_2 == -2:
                for i in range(3):
                    if self.cells[i][2 - i] == 0:
                        lst_comp.append((i,i))
            if our_sum_2 == 2:
                for i in range(3):
                    if self.cells[i][2 - i] == 0:
                        lst_human.append((i,i))
        if player == 1:
            for y in range(3):
                s = 0
                for x in range(3):
                    s += self.cells[y][x]
                if s == 2:
                    for index in range(3):
                        if self.cells[y][index] == 0:
                            lst_human.append((index,y))
                if s == -2:
                    for index in range(3):
                        if self.cells[y][index] == 0:
                            lst_comp.append((index,y))

            for y in range(3):
                s = 0
                for x in range(3):
                    s += self.cells[x][y]
                if s == 2:
                    for index in range(3):
                        if self.cells[index][y] == 0:
                            lst_human.append((y,index))
                if s == -2:
                    for index in range(3):
                        if self.cells[index][y] == 0:
                            lst_comp.append((y,index))

            our_sum_2 = self.cells[0][0] + self.cells[1][1] + self.cells[2][2]
            if our_sum_2 == 2:
                for i in range(3):
                    if self.cells[i][i] == 0:
                        lst_human.append((i,i))
            if our_sum_2 == -2:
                for i in range(3):
                    if self.cells[i][i] == 0:
                        lst_comp.append((i,i))

            our_sum_2 = self.cells[0][2] + self.cells[1][1] + self.cells[2][0]
            if our_sum_2 == 2:
                for i in range(3):
                    if self.cells[i][2 - i] == 0:
                        lst_human.append((i,i))
            if our_sum_2 == -2:
                for i in range(3):
                    if self.cells[i][2 - i] == 0:
                        lst_comp.append((i,i))
        if player == -1:
            if lst_comp != []:
                return lst_comp[0]
            elif lst_human != []:
                return lst_human[0]
        elif player == 1:
            if lst_human != []:
                return lst_human[0]
            elif lst_comp != []:
                return lst_comp[0]
        return None
    def copy_board(self):
        new_board = Board()
        for y in range(3):
            for x in range(3):
                new_board.cells[y][x] = self.cells[y][x]
        return new_board
    def set_value(self, tuple, item):
        """ """
        self.cells[tuple[0]][tuple[1]] =  item
        return self.cells
    def best_pos(self):
        if self.cells[1][1] == 0:
            return self.cells[1][1]
