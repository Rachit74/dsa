

class Node:
    data: int
    next: Node

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node
    def __init__(self):
        self.head = None

    # function to insert at the start of the list
    """
    we first check if the list is empty
    if the list is empty than we make the insererted element the head and return the funtion
    if the list is not empty than we make a new node, and set the head of the list as new node next pointer
    then we set the new node as the head of the list
    """
    def insertAtStart(self, data):
        # check if list is empty
        if self.head == None:
            new_node = Node(data=data)
            # set new node as the head
            self.head = new_node
            print("Node has been inserted at the start")
            return new_node
        
        new_node = Node(data=data)
        # set new nodes next pointer to the current head, moving the head to the second position in the list
        new_node.next = self.head
        # set the new node as the new head of the list
        self.head = new_node
        print("Node has been inserted, head updated")
        return new_node
    
    # function to insert at the end of the list
    """
    we first check if the list is empty
    if list is not empty we then traverse to the last node
    we set the last node's next pointer to the new node
    we set new node next pointer to null since it is at the end of the list
    """
    def insertAtEnd(self, data):
        # check if the list is empty
        if self.head == None:
            new_node = Node(data=data)
            self.head = new_node
            print("The list was empty! Element added as head!")
            return
        
        new_node = Node(data=data)
        # traverse the list until we are at last node
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node;
        print("Node inserted at the end of the list!")
        return

    # insert at position function
    """
    handles node insertion at any given position
    does not handle out of bounds!
    we first check if the list is empty
    we then check if the position given is 0 and call insertAtStart function in that case
    we then traverse to the node at pos-1
    we then set the next pointers according to new node, new_node.next = pos-1.next and then pos-1.next to new_node
    """
    def insertAtPosition(self, data, pos):
        # check if the list is empty
        if self.head == None:
            new_node = Node(data=data)
            self.head = new_node
            print("The List was empty! Element added as head!")
            return
        
        # handle position 0
        if pos == 0:
            self.insertAtStart(data=data)
            return
        
        current = self.head
        current_pos = 0
        while current_pos != pos-1:
            current_pos += 1
            current = current.next
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        print(f"Node Inserted at position {pos}")

    # function to traverse the list
    """
    first we check if the list is empty
    if the list is not empty then we set the current pointer to the head of the list
    we print the data of the current node and move current pointer to the nodes next pointer
    we do this until current pointer is not null
    """
    def traverse(self):
        # check if the list is empty
        if (self.head == None):
            print("The list is empty nothing to traverse")
            return
        
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        


list = LinkedList()
list.insertAtStart(10)
list.insertAtStart(15)
list.insertAtEnd(5)
list.insertAtPosition(99, 1)
list.traverse()