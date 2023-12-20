d={"m":1,"i":4,"s":4,"P":2}
for key,value in d.items():
    if(d[key]<d[key+1]):
        d[key],d[key+1]=d[key+1],d[key]
    