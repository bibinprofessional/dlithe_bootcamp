class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        current =self.head
        if current:
            while current.next:
                current=current.next
            current.next=new_node
        else:
            self.head=new_node

    def insert_at_index(self,data,index):
        if index>self.length():
            return
        else:
            new_node=Node(data)
            if index==0:
                new_node.next=self.head
                self.head=new_node
            else:
                count=0
                current=self.head
                while current:
                    count+=1
                    if count==index:
                        new_node.next=current.next
                        current.next=new_node
                        break
                        
                    current=current.next

    def delete_at_beginning(self):
        if self.head:
            self.head=self.head.next
        else:
            return
        
    def delete_at_end(self):
        if self.head:
            if self.head.next:
                current=self.head
                while current.next.next:
                    current=current.next
                current.next=None
            else:
                self.head=None
            
        else:
            return
        

    def delete_at_index(self,index):
        if index>=self.length():
            return
        else:
            if index==0:
                self.head=self.head.next
            else:
                count=0
                current=self.head
                while current:
                    count+=1
                    if count==index:
                        current.next=current.next.next
                        break
                    current=current.next

    def length(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.next
        return count

        
        

    def display(self):
        current=self.head
        while current:
            print(current.data,end=", ")
            current=current.next


l=LinkedList()
l.insert_at_beginning(2)
l.insert_at_beginning(212)
l.insert_at_beginning(1)
l.insert_at_end(12)
l.insert_at_end(144)
l.insert_at_end(22)
l.insert_at_index(25,4)
l.delete_at_beginning()
l.delete_at_beginning()
l.delete_at_end()
l.delete_at_index(2)
l.delete_at_index(0)
print(l.length())



l.display()