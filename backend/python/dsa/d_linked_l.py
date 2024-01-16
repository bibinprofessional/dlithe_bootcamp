class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def add_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return True  # Node deleted
            current = current.next
        return False  # Node not found

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


dll = DoublyLinkedList()
dll.display()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  

dll.add_at_start(0)
dll.display()  

dll.delete(2)
dll.display() 