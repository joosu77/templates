import heapq
from collections import deque

from tree_node import TreeNode


class Tree:
    def __init__(self):
        self.root = None

    def add_root(self, data=None):
        self.root = TreeNode(data)
        return self.root

    def dijkstra(self):
        queue = []
        heapq.heappush(queue, (0, 0, self.root))
        i = 1
        while queue:
            dist, _, node = heapq.heappop(queue)
            # print(f"Visiting {node}")
            node.total_distance = dist
            for dist2, child in node.children:
                heapq.heappush(queue, (dist + dist2, i, child))
                i += 1

    def dijkstra_with_target(self, target):
        queue= []
        heapq.heappush(queue, (0, 0, self.root))
        i = 1
        while queue:
            dist, _, node = heapq.heappop(queue)
            node.total_distance = dist
            if node == target:
                return
            for dist2, child in node.children:
                heapq.heappush(queue, (dist + dist2, i, child))
                i += 1

    @staticmethod
    def get_path(source, target):
        # TODO: do significant testing on this
        stack = deque()
        stack.append((source, None))
        came_from_stack = []
        while stack:
            node, came_from = stack.pop()
            combined_expansion = node.children + [(0, node.root)]
            if came_from is None:
                came_from = source
            else:
                while came_from != came_from_stack[-1]:
                    came_from_stack.pop()
            combined_expansion = [x for x in combined_expansion if x[1] not in [came_from, None]]
            if len(combined_expansion) > 0:
                came_from_stack.append(node)
            for _, child in combined_expansion:
                if child == target:
                    # came_from_stack.append(node)
                    came_from_stack.append(child)
                    return came_from_stack
                stack.append((child, node))

    def dfs(self):
        stack = deque()
        stack.append(self.root)
        while stack:
            node = stack.pop()
            # print(f"Visiting {node}")
            for dist2, child in node.children:
                stack.append(child)


if __name__ == '__main__':
    tree = Tree()
    root = tree.add_root("A")
    b1 = root.add_child(TreeNode("B1"))
    b2 = root.add_child(TreeNode("B2"))
    c1 = b2.add_child(TreeNode("C1"))
    c2 = b2.add_child(TreeNode("C2"))
    tree.dijkstra()
    print(c2.total_distance)
    tree.dfs()
    print(tree.get_path(c2, c1))
