#TODO import resources for manage the application
from flask import Flask, render_template, jsonify,session,request, redirect, url_for
from dev_routes import Routes
from flask_cors import CORS
from database.mysql_connect import connectdb
from dev_api.api import api
from dotenv import load_dotenv
from flask_socketio import SocketIO
from flask_socketio import join_room
from werkzeug.security import generate_password_hash, check_password_hash
import os
import secrets


#TODO init app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
socketio = SocketIO(app)



#secret_key = secrets.token_hex(16) genera al secret key para el manejo de sesiones
#print(secret_key)

CORS(app, resources={r"/api/*": {"origins": "http://192.168.18.5:5000"}})


#TODO getter the conexion a mysql
mysql = connectdb(app)

#TODO import api
api(app, mysql, jsonify)

#TODO init the routes for manage aplication
Routes.routes(app, render_template,session, request, mysql, jsonify, redirect, url_for,socketio,join_room,generate_password_hash, check_password_hash)

@socketio.on('update_event')
def handle_update_event(data):
    # Esta función será llamada cuando se emita el evento 'update_event'
    # Puedes realizar las operaciones necesarias y luego emitir un evento para actualizar la vista en todos los clientes.
    socketio.emit('update_view', data, broadcast=True)

#TODO run application web
if __name__ == '__main__':
    app.run(debug=True,port=5000 ,host="192.168.18.5")