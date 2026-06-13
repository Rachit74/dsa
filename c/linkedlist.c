// implementation of linked list in c

#include <stdio.h>
#include <stdlib.h>

// Node struct

struct Node {
    int data;
    struct Node *next;
};

// Linked List Struct

struct LinkedList {
    int length;
    struct Node *head;
};

struct Node *createNode(int data) {
    struct Node *newNode = malloc(sizeof(struct Node));

    if (newNode == NULL) {
        return NULL;
    }

    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

struct LinkedList *createList() {
    struct LinkedList *list = malloc(sizeof(struct LinkedList));

    if (list == NULL) {
        return NULL;
    }

    list->length = 0;
    list->head = NULL;
    return list;
}

void appendAtStart(struct LinkedList *list, struct Node *node) {
    // check if the list is empty
    if (list->length == 0) {
        list->head = node;
        list->length++;
        printf("Node Appended!\n");
        return;
    }

    // if list is not empty
    node->next = list->head;
    list->head = node;
    list->length++;
    printf("Node Appended!\n");
    return;
}

void appendAtEnd(struct LinkedList *list, struct Node *node) {
    // if the list is empty
    if (list->length == 0) {
        appendAtStart(list, node);
        return;
    }

    // if list is not empty
    // traverse the list
    struct Node *current = list->head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = node;
    list->length++;
    printf("Node Appended!\n");
    return;
}

void insertAtPosition(struct LinkedList *list, struct Node *node, int pos) {
    // check out of bounds
    if (pos < 0 || pos > list->length) {
        printf("Position out of bounds\n");
        return;
    }

    // if pos 0 
    if (pos == 0) {
        appendAtStart(list, node);
        return;
    }

    // append at end if pos == len
    if (pos == list->length) {
        appendAtEnd(list, node);
        return;
    }

    // append at position if the list is not empty
    struct Node *current = list->head;
    int index = 0;
    while (index != pos - 1) {
        current = current->next;
        index++;
    }
    node->next = current->next;
    current->next = node;
    list->length++;
    printf("Node Appended\n");
    return;
}

void printlist(struct LinkedList *list) {
    // traverse and print the elements
    struct Node *current = list->head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
    return;
}

int main() {
    struct LinkedList *list = createList();
    struct Node *node = createNode(5);
    struct Node *node2 = createNode(10);
    struct Node *node3 = createNode(15);
    struct Node *node4 = createNode(20);
    struct Node *node5 = createNode(25);

    appendAtStart(list, node);
    appendAtStart(list, node2);
    appendAtEnd(list, node3);
    appendAtEnd(list, node4);
    insertAtPosition(list, node5, 20);

    printf("%d\n", list->length);
    printlist(list);

    return 0;

}