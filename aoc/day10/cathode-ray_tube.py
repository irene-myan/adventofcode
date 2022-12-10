# --- Day 10: Cathode-Ray Tube ---


lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


crt = ""
cycle_num = 0


def cycle(x):
    global cycle_num, crt

    cycle_num += 1

    draw_pos = (cycle_num - 1) % 40

    crt += "♥" if abs(draw_pos - x) <= 1 else " "


def p1():
    x = 1
    cycles = []
    for line in lines:
        if line[0] == "n":
            cycles.append(x)
        else:
            _, am = line.split(" ")

            cycles.append(x)
            cycles.append(x)

            x += int(am)

    cycle_strength = 0
    for i in range(1, 220):
        if ((i + 1) - 20) % 40 == 0:
            cycle_strength += (i + 1) * cycles[i]

    print(cycle_strength)


def p2():
    x = 1
    for line in lines:
        if line[0] == "n":
            cycle(x)
        else:
            _, am = line.split(" ")

            cycle(x)
            cycle(x)

            x += int(am)

    for i in range(6):
        print(crt[i * 40 : (i + 1) * 40 - 1])


p1()
p2()
