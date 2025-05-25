from flask import Flask
from flask_cors import CORS
from api import create_api
from config import Config
import os
from utils.setup import init_database, init_directories


app = Flask(__name__)

CORS(app) # cors para habilitar interaccion con el navegador web

# configuracion de archivo de base de datps json
app.config.from_object(Config)
init_directories()
init_database()

#-----------------------------------------------------------------------------

create_api(app)

# ruta de prueba
@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':
    #app.run(debug=True)
    # Esto es solo cuando estemos en produccion
    # es decir, el programa este en el servidor (la nube)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)