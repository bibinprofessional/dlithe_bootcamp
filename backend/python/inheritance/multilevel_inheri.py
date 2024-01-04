class A:
    def given_A(self):
        print('First level super class properties given')
    
class B(A):
    def given_B(self):
        print('Second level super class properties given')

class C(B):
    def recieve(self):
        print('Both class properties recieved')

c=C()
c.given_A()
c.given_B()
c.recieve()