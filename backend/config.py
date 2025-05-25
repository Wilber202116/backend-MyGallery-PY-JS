import os

class Config:
    UPLOAD_FOLDER = './backend/static/uploads'
    DATA_FOLDER = './backend/data'
    DATABASE_FILE = os.path.join(DATA_FOLDER, 'database.json')