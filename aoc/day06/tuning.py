# --- Day 6: Tuning Trouble ---

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


def p(marker_len):
    line = lines[0]
    c = marker_len - 2
    m = set(line[0:marker_len])
    for i in range(len(line)):
        c += 1
        if len(m) == marker_len:
            break
        m = set(line[i : i + marker_len])

    print(c)
