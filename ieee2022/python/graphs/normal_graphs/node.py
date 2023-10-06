

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.neighbours = []

    def add_neighbour(self, neighbour, distance=1):
        self.neighbours.append((distance, neighbour))
