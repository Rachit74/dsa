#include <iostream>

// comments are fixes required

class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = nullptr;
        right = nullptr;
        std::cout << "Node Created with data " << data << "\n";
    }

    // will cause segmentation fault if a node only has one child 
    void getChildren() {
        std::cout << "Children for Node with data " << data << " are: \n";
        std::cout << "Left Child " << left->data << "\n" << "Right Child " << right->data << "\n";
    }
};

class BinaryTree {
public:
    Node* root;

    BinaryTree() {
        root = nullptr;
    }
};


int main() {
    std::cout << "Binary Tree Module" << std::endl;

    Node* rootNode = new Node(10);

    BinaryTree tree;

    tree.root = rootNode;
    tree.root->left = new Node(20);
    tree.root->right = new Node(5);


    tree.root->getChildren();

    rootNode->left->left = new Node(100);
    rootNode->left->right = new Node(100);


    rootNode->left->getChildren();


    return 0;
}