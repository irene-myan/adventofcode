# --- Day 5: Supply Stacks ---

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


stacks = [
    ["G", "T", "R", "W"],
    ["G", "C", "H", "P", "M", "S", "V", "W"],
    ["C", "L", "T", "S", "G", "M"],
    ["J", "H", "D", "M", "W", "R", "F"],
    ["P", "Q", "L", "H", "S", "W", "F", "J"],
    ["P", "J", "D", "N", "F", "M", "S"],
    ["Z", "B", "D", "F", "G", "C", "S", "J"],
    ["R", "T", "B"],
    ["H", "N", "W", "L", "C"],
]


def parse_stacks():
    for i in range(len(lines)):
        if lines[i].split(" ")[0] == "1":
            print(lines[i])


def move(fro, to):
    stacks[to - 1].append(stacks[fro - 1][-1])
    stacks[fro - 1].pop()


def move_many(num, fro, to):
    for i in range(num):
        stacks[to - 1].append(stacks[fro - 1][-(num - i)])
    del stacks[fro - 1][-num:]


def p1():

    for line in lines:
        if len(line) > 1 and line[0] == "m":
            _, num, _, fr, _, to = line.split(" ")
            for _ in range(int(num)):
                move(int(fr), int(to))

    top = [s[-1] for s in stacks]
    print("".join(top))


def p2():
    for line in lines:
        if len(line) > 1 and line[0] == "m":
            _, num, _, fr, _, to = line.split(" ")
            move_many(int(num), int(fr), int(to))

    top = [s[-1] for s in stacks]
    print("".join(top))
