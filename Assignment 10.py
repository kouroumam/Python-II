

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        self._insert_recursively(self.root, data)

    def _insert_recursively(self, current, data):

        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursively(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursively(current.right, data)

    def in_order_traversal(self, node, visited):
        if node:
            self.in_order_traversal(node.left, visited)
            visited.append(node.data)
            self.in_order_traversal(node.right, visited)

    def pre_order_traversal(self, node, visited):
        if node:
            visited.append(node.data)
            self.pre_order_traversal(node.left, visited)
            self.pre_order_traversal(node.right, visited)

    def post_order_traversal(self, node, visited):
        if node:
            self.post_order_traversal(node.left, visited)
            self.post_order_traversal(node.right, visited)
            visited.append(node.data)

# Create a binary tree with root node value 37
tree = BinaryTree(37)

# Insert additional nodes
tree.insert(6)
tree.insert(4)
tree.insert(29)
tree.insert(65)
tree.insert(40)
tree.insert(17)

# Perform in-order traversal
in_order_result = []
tree.in_order_traversal(tree.root, in_order_result)
print("In-order Traversal:", in_order_result)

# Perform pre-order traversal
pre_order_result = []
tree.pre_order_traversal(tree.root, pre_order_result)
print("Pre-order Traversal:", pre_order_result)

# Perform post-order traversal
post_order_result = []
tree.post_order_traversal(tree.root, post_order_result)
print("Post-order Traversal:", post_order_result)