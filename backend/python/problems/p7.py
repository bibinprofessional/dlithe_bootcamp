# 2 lists. 2nd list values need to inserted into 1st list

# l1=[1,2,3,4,5,6]
# l2=[3,4,5,6,3,54,3,23,6,5]

l1=[1,2,3,4,5,6]
l2=[3,4,5,6]

dif=len(l2)-len(l1)
new_l=[]
if dif>-1:
    for i in range((2*len(l1))-1):
        if i%2==0:
            new_l.append(l1[i//2])
        else:
            new_l.append(l2[i//2])
    
    new_l.extend(l2[len(l1)-1:])
    print(new_l)

else:
    for i in range((2*len(l2))):
        if i%2==0:
            new_l.append(l1[i//2])
        else:
            new_l.append(l2[i//2])
    
    new_l.extend(l1[len(l2):])
    print(new_l)