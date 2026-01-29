"""
doubly linked list is a linked with where node have two pointers, one to the previous node and one to the next node
"""

class Node:
    data: int
    previous: Node
    next: Node

    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class LinkedList:
    head: Node

    def __init__(self):
        self.head = None

    # function to check if the list is empty and create a head node
    """
    checks if the list is empty and creates the head node
    """
    def isEmpty(self, data) -> bool:
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            print("The list was empty, added node as head!")
            return True
        return False

    # insert at start
    def insertAtStart(self, data):
        # handle if the list is empty
        if self.isEmpty(data):
            return
        
        new_node = Node(data)

        # set the head's pervious pointer to new node
        self.head.previous = new_node
        
        # set the new node next to head
        new_node.next = self.head

        # set new node as head
        self.head = new_node

        print("Node was added!")

        return
    
    # insert at end
    def insertAtEnd(self, data):
        # handle empty list
        if self.isEmpty(data):
            return
        
        new_node = Node(data)

        # traverse to the end node
        current = self.head
        while not current.next == None:
            current = current.next

        # set the last node's next pointer to the new node
        current.next = new_node
        # set the new nodes previous pointer to the last node
        new_node.previous = current

        return
    
    # insert at position
    # Not handling out of bounds right now
    def insertAtPosition(self, data, pos):
        # check if the position is out of bounds
        bound = self.calculate_len()

        if pos > bound:
            print("Insert position is out of bounds")
            return

        # handle empty list
        if self.isEmpty(data):
            return
        
        # handle if the position is 0
        if pos == 0:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            return
        
        # traverse to the position in the list
        current = self.head
        current_pos = 0
        while current_pos != pos -1:
            current = current.next
            current_pos += 1
        
        new_node = Node(data)

        # the current nodes next node before insertion
        current_next = current.next

        # handle if the insert is at last pos
        if current_next is None:
            new_node.next = None
            new_node.previous = current
            current.next = new_node
            return

        # set the current_next previous to new node
        current_next.previous = new_node
        # set the current node next to new node
        current.next = new_node
        # set the new node previous to current and next to current_next
        new_node.previous = current
        new_node.next = current_next

        print(f"Node has been inserted at position {pos}")
        
    
    def traverse(self):
        # check if list is empty
        # we will not call isEmpty function here because we don't need to create a node
        if self.head == None:
            print("The List is empty, nothing to traverse!")
            return
        
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

        return
    
    # function to calculate the length of the list
    def calculate_len(self):
        len_ = 0
        current = self.head

        while current is not None:
            current = current.next
            len_ += 1

        return len_

list = LinkedList()

list.insertAtStart(10)
list.insertAtEnd(55)
list.insertAtStart(15)
list.insertAtPosition(99, 2)
list.insertAtPosition(99, 99)
list.traverse()