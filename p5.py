# Nested list value matching and deleting, create all the values as only one single list out of it.

l=[[1,3,4,5],[4,45,2,5,1],[5,6,32,3],[32,34,3,7,8],[3,5,4,33,4]]

l=sum(l,[])
print(l)

rep_l,nrep_l=set(),[]
for i in l:

    if l.count(i)>1:
        rep_l.add(i)
    else:
        nrep_l.append(i)

print([list(rep_l),nrep_l])