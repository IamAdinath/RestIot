# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import json
from dbops import DatabaseOps

app = Flask(__name__, template_folder='template/')


@app.route('/')
def index():
    return json.dumps({'name': 'alice', 'email': 'alice@outlook.com'})


@app.route('/newdevice', methods=['POST'])
def new_device():
    return json.dumps({'message': 'This device exist'})


@app.route('/tempsensors', methods=['POST', 'GET'])
def temp_sensor():
    if request.method == 'GET':
        return render_template("newdevice.html")

    return json.dumps({'message': 'This device exist'})


@app.route('/pressuresensors', methods=['POST'])
def pressure_sensors():
    return json.dumps({'message': 'This device exist'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
