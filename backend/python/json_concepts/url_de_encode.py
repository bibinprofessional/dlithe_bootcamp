import requests
import json
req=requests.get("https://gbfs.citibikenyc.com/gbfs/2.3/gbfs.json")
print(req.__dict__)
data=req.json()
print(data)
json_d=json.dumps(data,indent=4)
print(json_d)