import random


class Tile:
    def __init__(self, value):
        self.value = value


class Board:
    def __init__(self, size, numberOfColors):
        self.size = size
        self.numberOfColors = numberOfColors
        self.tiles = [[Tile(0) for x in range(size)] for y in range(size)]
        self.colorStatus = [0 for x in range(numberOfColors)]
        self.rounds = 0

    def reset_tiles(self):
        for i in range(self.size):
            for j in range(self.size):
                random_color = random.randint(1, self.numberOfColors)
                self.tiles[i][j].value = random_color
                self.colorStatus[random_color - 1] += 1
        self.rounds = 0

    def do_round(self):
        mode = random.randint(0, 1)
        y = random.randint(1, self.size * (self.size - 1))
        self.random_swap_color(mode, y)
        self.rounds += 1

    def random_swap_color(self, mode, y):
        i1 = int()
        j1 = int()
        i2 = int()
        j2 = int()
        n = self.size

        if mode == 0:
            i1 = (y - 1) % n
            j1 = (y - 1) // n
            i2 = i1
            j2 = j1 + 1
        elif mode == 1:
            i1 = (y - 1) // n
            j1 = (y - 1) % n
            i2 = i1 + 1
            j2 = j1

        base_tile = random.randint(1, 2)
        if base_tile == 1:
            self.colorStatus[self.tiles[i2][j2].value - 1] -= 1
            self.colorStatus[self.tiles[i1][j1].value - 1] += 1
            self.tiles[i2][j2].value = self.tiles[i1][j1].value
        elif base_tile == 2:
            self.colorStatus[self.tiles[i1][j1].value - 1] -= 1
            self.colorStatus[self.tiles[i2][j2].value - 1] += 1
            self.tiles[i1][j1].value = self.tiles[i2][j2].value

    def is_uniformed(self):
        number_of_zeros = 0
        for i in range(self.numberOfColors):
            if self.colorStatus[i] == 0:
                number_of_zeros += 1
        # print("NNNN" , number_of_zeros)
        if number_of_zeros == self.numberOfColors - 1:
            return True
        else:
            return False

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.tiles[i][j].value, end=" ")
            print()


class Round:
    def __init__(self, board):
        self.board = board


# size = int(input())
# colors = int(input())
#
# board = Board(size, colors)
#
# board.reset_tiles()
#
#
# board.do_round()
#
# while not board.is_uniformed():
#     board.do_round()
#     # board.print()
#
# print(board.rounds)