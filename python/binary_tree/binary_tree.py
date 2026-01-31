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
        # if the tree is empty we create a new root node
        if self.root is None:
            self.root = Node(data)
            return
        
        # if the tree is not empty we call the insert logic (private _insert function) on the root node
        self._insert(self.root, data)

    
    """
    function logic
    1. first check if the data/value of the new node is smaller or larger the data of the parent node (root node in this case)
    2. if the data is smaller then we check if the left child of the parent node is null(empty) or not
    3. if the left child is null, we create a new node and set the parent.left as new node
    4. if the left child is not empty then we use recursion to call the _insert function again and pass the new parent
    5. if the data is larger than we follow steps 3,4 but for right children
    
    - in simple terms, we first check weather the data is smaller or larger than the parent
    - based on the comparision we run left or right insert logic
    """
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

    # Search functions
    # searching nodes by value

    def search(self, data):
            self._search_node(self.root, data)

    def _search_node(self, node, data, level=0):
        if node is None:
            return
        # search is basically traversal while checking if the current node meets the searched node
        if node.data == data:
            print(f"Node found at level {level}")
            return
        
        level += 1
        self._search_node(node.left, data, level)
        self._search_node(node.right, data, level)


    # Traversal Functions

    def preOrder(self):
        root = self.root
        self._pre_order(node=root)

    def inOrder(self):
        root = self.root
        self._in_order(node=root)

    def postOrder(self):
        root = self.root
        self._post_order(root)

    """
    Pre-order traversal helper function:
    1. Print the current node's data.
    2. Recursively process the left child until there are no more left nodes.
    3. Then recursively process the right child.
    Recursion implicitly uses the call stack to remember where it left off.
    """
    def _pre_order(self, node):
        if node is None:
            return
        print(node.data)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def _in_order(self, node):
        if node is None:
            return
        
        self._in_order(node.left)
        print(node.data)
        self._in_order(node.right)

    def _post_order(self, node):
        if node is None:
            return
        
        self._post_order(node.left)
        self._post_order(node.right)
        print(node.data)
    
    def height(self):
        return self._height(self.root)

    """
    same as pre order with a height variable
    """
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

print("--- Pre Order ---")
tree.preOrder()

print("--- In Order ---")
tree.inOrder()

print("--- Post Order ---")
tree.postOrder()


tree.search(30)