# waitlist_manager.py

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist")

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            print(f"{name} added to the end of the waitlist")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{name} added to the end of the waitlist")

    def remove(self, name):
        if not self.head:
            return f"{name} not found"
        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"
        current = self.head
        while current.next and current.next.name != name:
            current = current.next
        if current.next:
            current.next = current.next.next
            return f"Removed {name} from the waitlist"
        return f"{name} not found"

    def print_list(self):
        if not self.head:
            print("The waitlist is empty")
            return
        print("Current waitlist:")
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    waitlist = LinkedList()
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
        elif choice == "3":
            name = input("Enter customer name to remove: ")
            print(waitlist.remove(name))
        elif choice == "4":
            waitlist.print_list()
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    waitlist_generator()


"""
DESIGN MEMO:

Our waitlist is implemented as a singly linked list, a data structure made up of nodes.
Each Node stores a customer's name and a pointer to the next Node in the list. The
LinkedList class manages these nodes, starting from the 'head', which always points to
the first customer in the waitlist.

The head is crucial because it’s the entry point to the entire list. Without it, we’d
lose access to all customers. Adding to the front simply means creating a new node and
pointing it to the current head, then updating head to the new node. Adding to the end
requires traversing the list until we find the last node, then linking it to the new node.
Removing a customer involves finding the node before the one to remove and adjusting its
pointer to skip over the removed node.

A real engineer might use a custom linked list like this when they need fine-grained
control over memory usage, insertion, and deletion operations — especially in systems
where performance matters and built-in Python lists are too costly for frequent
insertions/removals in the middle. This approach is also useful when modeling queues,
stacks, or other dynamic collections where the size changes constantly and order matters.
"""
