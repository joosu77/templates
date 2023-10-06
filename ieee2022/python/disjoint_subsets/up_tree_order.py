import random
import time


class UpTreeOrder:

    def __init__(self, index):
        self.index = index
        self.parent = self
        self.order = 0

    def find(self):
        root = self
        while root.parent != root:
            root = root.parent

        active = self
        while active != root:
            next = active.parent
            active.parent = root
            active = next

        return root

    def find_path_split(self):
        active = self
        while active.parent != active:
            active, active.parent = active.parent, active.parent.parent
        return active

    def find_path_halving(self):
        active = self
        while active.parent != active:
            active.parent = active.parent.parent
            active = active.parent
        return active

    get_root = find

    @staticmethod
    def union(a, b):
        a_root = a.get_root()
        b_root = b.get_root()
        if a_root.order < b_root.order:
            a_root.parent = b_root
        elif b_root.order < a_root.order:
            b_root.parent = a_root
        else:
            a_root.parent = b_root
            b_root.order += 1

    @staticmethod
    def union_with_return(a, b):
        a_root = a.get_root()
        b_root = b.get_root()
        if a_root.order < b_root.order:
            a_root.parent = b_root
            return b_root
        if b_root.order < a_root.order:
            b_root.parent = a_root
            return a_root
        a_root.parent = b_root
        b_root.order += 1
        return b_root

    @staticmethod
    def in_same_set(a, b):
        return a.get_root() == b.get_root()


if __name__ == '__main__':
    trees = []
    total_time = 0
    total_time -= time.time()
    for i in range(1000000):
        tree = UpTreeOrder(i)
        trees.append(tree)
        UpTreeOrder.union(tree, random.choice(trees))
    total_time += time.time()
    print(total_time)
