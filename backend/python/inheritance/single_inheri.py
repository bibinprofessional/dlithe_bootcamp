class A:
    def given(self):
        print('properties are given')

class B(A):
    def recieve(self):
        print('properties recieved')


c=B()
c.given()
c.recieve()