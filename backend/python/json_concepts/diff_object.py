import json

# my_list = [1, 2, 3, 4, 5]
# json_string = json.dumps(my_list, indent=4)

# print(json_string)


# my_set = {"a", "b", "c"}
# json_data = json.dumps(list(my_set),indent=2)

# print(json_data)




my_dict = {

    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "area":float('nan')
}

json_data1 = json.dumps(my_dict,indent=4,allow_nan=True,sort_keys=True,separators=(".","=>"))

print(json_data1)