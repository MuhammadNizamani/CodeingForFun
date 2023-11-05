class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        

if __name__ == "__main__":
    # Create a new linked list
    my_linked_list = LinkedList()

    # Append some data to the linked list
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)

    # Display the linked list
    my_linked_list.display()
