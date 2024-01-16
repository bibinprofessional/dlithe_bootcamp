class Node :
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def create_root(self,data):
        if self.root:
            return
        else:
            self.root=Node(data)

    def insert(self,data):
        self._insert(data,self.root)
        
    def _insert(self,data,root):
        if data<root.data:
            if root.left:
                self._insert(data,root.left)
            else:
                root.left=Node(data)
        else:
            if root.right:
                self._insert(data,root.right)
            else:
                root.right=Node(data)
    
    def search(self,data):
        res=self._search(data,self.root)
        if res:
            print(f'{data} is present')
        else:
            print(f'{data} is not present')
    
    def _search(self,data,root):
        if data==root.data:
            return True
        
        if data<root.data:
            if root.left:
                return self._search(data,root.left)
            else:
                return False
        
        else:
            if root.right:
                return self._search(data,root.right)
            else:
                return False
        

    def display(self):
        self._display(self.root)

    def _display(self,root):
        if root.left:
            self._display(root.left)

        print(root.data,end=', ')

        if root.right:
            self._display(root.right)




t=Tree()
t.create_root(25)
t.insert(29)
t.insert(10)
t.insert(16)
t.insert(15)
t.insert(1)
t.insert(16)
t.insert(15)
t.search(10)
t.search(1)
t.search(2)
t.search(26)
t.display()