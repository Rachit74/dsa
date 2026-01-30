package java_.BinaryTree;

// create Node class
class Node {
    int data;
    Node left = null;
    Node right = null;

    Node(int data) {
        this.data = data;
    }

}

// BinaryTree class
class BinaryTree {
    Node root;

    // constructor which sets root to null
    BinaryTree() {
        root = null;
    }

    // insert Record private function
    private void insertRecord(int data, Node parentNode) {
        // check if the data is smaller than the parent
        if (data < parentNode.data) {
            // check if the left child of parent node is null
            if (parentNode.left == null) {
                // set the new node as the parent node left child
                parentNode.left = new Node(data);
                return;
            }
            // call the function again if the node is not empty
            this.insertRecord(data, parentNode.left);
            return;
        }

        // check if the data is larger than the parent
        if (data > parentNode.data) {
            // check if the right child is null
            if (parentNode.right == null) {
                // set new node as the right child
                parentNode.right = new Node(data);
                return;
            }
            // call the function recursively if the child is not empty
            this.insertRecord(data, parentNode.right);
        }

    }


    // public function to add a node
    public void insert(int data) {
        // check if the tree is empty
        if (this.root == null) {
            // create a new node and set it as root
            this.root = new Node(data);
            return;
        }

        // if the tree is not empty, call the private insertRecord function and pass the root node as the parentNode
        this.insertRecord(data, this.root);
    }

}

public class main {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        tree.insert(50);
        tree.insert(45);
        tree.insert(55);
        tree.insert(66);
        tree.insert(30);
        System.out.println("Tree Successfull created!");
    }
}
