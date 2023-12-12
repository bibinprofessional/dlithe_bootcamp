from flask import Flask, jsonify, request

app = Flask(__name__)

data=[
    {'id':1,'name':'bibin','phone':'9873244324'},
{'id':2,'name':'nikhil','phone':'9873277324'},
{'id':3,'name':'shidhar','phone':'9873204324'},
{'id':4,'name':'srujan','phone':'9873004324'},
{'id':5,'name':'varsha','phone':'9870244324'},
{'id':6,'name':'ziya','phone':'98732443324'}
]

@app.route('/all_users',methods=['GET'])
def get_all_user():
    return jsonify({'users':data})

def find_user(user_id):

    return next((user for user in data if user['id']==user_id),None)

@app.route('/get_user/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user=find_user(user_id)
    if user:
        return jsonify({'user':user})
    else:
        return jsonify({'message':'user not found'}),404


@app.route('/add_user',methods=['POST'])
def add_user():
    user=request.get_json()
    new_user={'id':len(data)+1,'name':user['name'],'phone':user['phone']}
    data.append(new_user)
    return jsonify({'message':'user created','new_user':new_user}), 201


@app.route('/update_user/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if user:
        user_data=request.get_json()
        user['name']=user_data['name']
        user['phone']=user_data['phone']
        return jsonify({'message': 'user updated','updated_user_data':user_data})
    else:
        return jsonify({'message': 'user not found'}), 404

def delete(user_id):
    for i in data:
        if i['id']==user_id:
            data.remove(i)
            return 'user deleted'
    else:
        return 'user not found'

@app.route('/delete_user/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    user_mes = delete(user_id)
    return jsonify({'message':user_mes})


@app.route('/update_details/<int:user_id>',methods=['PATCH'])
def update_details(user_id):
    user = find_user(user_id)
    if user:
        user_data = request.get_json()
        try:
            user['name'] = user_data['name']
        except:
            pass
        try:
            user['phone'] = user_data['phone']
        except:
            pass

        return jsonify({'message': 'user updated', 'updated_user_data': user_data})

    else:
        return jsonify({'message': 'user not found'}), 404


if __name__=='__main__':
    app.run(host='0.0.0.0',port='81',debug=True)