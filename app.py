#TODO import resources for manage the application
from flask import Flask, render_template, jsonify
from dev_routes import Routes
from flask_cors import CORS
from database.mysql_connect import connectdb
from dev_api.api import api

#TODO init app
app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://192.168.18.5:5000"}})


#TODO getter the conexion a mysql
mysql = connectdb(app)

#TODO import api
api(app, mysql, jsonify)

#TODO init the routes for manage aplication
Routes.routes(app, render_template)

#TODO run application web
if __name__ == '__main__':
    app.run(debug=True,port=5000 ,host="192.168.18.5")