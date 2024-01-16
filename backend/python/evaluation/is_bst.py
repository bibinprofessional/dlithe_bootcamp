class Node :
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def is_bst(node):
    prev = None

    while node:
        if not node.left:
            if prev is not None and node.data <= prev.data:
                return False
            prev = node

            node = node.right
        else:
            current = node.left
            while current.right and current.right != node:
                current = current.right

            if not current.right:
                current.right = node
                node = node.left
            else:

                current.right = None
                if prev is not None and node.data <= prev.data:
                    return False
                prev = node

                node = node.right

    return True

        

head = Node(100)
head.left = Node(200)
head.right = Node(300)

print(is_bst(head))