from flask import Flask, Blueprint, current_app, request,jsonify
import json

auth_bp = Blueprint('auth', __name__)

#carga el archivo json
def load_db():
    with open(current_app.config['DATABASE_FILE']) as f:
        return json.load(f)

def save_db(data):
    with open(current_app.config['DATABASE_FILE'], 'w') as file:
        json.dump(data, file, indent=2)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json #datos que vienen desde postman
    #print(data)
    db = load_db() #datos almacenas en el servidor

    for user in db["users"]:
        if user["username"] == data["username"] and user["password"] == data["password"]:
            return jsonify({'mensaje': 'login exitoso', 'user_id': user["id"]}), 200
    
    return jsonify({'Error': 'Credenciales invalidas'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    db = load_db()

    if any(u["username"] == data["username"] and u["password"] ==data["password"] for u in db["users"]):
        return jsonify({'Error' : 'El usuario ya existe'}), 400
    
    newuser = {
        "id": len(db["users"]) + 1,
        "username": data["username"],
        "password": data["password"]
    }

    db["users"].append(newuser)
    save_db(db)
    return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201


@auth_bp.route('/users', methods=["GET"])
def get_users():
    db = load_db()
    return jsonify(db["users"]), 200

