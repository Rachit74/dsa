#include <iostream>
using namespace std;

struct Node{
    int data;
    Node *next;

    Node(int value) {
        data = value;
        next = nullptr;
    }
};

class LinkedList{
    private:
    Node *head;

    public:

    LinkedList(){
        head = nullptr;
    }

    // Insert at the head
    void insertAtHead(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }

    // Insert at tail
    void insertAtTail(int data) {
        Node *newNode = new Node(data);
        // if the list is empty
        if (head == nullptr) {
            head = newNode;
        }

        Node *current = head;
        while (current->next != nullptr)
        {
            current = current->next;
        }

        current->next = newNode;
        
        
    }

    // display
    void display() {
        Node *current = head;
        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next;
        }
    }

};

int main() {
    LinkedList list;
    list.insertAtHead(10);
    list.insertAtTail(20);
    list.display();
}