import heapq
from collections import deque

from node import Node


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key, data=None):
        self.nodes[key] = Node(key, data)

    def add_connection(self, source, target, distance=1):
        self.nodes[source].add_neighbour(self.nodes[target], distance)

    def add_bidirectional_connection(self, a, b, distance=1):
        self.nodes[a].add_neighbour(self.nodes[b], distance)
        self.nodes[b].add_neighbour(self.nodes[a], distance)

    def add_connection_with_object(self, source, target, distance=1):
        source.add_neighbour(target, distance)

    def add_bidirectional_connection_with_object(self, a, b, distance=1):
        a.add_neighbour(b, distance)
        b.add_neighbour(a, distance)

    def dijkstra(self, start):
        start_node = self.nodes[start]
        dists, prev, queue, explored = {}, {}, [], set()
        for key, node in self.nodes.items():
            dists[key] = float("inf")
            prev[key] = None
        dists[start] = 0
        heapq.heappush(queue, (0, start))
        while queue:
            dist, key = heapq.heappop(queue)
            if key in explored:
                continue
            explored.add(key)
            for dist2, neighbour in self.nodes[key].neighbours:
                alt_dist = dist + dist2
                if alt_dist < dists[neighbour.key]:
                    dists[neighbour.key] = alt_dist
                    prev[neighbour.key] = key
                    heapq.heappush(queue, (alt_dist, neighbour.key))
        return dists, prev

    def dijkstra_with_target(self, start, target):
        start_node = self.nodes[start]
        dists, prev, queue, explored = {}, {}, [], set()
        for key, node in self.nodes.items():
            dists[key] = float("inf")
            prev[key] = None
        dists[start] = 0
        heapq.heappush(queue, (0, start))
        while queue:
            dist, key = heapq.heappop(queue)
            if key in explored:
                continue
            if key == target:
                return dists, prev, True
            explored.add(key)
            for dist2, neighbour in self.nodes[key].neighbours:
                alt_dist = dist + dist2
                if alt_dist < dists[neighbour.key]:
                    dists[neighbour.key] = alt_dist
                    prev[neighbour.key] = key
                    heapq.heappush(queue, (alt_dist, neighbour.key))
        return dists, prev, False

    @staticmethod
    def get_path(source, target, dists, prev):
        path = []
        current = target
        while current != source:
            if prev[current] is None:
                return None
            path.append(current)
            current = prev[current]
        path.append(source)
        return path[::-1], dists[target]

    def dfs(self, start):
        visited = set()
        stack = deque()
        stack.append(start)
        while stack:
            next_key = stack.pop()
            if next_key in visited:
                continue
            print(f"Visiting {next_key}")
            visited.add(next_key)
            for _, neighbour in self.nodes[next_key].neighbours:
                stack.append(neighbour.key)


if __name__ == '__main__':
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_bidirectional_connection("A", "B", 1)
    graph.add_bidirectional_connection("A", "C", 2)
    graph.add_bidirectional_connection("B", "D", 10)
    graph.add_bidirectional_connection("C", "D", 4)
    graph.add_bidirectional_connection("B", "C", 2)
    dists, prev, success = graph.dijkstra_with_target("A", "D")
    print(f"Path from 'A' to 'D': {Graph.get_path('A', 'D', dists, prev)}")

    print("Doing DFS")
    graph.dfs("B")
