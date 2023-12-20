def sort1(item):

    order = {int: 0,float: 1,str: 2,list: 3}
    
    a=order.get(type(item))
    return a, item


con = [5.2,'na', 'bi', [9, 8, 5], 3,['bi','in'], 76,[2,5], 5, 1, 4.1, 5.5, 2.1]
con.sort(key=sort1)

print(con)