# --- Day 4: Camp Cleanup ---

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


def contains(r1s, r1e, r2s, r2e):
    return int(r1s) <= int(r2s) and int(r1e) >= int(r2e)


def p1():
    fully_containing = 0
    for line in lines:
        r1, r2 = line.split(",")
        r1s, r1e = r1.split("-")
        r2s, r2e = r2.split("-")

        if contains(r1s, r1e, r2s, r2e) or contains(r2s, r2e, r1s, r1e):
            fully_containing += 1

    print(fully_containing)


def p2():
    overlaps = 0
    for line in lines:
        r1, r2 = line.split(",")
        r1s, r1e = r1.split("-")
        r2s, r2e = r2.split("-")

        # if theres an overlap, the start of one range must be in the other
        if contains(r1s, r1e, r2s, r2s) or contains(r2s, r2e, r1s, r1s):
            overlaps += 1

    print(overlaps)
