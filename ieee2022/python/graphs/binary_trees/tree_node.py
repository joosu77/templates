

class TreeNode:
    def __init__(self, data):
        self.data = data

        self.parent = None
        self.left = None
        self.right = None

    def add_child(self, child, distance=1):
        child.root = self
        child.dist_to_parent = distance
        self.children.append((distance, child))
        return child

    def __repr__(self):
        return str(self.data)
