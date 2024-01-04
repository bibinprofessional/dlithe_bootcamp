l=[
    {'name':'bibin','age':23},
    {'name':'srujan','age':24},
    {'name':'varsha','age':22},
    {'name':'ziya','age':19},
    {'name':'nikhil','age':25},
    {'name':'shridhar','age':26},
]

sort_l=sorted(l,key=lambda x:x['age'])
print(sort_l)