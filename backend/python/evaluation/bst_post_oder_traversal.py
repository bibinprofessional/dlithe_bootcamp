class Node :
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def traversal(head):
    stack=[head]
    l=[]
    while stack:
        current = stack.pop()
        l.insert(0, current.data)

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    return l  



head = Node(100)
head.left = Node(200)
head.right = Node(300)
head.left.left = Node(400)
head.left.right = Node(500)

print(traversal(head))