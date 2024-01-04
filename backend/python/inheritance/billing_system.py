class product:
    def __init__(self):
        self.productdata=[
            {'id':1,'name':'bag','price':650,'count':12},
            {'id':2,'name':'mobile','price':20000,'count':21},
            {'id':3,'name':'watch','price':5500,'count':3},
            {'id':4,'name':'laptop','price':85000,'count':8}
        ]

    def check_avail(self):
        for i in self.productdata:


    def display_products(self):
        for i in self.productdata:
            print(f"name: {i['name']}  price:{i['price']}  count:{i['count']}")

class biller_1(product):
    
    def billing(self,u_p):
        for i in u_p:
            self.check_avail()
            



class biller_2(product):
    pass


class biller_3(product):
    pass


class biller_4(product):
    pass

user_product=[]
c=product()

while True:
    print('Available products are :')
    print()
    c.display_products()
    print()
    prod=input('enter products name with count :  ').replace(" ","")
    
    for i in prod.split(","):
        user_product.append(i.split(":"))

    biller_no=input('enter the biller no :')
    if biller_no==1:
        b=biller_1()
        b.billing(user_product)

    elif biller_no==2:
        b=biller_1()
        b.billing(user_product)

    elif biller_no==3:
        b=biller_1()
        b.billing(user_product)

    elif biller_no==4:
        b=biller_1()
        b.billing(user_product)

    else:
        print('invalid biller no')

