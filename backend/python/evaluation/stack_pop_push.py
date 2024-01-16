class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")



stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.items)

stack.pop()
print(stack.items)
