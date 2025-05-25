from flask import Flask, Blueprint, current_app, request,jsonify
import json

comments_bp = Blueprint('comments', __name__)

def load_db():
    with open(current_app.config['DATABASE_FILE']) as f:
        return json.load(f)

def save_db(data):
    with open(current_app.config['DATABASE_FILE'], 'w') as file:
        json.dump(data, file, indent=2)

@comments_bp.route('/comments/<int:image_id>', methods=["POST"])
def add_comment(image_id):
    data = request.json # trae el user_id y el text
    db = load_db()

    for image in db['image']:
        if image['id'] == image_id:
            newComment = {
                "user_id": data["user_id"],
                "text": data["comment"]
            }
            image['comments'].append(newComment)
            save_db(db)
            return jsonify({'message': 'Comentario agregado'}),201
    return jsonify({'Error': 'Imagen no encontrada'}), 404