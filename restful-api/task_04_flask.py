#!/usr/bin/python3
"""
Module that contains a simple Flask API
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(users))


@app.route('/status')
def status():
    return 'OK'

@app.route('/add_user', methods=["POST"])
def add_user():
    data = request.json
    if data is None:
        return jsonify({'error': 'Invalid input'}), 400

    username = data.get('username')
    if not username:
        return jsonify({'error': 'Username required'}), 400
    
    if username in users:
        return jsonify({'error': 'Username already exists'}), 400

    user = {
        'username': username,
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[username] = user
    return jsonify({'message': 'User added', 'user': user}), 201

@app.route('/users/<username>')
def user_name(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

if __name__ == "__main__":
    app.run()
