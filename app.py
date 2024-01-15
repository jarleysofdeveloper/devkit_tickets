#TODO import resources for manage the application
from flask import Flask, render_template, jsonify,session,request, redirect, url_for
from dev_routes import Routes
from flask_cors import CORS
from database.mysql_connect import connectdb
from dev_api.api import api
from dotenv import load_dotenv
import os
import secrets

#TODO init app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

#secret_key = secrets.token_hex(16) genera al secret key para el manejo de sesiones
#print(secret_key)

CORS(app, resources={r"/api/*": {"origins": "http://192.168.18.5:5000"}})


#TODO getter the conexion a mysql
mysql = connectdb(app)

#TODO import api
api(app, mysql, jsonify)

#TODO init the routes for manage aplication
Routes.routes(app, render_template,session, request, mysql, jsonify, redirect, url_for)

#TODO run application web
if __name__ == '__main__':
    app.run(debug=True,port=5000 ,host="192.168.18.5")