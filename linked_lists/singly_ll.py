# ---------------------------------------
# Singly Linked List Implementation in Python
# ---------------------------------------

class Node:
    """
    A single node of a linked list.
    Holds the data and a reference (pointer) to the next node.
    """
    def __init__(self, data):
        self.data = data       # The actual value stored in this node
        self.next = None       # Pointer to the next node (None if it's the last node)


class LinkedList:
    """
    A simple singly linked list.
    Each node points to the next, starting from the head node.
    """
    def __init__(self):
        self.head = None   # Initially the list is empty, so head is None

    """
    Append Functions
    1. insert at tail
    2. insert at head
    3. insert at position
    """

    def insert_at_tail(self, data):
        """
        Add a new node containing 'data' at the end of the linked list.
        """
        new_node = Node(data)

        # Case 1: If the list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Case 2: Traverse to the last node
        last_node = self.head
        while last_node.next is not None:   # Keep moving until .next is None
            last_node = last_node.next

        # Now last_node is the actual last node, link it to the new node
        last_node.next = new_node

    def insert_at_start(self, data):
        """
        Add a new node contaning data at the start of the linked list
        """
        new_node = Node(data)

        #Case 1: check if the list is empty, 
        if self.head is None:
            self.head = new_node
            return
        
        #Case 2: set the new_node.next to head and then make new_nod the head
        new_node.next = self.head
        self.head = new_node

    def insert_in_middle(self, data, pos):
        root_node = self.head
        """
        Add a new Node contaning data at the middle of the linked list based on the given position
        """
        new_node = Node(data)

        # Case 1: list is empty
        if self.head is None:
            if pos == 0:
                self.head = new_node
            else:
                print("Position Out of bounds")
            return
        
        # Case 2: insert at the head
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Traverse to the pos-1 node
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1

        if not current:
            print("Out of bounds")

        new_node.next = current.next
        current.next = new_node


    """
    Pop functions
    1. delete_at_tail
    2. delete_at_head
    3. delete_at_position
    """

    def delete_at_tail(self):
        """
        if the list is empty do nothing
        traverse to the last node, set prev to current - 1, set prev.next = None to remove the pointer to the last node
        check for if the list has only one node
        """
        # check if list is empty
        if self.head is None:
            print("List is empty, No elements to delete")
            return

        # if the list has only one node
        if self.head.next == None:
            self.head = None
            return

        #Traverse and delete the last node
        current = self.head
        prev = None
        while current.next != None:
            prev = current
            current = current.next

        prev.next = None

    def delete_at_head(self):
        """
        check if the list is empty do nothing
        set self.head = self.head.next, and self.head = None
        check for if the list has only one node
        """

        # check if the list is empty
        if self.head is None:
            print("List is empty, No elements to delete")
            return

        #check if there is only one node in the list
        if self.head.next == None:
            self.head = None
            return
        
        # move head to the next node
        self.head = self.head.next

    def delete_at_position(self, pos):
        """
       
        """
        if self.head is None:
            print("The list is empty")
            return

        # deleting at head
        if pos == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0

        # move to the node just before the target position
        while current is not None and count < pos - 1:
            current = current.next
            count += 1

        # unlink the node at pos
        current.next = current.next.next

        



    # Display Function

    def display(self):
        """
        Print the linked list in a readable format.
        """
        current = self.head

        while current is not None:
            print(f"{current.data} -> ", end="")
            current = current.next

        print("None")   # Indicates the end of the list


# ---------------------------------------
# Example usage
# ---------------------------------------
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(4)
    ll.insert_at_tail(5)
    ll.insert_at_start(10)
    ll.insert_in_middle(50, 2)

    ll.display()

    ll.delete_at_tail()
    ll.delete_at_head()
    ll.delete_at_position(3)



    ll.display()
