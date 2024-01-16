class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)

print("Front element:", queue.front())

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
print("Queue after dequeue:", queue.items)

print("Is the queue empty?", queue.is_empty())
print("Queue size:", queue.size())
