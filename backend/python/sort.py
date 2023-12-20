con=['na','bi',3,76,5,1,4.1,5.5,2.1,['a','b',5]]

int_l=[]
float_l=[]
str_l=[]
list_l=[]
for i in con:
    if type(i)==int:
        int_l.append(i)

    elif type(i)==float:
        float_l.append(i)

    elif type(i)==str:
        str_l.append(i)
    
    else:
        list_l.append(i)

int_l.sort()
float_l.sort()
str_l.sort()
list_l.sort()

final_l=int_l+float_l+str_l+list_l

print(final_l)
