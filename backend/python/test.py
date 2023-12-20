string=input()
for i in string:
    if not i.isalnum():
        string=string.replace(i,'')
print(string)