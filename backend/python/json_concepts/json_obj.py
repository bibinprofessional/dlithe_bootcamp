
import json

json_string='{ "id": 101, "name": "bibin", "age":23}'
print(json_string)
print(type(json_string))
d=json.loads(json_string)
print(d)   
print(type(d))

print()
print()
json_string2='[102,"asd",21]'
print(json_string2)
print(type(json_string2))
d2=json.loads(json_string2)
print(d2)  
print(type(d2))  

print()
print()
json_string3='[102,"asd",21]'
print(json_string3)
print(type(json_string3))
d3=tuple(json.loads(json_string3))
print(d3)  
print(type(d3))  

print()
print()
print(json_string)
print(type(json_string))
d4=json.loads(json_string)
d4=tuple(d4.items())
print(d4)  
print(type(d4))  