from flask import Flask, jsonify, request
app=Flask(__name__)
users=[
    {
        "id":1,
        "name":"Rakshita",
        "age":21
    },
    {
        "id":2,
        "name":"Rohit",
        "age":22
    }
]
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    user=next((user for user in users if user['id']==user_id),None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message":"User not found"}),404
    
@app.route('/users',methods=['POST'])
def create_user():
    data=request.get_json()
    new_user={
        "id":len(users)+1,
        "name":data['name'],
        "age":data['age']
    }
    users.append(new_user)
    return jsonify(new_user),201

@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    user=next((user for user in users if user['id']==user_id),None)
    if user:
        data=request.get_json()
        user['name']=data.get('name',user['name'])
        user['age']=data.get('age',user['age'])
        return jsonify(user)
    else:
        return jsonify({"message":"User not found"}),404

@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    user=next((user for user in users if user['id']==user_id),None)
    if user:
        users.remove(user)
        return jsonify({"message":"User deleted successfully"})
    else:
        return jsonify({"message":"User not found"}),404
    
if __name__=="__main__":
    app.run(debug=True)
    