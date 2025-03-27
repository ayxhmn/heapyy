class Node:
    """A node in the singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A simple singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, value):
        """Append a value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        """Prepend a value to the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        """Convert linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def remove(self, value):
        """Remove the first occurrence of a value from the list."""
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def find(self, value):
        """Check if a value exists in the list."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
