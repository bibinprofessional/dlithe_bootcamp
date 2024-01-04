class A:
    def given_A(self):
        print('First super class properties given')
    
class B:
    def given_B(self):
        print('Second super class properties given')

class C(A,B):
    def recieve(self):
        print('Both class properties recieved')

c=C()
c.given_A()
c.given_B()
c.recieve()