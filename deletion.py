class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete node by value
    def delete(self, value):
        temp = self.head

        # If list is empty
        if temp is None:
            print("List is empty")
            return

        # If first node is to be deleted
        if temp.data == value:
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

            print("Node deleted:", value)
            return

        # Search for the node
        while temp is not None and temp.data != value:
            temp = temp.next

        # If node is not found
        if temp is None:
            print("Node not found")
            return

        # Connect previous node to next node
        if temp.prev is not None:
            temp.prev.next = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print("Node deleted:", value)

    # Display linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main program
dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

print("Original Doubly Linked List:")
dll.display()

dll.delete(20)

print("After Deletion:")
dll.display()
