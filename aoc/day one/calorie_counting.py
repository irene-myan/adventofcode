# --- Day 1: Calorie Counting ---

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


def p1():
    max_so_far = 0
    cur_sum = 0
    for c in lines:
        if c == "":
            if cur_sum > max_so_far:
                max_so_far = cur_sum
            cur_sum = 0
        else:
            cur_sum += int(c)

    print(max_so_far)


def p2():
    elves = []
    cur_sum = 0
    for c in lines:
        if c == "":
            elves.append(cur_sum)
            cur_sum = 0
        else:
            cur_sum += int(c)

    elves.sort(reverse=True)
    print(sum(elves[:3]))
