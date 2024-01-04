# reverse the string words 

string=input()
l=list(string.split())

rev=''
for i in l[::-1]:
    rev+=i+' '

print(rev)