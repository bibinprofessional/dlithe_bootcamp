import re
string='1235Hello Hi 567'
format=re.compile(r'\d+')

res=re.match(format,string)
print()
print(res)
print(res.group())

res2=re.search(format,string)
print()
print(res2)
print(res2.group())

res2=re.sub(format,'****',string)
print()
print(res2)
