# --- Day 9: Rope Bridge ---

from math import ceil

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]

# Theres a more efficient way of doing this but I dont want to
GRID_SIZE = 10000
ROPE_LENGTH = 10

grid = []
for i in range(GRID_SIZE):
    grid.append(["_"] * GRID_SIZE)


# Used for testing
def print_grid():
    global grid
    print("~" * GRID_SIZE)
    for i in grid:
        print(" ".join(i))


def touching(head, tail):
    if head == tail:
        return True
    if head[0] == tail[0]:
        return abs(head[1] - tail[1]) == 1
    if head[1] == tail[1]:
        return abs(head[0] - tail[0]) == 1
    return abs(head[1] - tail[1]) == 1 and abs(head[0] - tail[0]) == 1


def new_loc(head, tail):
    if touching(head, tail):
        return tail

    if head[0] == tail[0]:  # ..T.H..
        return [tail[0], (head[1] + tail[1]) / 2]
    if head[1] == tail[1]:
        return [(head[0] + tail[0]) / 2, tail[1]]

    if abs(head[0] - tail[0]) == 1:  # horizontal diagonal
        return [head[0], ceil((head[1] + tail[1]) / 2)]
    if abs(head[1] - tail[1]) == 1:  # vertical diagonal
        return [ceil((head[0] + tail[0]) / 2), head[1]]


def move_tail_p1(head, tail):
    global grid

    tail = new_loc(head, tail)
    grid[int(tail[0])][int(tail[1])] = "#"

    return tail


def move_tail_p2(rope):
    global grid

    for i in range(1, ROPE_LENGTH):
        if rope[i] is None:
            rope[i] = [0, 0]
            break
        rope[i] = new_loc(rope[i - 1], rope[i])

    if rope[-1]:
        grid[int(rope[-1][0])][int(rope[-1][1])] = "#"

    return rope


def p1():

    global grid

    head = [0, 0]
    tail = [0, 0]

    for line in lines:
        dr, am = line.split(" ")
        am = int(am)
        if dr == "R":
            while am:
                head = [head[0], head[1] + 1]
                tail = move_tail_p1(head, tail)
                am -= 1
        elif dr == "L":
            while am:
                head = [head[0], head[1] - 1]
                tail = move_tail_p1(head, tail)
                am -= 1
        elif dr == "U":
            while am:
                head = [head[0] + 1, head[1]]
                tail = move_tail_p1(head, tail)
                am -= 1
        elif dr == "D":
            while am:
                head = [head[0] - 1, head[1]]
                tail = move_tail_p1(head, tail)
                am -= 1

    tail_visits = sum([i.count("#") for i in grid])
    print(tail_visits)


def p2():

    global grid

    rope = [None] * ROPE_LENGTH
    rope[0] = [0, 0]

    for line in lines:
        dr, am = line.split(" ")
        am = int(am)
        if dr == "R":
            while am:
                rope[0] = [rope[0][0], rope[0][1] + 1]
                rope = move_tail_p2(rope)
                am -= 1
        elif dr == "L":
            while am:
                rope[0] = [rope[0][0], rope[0][1] - 1]
                rope = move_tail_p2(rope)
                am -= 1
        elif dr == "U":
            while am:
                rope[0] = [rope[0][0] + 1, rope[0][1]]
                rope = move_tail_p2(rope)
                am -= 1
        elif dr == "D":
            while am:
                rope[0] = [rope[0][0] - 1, rope[0][1]]
                rope = move_tail_p2(rope)
                am -= 1

    tail_visits = sum([i.count("#") for i in grid])
    print(tail_visits)


p2()
