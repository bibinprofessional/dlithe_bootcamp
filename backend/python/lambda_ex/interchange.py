d={'name':"bibin",'age':'12'}

changed_d=dict(map(lambda x:(x[1],x[0]),d.items()))
print(changed_d)