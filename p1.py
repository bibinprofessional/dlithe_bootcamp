# remove special characters from the input string

string=input()
for i in string:
    if not i.isalnum() and i!=' ':
        string=string.replace(i,'')
print(string)