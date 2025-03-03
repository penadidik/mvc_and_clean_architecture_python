from flask import request, jsonify
from models.user import User
from database.db import db

def get_users():
    users = User.query.all()
    return jsonify([
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        } for user in users
    ])

def create_user():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(
        {
            "message": "User created successfully"
        }
    ), 201

