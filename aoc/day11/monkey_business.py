# --- Day 11: Monkey in the Middle ---

from math import floor

from numpy import prod

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


class Monkey:
    def __init__(self, items, op, div_by, true, false):
        self.items, self.op, self.div_by, self.true, self.false = items, op, div_by, true, false
        self.times_inspected = 0


def parse_monkeys():
    global monkeys, M
    for i in range(len(lines)):
        if len(lines[i]) and lines[i][0] == "M":
            items = list((lines[i + 1].split(":")[1]).split(","))
            items = [int(j.strip()) for j in items]

            op_fxn = (lines[i + 2].split("= "))[1]

            div_by = int(lines[i + 3].split("by ")[-1])
            M *= div_by

            true = int(lines[i + 4].split("monkey ")[-1])
            false = int(lines[i + 5].split("monkey ")[-1])

            monkeys.append(Monkey(items, op_fxn, div_by, true, false))


monkeys = []
M = 1


def inspect_items_p1(monkey):
    global monkeys

    for i in range(len(monkey.items)):
        monkey.times_inspected += 1
        new = floor(eval(monkey.op, None, {"old": monkey.items[i]}) / 3)

        if new % monkey.div_by == 0:
            monkeys[monkey.true].items.append(new)
        else:
            monkeys[monkey.false].items.append(new)

        monkey.items[i] = None

    res = []
    for i in range(len(monkey.items)):
        if monkey.items[i] is not None:
            res.append(monkey.items[i])
    monkey.items = res


def inspect_items_p2(monkey):
    global monkeys

    for i in range(len(monkey.items)):
        monkey.times_inspected += 1
        new = eval(monkey.op, None, {"old": monkey.items[i]})
        new %= M
        if new % monkey.div_by == 0:
            monkeys[monkey.true].items.append(new)
        else:
            monkeys[monkey.false].items.append(new)

        monkey.items[i] = None

    res = []
    for i in range(len(monkey.items)):
        if monkey.items[i] is not None:
            res.append(monkey.items[i])
    monkey.items = res


def p1():
    parse_monkeys()

    for _ in range(20):
        for monkey in monkeys:
            inspect_items_p1(monkey)

    top_inspected = sorted([m.times_inspected for m in monkeys])[-2:]
    print(prod(top_inspected))


def p2():
    parse_monkeys()

    for _ in range(1000):
        for monkey in monkeys:
            inspect_items_p2(monkey)

    top_inspected = sorted([m.times_inspected for m in monkeys])[-2:]
    print(prod(top_inspected))
