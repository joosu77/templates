
from up_tree_order import UpTreeOrder as UpTree
# from up_tree_size import UpTreeSize as UpTree




class DisjointSubsets:
    def __init__(self):
        self.elements = {}

    def add(self, index, data):
        self.elements[index] = (UpTree(index), data)

    def add_with_check(self, index, data):
        if index not in self.elements.keys():
            self.elements[index] = (UpTree(index), data)

    def find(self, index):
        return self.elements[index]

    def find_with_check(self, index):
        if index in self.elements.keys():
            return self.elements[index]

    def find_with_add(self, index, default_data):
        if index in self.elements.keys():
            return self.elements[index]
        self.elements[index] = (UpTree(index), default_data)
        return self.elements[index]

    def join(self, a, b):
        UpTree.union(self.find(a)[0], self.find(b)[0])

    def join_with_check(self, a, b):
        a_el = self.find_with_check(a)
        if a_el is None:
            return False
        b_el = self.find_with_check(b)
        if b_el is None:
            return False
        UpTree.union(a_el[0], b_el[0])
        return True

    def join_with_add(self, a, b, default_data_a, default_data_b):
        a_el = self.find_with_add(a, default_data_a)
        b_el = self.find_with_add(b, default_data_b)
        UpTree.union(a_el[0], b_el[0])

    def in_same(self, a, b):
        a_el = self.find(a)
        b_el = self.find(b)
        return UpTree.in_same_set(a_el[0], b_el[0])

    def in_same_with_check(self, a, b):
        a_el = self.find_with_check(a)
        if a_el is None:
            return False
        b_el = self.find_with_check(b)
        if b_el is None:
            return False
        return UpTree.in_same_set(a_el[0], b_el[0])
