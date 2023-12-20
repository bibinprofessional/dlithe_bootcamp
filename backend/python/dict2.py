def str_sort(d):
    n=len(d)
    for i in range(n):
        for key,value in d.items():
            if(d[key]<d[key+1]):
                d[key],d[key+1]=d[key+1],d[key]


string=input().split(',')
diction={}
for i in string:
    diction[i.split(':')[0].replace(" ","")]=i.split(':')[1].replace(" ","")

print(diction)



a=str_sort(diction)
print(a)
print(dict(a))



