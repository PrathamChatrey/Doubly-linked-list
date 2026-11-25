# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
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

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete node
    def delete(self, data):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp and temp.data != data:
            temp = temp.next

        if temp is None:
            print("Node not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print(data, "deleted successfully")

    # Display forward
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        print("Doubly Linked List:", end=" ")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Display backward
    def display_reverse(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        print("Reverse List:", end=" ")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Main program
dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

dll.display()

dll.delete(20)

dll.display()

dll.display_reverse()
