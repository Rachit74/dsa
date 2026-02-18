package main

import (
	"fmt"
)

// node struct
type Node struct {
	Value int
	Next  *Node
}

// linked list struct
type LinkedList struct {
	Head *Node
	Size int
}

// add element at last
func (l *LinkedList) Append(val int) {
	new_node := &Node{Value: val}

	// check if the list is empty
	if l.Head == nil {
		l.Head = new_node
	} else {
		current := l.Head
		for current.Next != nil {
			current = current.Next
		}
		current.Next = new_node
	}

	l.Size++
}

// add element at start
func (l *LinkedList) Prepend(val int) {
	new_node := &Node{Value: val}

	// check if list is empty
	if l.Head == nil {
		l.Head = new_node
	} else {
		new_node.Next = l.Head
		l.Head = new_node
	}
	l.Size++
}

// print list
func (l *LinkedList) print() {
	// check if list is empty
	if l.Head == nil {
		fmt.Println("Empty List")
	} else {
		current := l.Head
		for current != nil {
			fmt.Println(current.Value)
			current = current.Next
		}
	}

}

func main() {
	list := &LinkedList{}

	list.Append(50)
	list.Prepend(100)
	list.print()
}
