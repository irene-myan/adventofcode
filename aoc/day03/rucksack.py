# --- Day 3: Rucksack Reorganization ---

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


def priority(item):
    if item.isupper():
        return ord((item).swapcase()) - ord("A") - 5
    return ord((item).swapcase()) - ord("A") + 1


def same(f, s):
    f = list(f)
    s = list(s)
    return list(set(f).intersection(s))


def badge(group):
    group = [list(r) for r in group]
    badge = same(same(group[0], group[1]), group[2])
    return priority(badge[0])


def p1():
    priority_sum = 0
    for line in lines:
        f, s = line[: len(line) // 2], line[len(line) // 2 :]
        priority_sum += priority(same(f, s)[0])

    print(priority_sum)


def p2():
    priority_sum = 0
    cur_group = []
    for line in lines:
        if len(cur_group) == 3:
            priority_sum += badge(cur_group)
            cur_group = [line]
        else:
            cur_group.append(line)

    priority_sum += badge(cur_group)

    print(priority_sum)
