from flask import Flask, Blueprint, current_app, request,jsonify
from werkzeug.utils import secure_filename
import json, os

image_bp = Blueprint('images', __name__)

def load_db():
    with open(current_app.config['DATABASE_FILE']) as f:
        return json.load(f)

def save_db(data):
    with open(current_app.config['DATABASE_FILE'], 'w') as file:
        json.dump(data, file, indent=2)

@image_bp.route('/images', methods=["GET"])
def get_images():
    db = load_db()
    return jsonify(db["image"])

@image_bp.route('/upload', methods=["POST"])
def upload():
    user_id = request.form['user_id']
    file = request.files['image']
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        db = load_db()
        new_image = {
            "id": len(db['image']) + 1,
            "user_id": int(user_id),
            "filename": filename,
            "comments": []
        }
    
        db['image'].append(new_image)
        save_db(db)
        return jsonify({'message': 'Imagen Subida'}), 201
    return jsonify({'Error': 'No se recibio la imagen'}), 400