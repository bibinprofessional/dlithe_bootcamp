class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_end(self,data):
        new_node=Node(data)
        current =self.head
        if current:
            while current.next:
                current=current.next
            current.next=new_node
        else:
            self.head=new_node

def check_palindrome(l):
    l.head.prev=None
    current=l.head
    count=1
    while current.next:
        count+=1
        prev=current
        current=current.next
        current.prev=prev

    itr=1
    first=l.head
    last=current
    
    while itr<=count//2:
        if first.data!=last.data:
            print('Not a palindrome')
            break
        first=first.next
        last=last.prev
        itr+=1
    else:
        print('Is a palindrome')




l=LinkedList()
l.insert_at_end(10)
l.insert_at_end(10)
l.insert_at_end(12)
l.insert_at_end(1)
l.insert_at_end(12)
l.insert_at_end(1)
l.insert_at_end(10)
check_palindrome(l)

l2=LinkedList()
l2.insert_at_end(10)
l2.insert_at_end(13)
l2.insert_at_end(12)
l2.insert_at_end(1)
l2.insert_at_end(12)
l2.insert_at_end(13)
l2.insert_at_end(10)
check_palindrome(l2)