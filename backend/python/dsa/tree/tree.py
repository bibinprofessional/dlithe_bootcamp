class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def add(self,data):
        print(self.data)
        if data==self.data:
            return
        
        if data<self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left=Node(data)
        
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right=Node(data)

    def traversal_ascending(self):

        if self.left:
            self.left.traversal_ascending()
    
        print(self.data,end=' ')
        
        if self.right:
            self.right.traversal_ascending()

    def traversal_descending(self):
    
        if self.right:
            self.right.traversal_descending()

        print(self.data, end=' ')

        if self.left:
            self.left.traversal_descending()
        



n=Node(20)
print()
n.add(25)
print()
n.add(29)
print()
n.add(10)
print()
n.add(16)
print()
n.add(26)
print()
n.add(5)
print()
n.add(24)
print()
n.add(21)
print()
n.add(8)
print()
n.add(23)
print()
n.add(21)
print()
n.add(90)
print()
n.add(7)
print()


n.traversal_ascending()
print()
n.traversal_descending()
        