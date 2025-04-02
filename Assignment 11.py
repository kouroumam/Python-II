

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value) # if the tree is empty, then create the root node with whatever, value that was given
        else:
            self.insert_rec(self.root, value)

    def insert_rec(self, node, value):

        if value < node.value:

            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_rec(node.right, value)

    def search(self, value):

        return self.search_rec(self.root, value)

    def search_rec(self, node, value):

        if node is None:
            return False

        if value == node.value:
            return True

        elif value < node.value:
            return self.search_rec(node.left, value)

        else:
            return self.search_rec(node.right, value)

def test():
    binary_test = BinarySearchTree()

    binary_test.insert(50)
    binary_test.insert(30)
    binary_test.insert(70)
    binary_test.insert(20)
    binary_test.insert(40)
    binary_test.insert(60)
    binary_test.insert(80)

    print("Search for value 40: ", binary_test.search(40))
    print("Search for value 25: ", binary_test.search(25))

test()