from flask import Flask, abort
from flask import request
import json

app = Flask(__name__)

users=[]

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/users/<int:uid>', methods=['GET'])
def users_get(uid):
    if len(users) == 0 or uid > len(users):
        abort(404)
    return json.dumps({'id': userId, 'name': users[uid]})

@app.route('/users', methods=['POST'])
def users_post():
    name = request.form['name']
    user = {'id': len(users)+1, 'name': name}
    users.append(user)
    ret = json.dumps(user)
    return ret, 201

@app.route('/users/<int:uid>', methods=['DELETE'])
def users_delete(uid):
    if len(users) == 0 or userId > len(users):
        abort(404)
    user = users[userId-1]
    users.remove(user)
    return jsonify({'result': True})
    
    usersMap.pop(userId, None)
        return "", 204
