import json

# with open('json_concepts/data.json') as data:
#     d=json.load(data)

#     print(d)
#     print(d['company1'][1]['name'])

# print()

company_details ={ 
    "company3":[
        {
            'id':105,
            'name':'srujan',
            'age':25
        },
        {
            'id':106,
            'name':'nikhil',
            'age':22
        }
    ]
} 

# with open("json_concepts/sample.json", "w") as file: s
#     json.dump(company_details, file,indent=4)

with open("json_concepts/data.json", "r+") as file1: 
    d2=json.load(file1)
    d2.update(company_details)
    file1.seek(0)
    json.dump(d2, file1,indent=4)


