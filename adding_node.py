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

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        # Traverse to the last node
        while temp.next is not None:
            temp = temp.next

        # Connect new node
        temp.next = new_node
        new_node.prev = temp

    # Display the linked list
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

print("Doubly Linked List:")
dll.display()
