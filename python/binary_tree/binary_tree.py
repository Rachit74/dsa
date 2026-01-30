"""
a binary tree has exactly at most 2 child for each node
in a binary search tree left nodes are smaller than the parent node and right nodes are larger than the parent node
"""

class Node:
    data: int
    left: Node
    right: Node

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root: Node

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            new_node = Node(data)
            self.root = new_node
            return
        
        self._insert(self.root, data)

    def _insert(self, node: Node, data: int):

        # if the data is smaller than the data of parent node, insert to the left
        if data < node.data:
            # check if the left node is empty or not
            if node.left is None:
                # insert the new node as left child if it is none
                node.left = Node(data)
                return
            else:
                # call the _insert function again recursively if the node is not empty
                self._insert(node.left, data)

        # if the data is larger than the data of parent node, insert to the right
        elif data > node.data:
            # check if the right node is empty or not
            if node.right is None:
                # insert the new node as left child if it is none
                node.right = Node(data)
                return
            else:
                # call the _insert function again recursively if the node is not empty
                self._insert(node.right, data)

    def preOrder(self):
        root = self.root
        self._pre_order(node=root)

    def _pre_order(self, node):
        if node is None:
            return
        print(node.data)
        self._pre_order(node.left)
        self._pre_order(node.right)

    
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return 1 + max (left_height, right_height)


tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(5)

tree.preOrder()