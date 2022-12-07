# --- Day 7: No Space Left On Device ---

lines = []
with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]


class Node:
    def __init__(self, size, name):
        self.parent = None
        self.name = name
        self.size = size
        self.children = []

    def increase_size(self, size):
        self.size += size

        if self.parent:
            self.parent.increase_size(size)

    def add_child(self, size, name):
        self.children.append(Node(size, name))
        self.children[-1].parent = self
        self.increase_size(size)

    def get_all_p1(self):
        ar = []
        for m in self.children:
            if m.size <= 100000:
                ar.append(m.size)
            gotten = m.get_all()
            if len(gotten) > 0:
                ar += gotten

        return ar

    def get_all(self):
        ar = []
        for m in self.children:
            ar.append(m.size)
            gotten = m.get_all()
            if len(gotten) > 0:
                ar += gotten

        return ar


def load_tree():
    root = Node(0, "root")
    cur = root
    for line in lines:
        if line[0] == "$":
            a = line.split(" ")
            if a[1] == "cd":
                if a[2] == "/":
                    cur = root
                if a[2] == "..":
                    cur = cur.parent
                else:
                    for k in cur.children:
                        if k.name == a[2]:
                            cur = k
        else:
            cmd, name = line.split(" ")
            if cmd == "dir":
                cur.add_child(0, name)
            else:
                cur.increase_size(int(cmd))

    return root


def p1():
    root = load_tree()

    aa = root.get_all_p1()
    print(sum(aa))


def p2():
    root = load_tree()

    aa = sorted(root.get_all())

    unused_space = 70000000 - root.size
    space_needed = 30000000 - unused_space

    for i in aa:
        if i >= space_needed:
            print(i)
            break
