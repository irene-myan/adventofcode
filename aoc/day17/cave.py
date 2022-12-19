cave = []

WIDTH = 7


def print_cave():
    p = reversed(cave)
    for i in p:
        for j in i:
            print(j, end="")
        print("")
    print("_____________")


def tallest():
    height = 0
    for i in range(len(cave) - 1, -1, -1):
        if "#" in cave[i]:
            height = i + 1
            break

    del cave[height:]

    return height
