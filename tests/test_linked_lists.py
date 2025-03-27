import sys
import os
# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from heapyy import LinkedList, DoublyLinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def test_operations(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(ll.to_list(), [10, 20, 30])

        ll.prepend(5)
        self.assertEqual(ll.to_list(), [5, 10, 20, 30])

        ll.remove(20)
        self.assertEqual(ll.to_list(), [5, 10, 30])

        self.assertTrue(ll.find(10))
        self.assertFalse(ll.find(100))


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        """Initialize a new DLL before each test."""
        self.dll = DoublyLinkedList()

    def test_append(self):
        """Test appending elements to the DLL."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertEqual(self.dll.to_list(), [1, 2, 3])

    def test_prepend(self):
        """Test prepending elements to the DLL."""
        self.dll.prepend(3)
        self.dll.prepend(2)
        self.dll.prepend(1)
        self.assertEqual(self.dll.to_list(), [1, 2, 3])

    def test_delete(self):
        """Test deleting elements from the DLL."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.assertTrue(self.dll.delete(2))
        self.assertEqual(self.dll.to_list(), [1, 3])
        self.assertFalse(self.dll.delete(4))  # Element not in list

    def test_search(self):
        """Test searching elements in the DLL."""
        self.dll.append(10)
        self.dll.append(20)
        self.dll.append(30)
        self.assertTrue(self.dll.search(20))
        self.assertFalse(self.dll.search(40))

    def test_reverse(self):
        """Test reversing the DLL."""
        self.dll.append(1)
        self.dll.append(2)
        self.dll.append(3)
        self.dll.reverse()
        self.assertEqual(self.dll.to_list(), [3, 2, 1])

if __name__ == "__main__":
    unittest.main()
