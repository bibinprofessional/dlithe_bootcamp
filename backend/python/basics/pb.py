n=int(input('N = '))
l=int(input('Leaves = '))
f=list(input().split(','))
f=[int(i) for i in f]
a=set()

while True:
    if min(f)>l:
        break

    else:
        for i in range(len(f)):
            if f[i]<l:
                a.add(f[i])
                f[i]+=f[i]
                  

print(a)