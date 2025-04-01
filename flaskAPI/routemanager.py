from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import dbmanager as db

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return db.default()

@app.route('/pntDevs', methods=['GET'])
def printDevs():
    return jsonify(db.printDevices())

@app.route('/addDev', methods=['GET', 'POST'])
def addDev():
    if request.method == 'GET':
        return "This is a GET request!"
    
    if request.method == 'POST':
        data = request.json
        params = [data.get('MAC'), data.get('IP'), data.get('Product')]
        db.addDevice(params[0],params[1],params[2])
    #return "Figure out post requests"

@app.route('/editDev', methods=['GET', 'POST'])
def editDev():
    #db.editDevice()
    return "Figure out post methods"

db.setupDevicesDB()
if __name__ == '__main__':
    app.run()