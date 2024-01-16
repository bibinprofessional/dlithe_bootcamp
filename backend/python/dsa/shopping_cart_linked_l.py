class Node:
    def __init__(self,item,quantity):
        self.item=item
        self.quantity=quantity
        self.next=None

class Cart:
    def __init__(self):
        self.head=None

    def add_item(self,item,quantity=1):
        new_node=Node(item,quantity)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
        else:
            self.head=new_node
        
        print(f'{item} added to cart')

    def remove_item(self,item):
        if self.head:
            current=self.head
            while current.next:
                if item==current.item:
                    prev.next=current.next
                    print(f'{item} deleted from cart')
                    break
                prev=current
                current=current.next
            else:
                print(f'{item} not in cart')
        else:
            return
        
    def remove_all(self):
        self.head=None
        print('All items removed from cart')


    def display_cart(self):
        current=self.head
        while current:
            print(f'({current.item},{current.quantity})',end=", ")
            current=current.next




c=Cart()
c.add_item('phone',quantity=2)
c.add_item('laptop',quantity=4)
c.add_item('tv')
c.add_item('mouse',quantity=4)
c.remove_item('laptop')
c.remove_all()



c.display_cart()
