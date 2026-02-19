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

func (l *LinkedList) InsertAtPosition(val int, pos int) {
	// check out of bounds
	if pos < 0 || pos > l.Size {
		fmt.Println("Position out of index")
		return
	}

	if pos == 0 {
		l.Prepend(val)
		return
	}

	if pos == l.Size {
		l.Append(val)
		return
	}

	// insert in the middle
	newNode := &Node{Value: val}
	current := l.Head

	for i := 0; i < pos-1; i++ {
		current = current.Next
	}

	newNode.Next = current.Next
	current.Next = newNode

	l.Size++
}

func (l *LinkedList) Search(val int) int {
	if l.Head == nil {
		fmt.Println("Empty list, nothing to search")
		return -1
	}

	current := l.Head
	for i := 0; i < l.Size; i++ {
		if current.Value == val {
			fmt.Println("Target found at index:", i)
			return i
		}
		current = current.Next
	}

	fmt.Println("Target not found in the list")
	return -1
}

func (l *LinkedList) Delete(val int) {
	if l.Head == nil {
		fmt.Println("List is empty, nothing to delete")
		return
	}

	targetIndex := l.Search(val)
	if targetIndex == -1 {
		fmt.Println("Value not found, cannot delete")
		return
	}

	if targetIndex == 0 {
		l.Head = l.Head.Next
		l.Size--
		fmt.Println("Deleted value at head")
		return
	}

	current := l.Head
	for i := 0; i < targetIndex-1; i++ {
		current = current.Next
	}

	// skip over the target node
	current.Next = current.Next.Next
	l.Size--
	fmt.Println("Deleted value at index:", targetIndex)
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

	list.Append(10)
	list.Append(20)
	list.Append(30)
	list.Append(40)
	list.InsertAtPosition(25, 3)
	list.print()
	list.Search(30)
	list.Delete(30)
	list.print()
}
