class Node:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    """Doubly Linked List (DLL) implementation."""
    def __init__(self):
        self.head = None  # Head (first node) of the list
        self.tail = None  # Tail (last node) of the list
        self.size = 0     # Size of the linked list

    def append(self, data):
        """Add a node to the end of the linked list."""
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """Add a node to the beginning of the linked list."""
        new_node = Node(data)
        if not self.head:  # If list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def delete(self, data):
        """Delete the first occurrence of a node with given data."""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # If deleting head
                    self.head = current.next
                if current == self.tail:  # If deleting tail
                    self.tail = current.prev
                self.size -= 1
                return True  # Data found and deleted
            current = current.next
        return False  # Data not found

    def search(self, data):
        """Search for a node with given data. Returns True if found, else False."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        """Reverse the doubly linked list in place."""
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next  # Swap next and prev
            current = current.prev  # Move to next node (previous node due to swap)
        self.head, self.tail = self.tail, self.head  # Swap head and tail