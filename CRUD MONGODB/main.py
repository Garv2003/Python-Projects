from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv,find_dotenv
import os
import pprint

load_dotenv(find_dotenv())

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))

print(client.list_database_names())

db = client.get_database("test")

collections= db.list_collection_names()

print(collections)

@app.route('/users', methods=['GET'])
def get_users():
    users = db.users.find()
    print(users)
    response = []
    for user in users:
        user['_id'] = str(user['_id'])
        response.append(user)
    return jsonify(response)

@app.route("/users/<id>", methods=["GET"])
def get_user_id(id):
    user = db.users.find_one({"_id": id})
    user["_id"] = str(user["_id"])
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    user = {
        'name': request.json['name'],
        'email': request.json['email']
    }
    user=db.users.insert_one(user)
    print(user.inserted_id)
    return jsonify({'message': 'User created', '_id': str(user.inserted_id)})

@app.route("/insert_many_users", methods=["POST"])
def insert_many():
    users = request.json["users"]
    db.users.insert_many(users)
    return jsonify({"message": "Users created"})

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    db.users.update_one({'_id': id}, {'$set': {
        'name': request.json['name'],
        'email': request.json['email']
    }})
    return jsonify({'message': 'User updated'})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    db.users.delete_one({'_id': id})
    return jsonify({'message': 'User deleted'})

@app.route("/count_users", methods=["GET"])
def count_users():
    count = db.users.count_documents({})
    return jsonify({"count": count})

@app.route("/user_tasks/<user_id>", methods=["GET"])
def get_user_tasks(user_id):
    tasks = db.tasks.find({"user_id": user_id})
    response = []
    for task in tasks:
        task["_id"] = str(task["_id"])
        response.append(task)
    return jsonify(response)

@app.route("/tasks", methods=["POST"])
def create_task():
    task = {
        "user_id": request.json["user_id"],
        "description": request.json["description"]
    }
    task = db.tasks.insert_one(task)
    return jsonify({"message": "Task created", "_id": str(task.inserted_id)})

@app.route("/tasks/<id>", methods=["PUT"])
def update_task(id):
    db.tasks.update_one({"_id": id}, {"$set": {
        "description": request.json["description"]
    }})
    return jsonify({"message": "Task updated"})

@app.route("/tasks/<id>", methods=["DELETE"])
def delete_task(id):
    db.tasks.delete_one({"_id": id})
    return jsonify({"message": "Task deleted"})

@app.route("/tasks/<id>", methods=["GET"])
def get_task(id):
    task = db.tasks.find_one({"_id": id})
    task["_id"] = str(task["_id"])
    return jsonify(task)

@app.route("/count_tasks", methods=["GET"])
def count_tasks():
    count = db.tasks.count_documents({})
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run(debug=True)