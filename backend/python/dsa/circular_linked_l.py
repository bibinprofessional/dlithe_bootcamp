import pandas as pd
import os

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.current=None

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head:
            cur=self.head.prev
            cur.next=new_node
            new_node.prev=cur
            new_node.next=self.head
            self.head.prev=new_node
        else:
            self.head=new_node
            new_node.next = self.head
            new_node.prev = self.head
            self.current=self.head
            


    def display(self):
        if self.head:
            cur=self.head
            while True:
                print(cur.data,end=", ")
                cur=cur.next
                if cur==self.head:
                    break
        else:
            return
        
    def display_operation(self,oper):
        if not self.head:
            return False
        if oper=='n':
            self.current=self.display_next(self.current)
            return self.current.data
        elif oper=='p':
            self.current=self.display_prev(self.current)
            return self.current.data
        else:
            return False


    def display_next(self,cur):
        return cur.next
        
    
    def display_prev(self,cur):
        return cur.prev


l=LinkedList()
l.insert_at_end('demo1')
l.insert_at_end('demo2')
l.insert_at_end('demo3')


df=pd.read_csv('dsa/demo_files/demo1.csv',encoding='unicode_escape')

while True:
    os.system('cls')
    print(df)
    opt=input('n => next\np => previous\npress : ')
    file=l.display_operation(opt)
    if file:
        df=pd.read_csv(f'dsa/demo_files/{file}.csv',encoding='unicode_escape')