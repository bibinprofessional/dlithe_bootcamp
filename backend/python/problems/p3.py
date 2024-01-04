# capitalize first character of in each sentence ans add it to dictionary

sentence=input()
l=list(sentence.split('.'))
d={}
for i in range(len(l)):
    d[i]=l[i].strip().capitalize()

print(d)