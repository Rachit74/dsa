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
    ll.insert_at_start(1)
    ll.insert_at_start(2)
    ll.insert_at_start(3)
    ll.insert_at_start(10)
    ll.insert_in_middle(50, 2)

    ll.display()   # Output: 1 -> 2 -> 3 -> None
