# key search value extract, value search key extract

d={23:'bibin',44:'fasf',54:'GDS',26:'dssfg',32:'bibin'}

for k,v in d.items():
    if k==54:
        print(v)
        break
else:
    print('key not found')


for k1,v1 in d.items():
    if v1=='bibin':
        print(k1)

