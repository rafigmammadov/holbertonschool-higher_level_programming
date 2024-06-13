#!/usr/bin/python3
"""
Module that contains some classes and methods
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_jwt_extended import jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'navibreynrinqinatasi'
jwt = JWTManager(app)

users = {"user1": {"username": "user1",
                   "password": generate_password_hash("password"),
                   "role": "user"},
         "admin1": {"username": "admin1",
                    "password": generate_password_hash("password"),
                    "role": "admin"}}

@auth.verify_password
def verify(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def unauthorized(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.revoked_token_loader
def revoked_token(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.needs_fresh_token_loader
def fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401

@jwt.expired_token_loader
def expired_token(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == '__main__':
    app.run()