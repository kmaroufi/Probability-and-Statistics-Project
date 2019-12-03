import random


class Graph:
    def __init__(self, size, average_degree, number_of_colors, build_type):
        self.size = int(size)
        self.average_degree = int(average_degree)
        self.e = self.set_e()
        self.number_of_colors = int(number_of_colors)
        self.build_type = int(build_type)

        self.edges = [[0 for x in range(2)] for y in range(self.e)]
        self.matrix = [[0 for x in range(self.size)] for y in range(self.size)]
        self.vertices = [Node(i) for i in range(self.size)]

        self.reset_show_colors()
        self.build()

        self.rounds = 0

    def build(self):
        if self.build_type == 0:
            self.build_normal_graph()
        elif self.build_type == 1:
            self.build_connected_graph()

        self.set_edges()

    def is_uniformed(self):
        first_show_color = self.vertices[0].show_color
        for i in range(1, self.size):
            if self.vertices[i].show_color != first_show_color:
                return False

        return True

    def do_round(self):
        rand_edge = random.randint(0, self.e - 1)
        v1 = self.vertices[self.edges[rand_edge][0]]
        v2 = self.vertices[self.edges[rand_edge][1]]

        mode = random.randint(0, 1)
        if mode == 0:
            v1.show_color = v2.show_color
        elif mode == 1:
            v2.show_color = v1.show_color
        self.rounds += 1

    def set_edges(self):
        added = 0
        for i in range(self.size - 1):
            for j in range(i + 1, self.size):
                if self.matrix[i][j] == 1:
                    self.edges[added][0] = i
                    self.edges[added][1] = j
                    added += 1

    def reset_show_colors(self):
        for i in range(self.size):
            color_i = random.randint(1, self.number_of_colors)
            self.vertices[i].show_color = color_i

    def build_normal_graph(self):
        used = 0
        while used != self.e:
            x = random.randint(0, self.size - 2)
            y = random.randint(x + 1, self.size - 1)

            if self.matrix[x][y] == 0:
                self.matrix[x][y] = 1
                self.matrix[y][x] = 1
                used += 1

    def build_connected_graph(self):
        while True:
            self.reset_matrix()
            self.build_normal_graph()
            if self.is_connected():
                break

    def reset_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = 0

    def set_e(self):
        e = self.size * self.average_degree / 2
        maximum = self.size * (self.size - 1) / 2
        if e > maximum:
            e = maximum
        return int(e)

    def is_connected(self):
        u = self.vertices[0]
        self.dfs_visit(u)

        result = True
        for i in range(self.size):
            if self.vertices[i].dfs_color != 2:
                result = False

        self.reset_dfs_colors()
        return result

    def reset_dfs_colors(self):
        for i in range(self.size):
            self.vertices[i].dfs_color = 0

    def dfs_visit(self, u):
        u.dfs_color = 1
        for i in range(self.size):
            if self.matrix[i][u.number] != 0:
                if self.vertices[i].dfs_color == 0:
                    self.dfs_visit(self.vertices[i])
        u.dfs_color = 2

    def print_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.matrix[i][j], end=" ")
            print()

        print()

    def print_show_colors(self):
        for i in range(self.size):
            print(self.vertices[i].show_color, end=" ")
        print()

    def print_edges(self):
        for i in range(self.e):
            for j in range(2):
                print(self.edges[i][j], end=" ")
            print()


class Node:
    def __init__(self, number):
        self.number = number
        self.dfs_color = 0
        self.show_color = 0


# n = input()
# m = input()
# c = input()
#
# graph1 = Graph(n, m, c, 1)
#
#
# print(graph1.e)
# graph1.print_show_colors()
# print(graph1.is_connected())
# graph1.print_matrix()
# graph1.print_edges()
#
# while not graph1.is_uniformed():
#     graph1.print_show_colors()
#     graph1.do_round()
#
# graph1.print_show_colors()

# graph2 = Graph(n, m, c, 0)
# print(graph2.e)
# print(graph2.is_connected())
# graph2.print_matrix()
# graph2.print_show_colors()
