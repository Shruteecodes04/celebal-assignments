class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to manage a singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print the linked list."""
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node in the list (1-based index)."""
        try:
            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise ValueError("Index must be a positive integer.")

            if n == 1:
                print(f"Deleting node {n}: {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            prev = None
            count = 1

            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if not current:
                raise IndexError(f"Index {n} is out of range.")

            print(f"Deleting node {n}: {current.data}")
            prev.next = current.next

        except (IndexError, ValueError) as e:
            print(f"Error: {e}")


# Sample Test
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Original list:")
    ll.print_list()

    print("\nDelete 2nd node:")
    ll.delete_nth_node(2)
    ll.print_list()

    print("\nDelete 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTry to delete 5th node (out of range):")
    ll.delete_nth_node(5)

    print("\nDelete remaining nodes:")
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTry to delete from empty list:")
    ll.delete_nth_node(1)
