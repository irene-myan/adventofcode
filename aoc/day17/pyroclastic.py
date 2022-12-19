# --- Day 17: Pyroclastic Flow ---


from abc import abstractclassmethod
from math import floor

from cave import WIDTH, cave, print_cave, tallest
from rocks import L, Line, Plus, Square, Tall

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]
# lines = [">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"]
line = lines[0]

MAX_ROCKS = 2022
ROCKS = [Line, Plus, L, Tall, Square]
TRILLION = 1000000000000


def p1():
    global cave
    global line

    cur_move = 0
    for i in range(MAX_ROCKS):
        cur_rock = i % 5
        start_pos = [tallest() + 3, 2]
        while len(cave) <= start_pos[0]:
            cave.append(list("." * WIDTH))
        cur_rock = ROCKS[cur_rock](start_pos)

        cur_rock.move(line[cur_move % len(line)])
        cur_move += 1
        while cur_rock.drop():
            cur_rock.move(line[cur_move % len(line)])
            cur_move += 1

        cur_rock.set_points_as("#")

    print(tallest())


def p2():
    global cave
    global line
    det_loop = False
    height_offset = ""
    cache = {}

    cur_height = tallest()
    cur_move = 0
    i = 0
    while i < TRILLION:
        cur_rock = i % 5
        start_pos = [cur_height + 3, 2]
        while len(cave) <= start_pos[0]:
            cave.append(list("." * WIDTH))

        cur_rock = ROCKS[cur_rock](start_pos)

        cur_rock.move(line[cur_move % len(line)])

        while cur_rock.drop():
            cur_move += 1
            cur_rock.move(line[cur_move % len(line)])

        cur_move += 1
        cur_rock.set_points_as("#")

        cur_height = tallest()
        i += 1
        if i == 2021:  # Assuming the cycle has already started
            cache[(i % 5, cur_move % len(line))] = i, cur_height
        elif not det_loop and i > 2021 and (i % 5, cur_move % len(line)) in cache:
            move_num, height = cache[(i % 5, cur_move % len(line))]

            # Skip cycles - get to last cycle
            loop_len = i - move_num
            num_future_cycles = floor((TRILLION - i) / loop_len)
            i += loop_len * num_future_cycles

            dh = cur_height - height
            height_offset = dh * num_future_cycles

            det_loop = True

    print(tallest() + height_offset)
