import json

d={'id':110,'name':'bibin','age':23}
print(d)
print(type(d))

json_d=json.JSONEncoder().encode(d)
print(json_d)
print(type(json_d))
try:
    d1=json.JSONDecoder().decode(json_d)
    print(d1)
    print(type(d1))
except json.JSONDecodeError as e:
    print(e)
