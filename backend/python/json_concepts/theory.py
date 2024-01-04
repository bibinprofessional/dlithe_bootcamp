import json
# why json?
#     light weight and faster interchange
#     easy to understand and readability
#     handles hierarchical and unstructured data
    

# where is json used?
#     read and transfer data between client and server
#     api's and web services

# how json is used?
#     client sent request to server for data and data can be passed to client as html but rendering a new html page for every request makes the website slow. In that case if we use json object, data can be sent in no time.


# coverting json to dictionary
# json_string='{ "id": 101, "name": "bibin", "age":23}'
# d=json.loads(json_string)
# print(d)
# print(d['name'])

with open('json_concepts/data.json') as data:
    d2=json.load(data)

    print(d2)
    print(d2['company1'][1]['name'])


# converting dictionary to json
student_details ={ 
    "name" : "ajith", 
    "rollno" : 56, 
    "phonenumber" : "9976770500"
} 

# json_object = json.dumps(student_details, indent = 4) 
# print(json_object)

with open("json_concepts/sample.json", "w") as outfile: 
    json.dump(student_details, outfile)
