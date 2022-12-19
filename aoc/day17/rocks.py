from cave import WIDTH, cave, print_cave


class Rock:
    def set_points_as(self, symb):
        global cave
        for p1, p2 in self.points:
            cave[p1][p2] = symb

    def move(self, dir):
        global cave

        temp_points = [[y, x + (1 if dir == ">" else -1)] for y, x in self.points]

        if self.no_intercept(temp_points):
            self.set_points_as(".")
            self.points = temp_points
            self.set_points_as("@")

    def drop(self):
        global cave

        temp_points = [[y - 1, x] for y, x in self.points]
        if not self.no_intercept(temp_points):
            return False

        self.set_points_as(".")
        self.points = temp_points
        self.set_points_as("@")

        return True

    def no_intercept(self, new_points):
        for i in range(len(new_points)):
            if new_points[i][1] < 0 or new_points[i][1] >= WIDTH:
                return False
            if new_points[i][0] < 0:
                return False
            if cave[new_points[i][0]][new_points[i][1]] == "#":
                return False
        return True


class Line(Rock):
    def __init__(self, start_pos):
        y, x = start_pos

        self.points = [[y, x], [y, x + 1], [y, x + 2], [y, x + 3]]

        self.set_points_as("@")


class Plus(Rock):
    def __init__(self, start_pos):
        y, x = start_pos

        self.points = [[y + 1, x], [y, x + 1], [y + 1, x + 1], [y + 2, x + 1], [y + 1, x + 2]]
        cave.append(list("." * WIDTH))
        cave.append(list("." * WIDTH))

        self.set_points_as("@")


class L(Rock):
    def __init__(self, start_pos):
        y, x = start_pos

        self.points = [[y, x], [y, x + 1], [y, x + 2], [y + 1, x + 2], [y + 2, x + 2]]
        cave.append(list("." * WIDTH))
        cave.append(list("." * WIDTH))

        self.set_points_as("@")


class Tall(Rock):
    def __init__(self, start_pos):
        y, x = start_pos

        self.points = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]]
        cave.append(list("." * WIDTH))
        cave.append(list("." * WIDTH))
        cave.append(list("." * WIDTH))

        self.set_points_as("@")


class Square(Rock):
    def __init__(self, start_pos):
        y, x = start_pos

        self.points = [[y, x], [y + 1, x + 1], [y + 1, x], [y, x + 1]]
        cave.append(list("." * WIDTH))

        self.set_points_as("@")
