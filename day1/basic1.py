from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def my_function():
    if request.method == 'GET':
        return jsonify({'message': 'Hello, Team'})

    elif request.method == 'POST':
        data=request.get_json()
        return jsonify({'message':'Hi {}'.format(data['name']) })


@app.route('/my_details', methods=['GET', 'POST'])
def my_function2():
    if request.method=='GET':
        return jsonify({'message':'My details'})
    elif request.method=='POST':
        data=request.get_json()
        return jsonify({'message':'Hi, I am {}, {} years old. My phone number is {}'.format(data['name'],data['age'],data['phone_number'])})


if __name__ == '__main__':
    app.run(debug=True)
