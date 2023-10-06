import heapq
import math


class Graph:

    def __init__(self):
        self.edges = {}  # edges alike {from: [to, weight]}
        self.vertexes = set()

    def add_edge(self, start, finish, weight=1, directed=False):
        self.vertexes.add(start)
        self.vertexes.add(finish)
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append([finish, weight])
        if not directed:
            if finish not in self.edges:
                self.edges[finish] = []
            self.edges[finish].append([start, weight])

    def dijkstra(self, start, finish=None, get_path=False):
        open_set = [(1, start)]
        came_from = {}
        dist = {start: 0}

        while open_set:
            current = heapq.heappop(open_set)[1]
            if finish is not None and current == finish:
                break
            if current not in self.edges:
                continue
            for neighbor, weight in self.edges[current]:
                alt = dist[current] + weight
                if neighbor not in dist or alt < dist[neighbor]:
                    dist[neighbor] = alt
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (alt, neighbor))
        return self.reconstruct_path(came_from, start, finish) if get_path else came_from

    def reconstruct_path(self, came_from, start, finish):
        path = [finish]
        current = finish
        while current != start:
            current = came_from[current]
            path.append(current)
        return path

    def bfs(self, start, finish=None, get_path=False):
        open_set = {start}
        came_from = {start: start}
        temp_set = set()

        while open_set:
            current = open_set.pop()
            if finish is not None and current == finish:
                break
            if current not in self.edges:
                continue
            for neighbor, weight in self.edges[current]:
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    temp_set.add(neighbor)
            if not open_set:
                open_set = temp_set
                temp_set = set()
        return self.reconstruct_path(came_from, start, finish) if get_path else came_from

    def dfs(self, start):
        been = set()

        def dfs_rec(current):
            # print(current)
            been.add(current)
            if current not in self.edges:
                return
            for goto in self.edges[current]:
                if goto[0] not in been:
                    dfs_rec(goto[0])

        dfs_rec(start)

    def get_inverse_graph(self):
        g = Graph()
        for start, end in self.edges.items():
            for dest in end:
                g.add_edge(dest[0], start, dest[1], directed=True)
        return g

    def floyd_warshall(self):
        dist = dict()
        for a in self.vertexes:
            for b in self.vertexes:
                dist[(a, b)] = math.inf
                dist[(b, a)] = math.inf
            dist[(a, a)] = 0
        for k, v in self.edges.items():
            for dest in v:
                dist[(k, dest[0])] = dest[1]

        for k in self.vertexes:
            for i in self.vertexes:
                for j in self.vertexes:
                    dist[(i, j)] = min(dist[(i, j)], dist[(i, k)] + dist[(k, j)])

        return dist


class FenwickTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.BITTree = [0] * (self.n + 1)
        for i in range(self.n):
            self.updatebit(i, arr[i])

    def getsum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.BITTree[i]
            i -= i & (-i)
        return s

    def get_sum_range(self, start, finish):
        if start >= finish:
            return 0
        return self.getsum(finish - 1) - self.getsum(start - 1)

    def updatebit(self, idx, delta):
        idx += 1
        while idx <= self.n:
            self.BITTree[idx] += delta
            idx += idx & (-idx)


class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, item):
        self.parent[item] = item
        self.size[item] = 1

    def get_size(self, item):
        return self.size[self.find(item)]

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        self.parent[root1] = root2
        self.size[root2] += self.size[root1]


def is_prime(n):
    if n <= 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_up_to_n(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def binary_search(arr, val, l=None, h=None):
    # assert arr == sorted(arr)
    if l is None or h is None:
        return binary_search(arr, val, 0, len(arr) - 1)
    if l > h:
        return -1
    mid = (l + h) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, h)
    if arr[mid] > val:
        return binary_search(arr, val, l, mid - 1)
    return mid


def read_str_row(delimiter=" "):
    return input().split(delimiter)


def read_float_row(delimiter=" "):
    return [float(x) for x in read_str_row(delimiter)]


def read_int_row(delimiter=" "):
    return [int(x) for x in read_str_row(delimiter)]


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    s = g.get_inverse_graph().floyd_warshall()
    print(s)
    s = g.dijkstra(3, 5, get_path=True)
    print(s)

    d = DisjointSet()
    d.add("aa")
    d.add("bb")
    d.add("cc")
    d.add("dd")
    d.union("aa", "bb")
    d.union("dd", "cc")
    d.union("aa", "cc")
    print(d.parent)
