class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

    def find_minimum(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.val

# Приклад використання
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(15)
bst.insert(3)

min_value = bst.find_minimum()
print(min_value)  # Виведе 3