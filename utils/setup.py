import os
import json
from config import Config

def init_directories():
    os.makedirs(Config.DATA_FOLDER, exist_ok=True)
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

def init_database():
    if not os.path.exists(Config.DATABASE_FILE):
        #print("pase por aca")
        with open(Config.DATABASE_FILE,'w') as f:
            #print("discreto")
            json.dump({ "users": []}, f) #contenido de la base de datos si no existe