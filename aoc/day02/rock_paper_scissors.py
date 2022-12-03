# --- Day 2: Rock Paper Scissors ---

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


def shape_points(shape):
    if shape == "A" or shape == "X":
        return 1
    if shape == "B" or shape == "Y":
        return 2
    if shape == "C" or shape == "Z":
        return 3


def won(me, op):
    if me > op:
        return me - op == 1
    return op - me > 1


def winners_score(op):
    return op + 1 % 3


def losers_score(op):
    return op - 1 % 3


def p1():
    op_score = 0
    my_score = 0

    for line in lines:
        op, me = line.split()

        op = shape_points(op)
        me = shape_points(me)

        op_score += op
        my_score += me

        if me == op:
            my_score += 3
            op_score += 3
        elif won(me, op):
            my_score += 6
        else:
            op_score += 6

    print(my_score)
    print(op_score)


def p2():
    op_score = 0
    my_score = 0

    for line in lines:
        op, end = line.split()

        op = shape_points(op)
        end = (shape_points(end) - 1) * 3

        op_score += op
        my_score += end

        if end == 0:
            my_score += losers_score(op)
        elif end == 6:
            my_score += winners_score(op)
        else:
            my_score += op

    print(my_score)
    print(op_score)
