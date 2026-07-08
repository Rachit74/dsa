#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *left, *right;
};

struct binary_tree
{
    struct Node *root;
};

struct Node *create_node(int data) {
    struct Node *new_node = malloc(sizeof(struct Node));
    if (new_node == NULL) {
        return NULL;
    }

    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    
    return new_node;
}

struct binary_tree *create_tree() {
    struct binary_tree *new_tree = malloc(sizeof(struct binary_tree));
    if (new_tree == NULL) {
        return NULL;
    }

    new_tree->root = NULL;

    return new_tree;
}

void insert(struct binary_tree *tree, struct Node *node) {
    // if the tree is empty then make the node root node
    if (tree->root == NULL) {
        tree->root = node;
        return;
    }
}