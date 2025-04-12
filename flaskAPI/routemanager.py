from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import dbmanager as db

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return "Successful Connection"

@app.route('/pntDevs', methods=['GET'])
def printDevs():
    if request.method == 'GET':
        return jsonify(db.printDevices())
    
    if request.method == 'POST':
        data = request.json
        # the value to sort by, whatever that is
        param = data.get('sortby')
        return jsonify(db.printOrderedDevices(param))

@app.route('/addDev', methods=['GET', 'POST'])
def addDev():
    if request.method == 'GET':
        return "This is the /addDev GET request!"
    
    if request.method == 'POST':
        data = request.json
        
        # try to look up the device
        # if the lookup fails (device doesn't exist), then add the device
        try:
            db.extractDev(data.get('MAC'))
        except:
            db.addDevice(data.get('MAC'), data.get('IP'), data.get('Product'), data.get('Vendor'), data.get('Type'), data.get('Status'), data.get('Notes'))
            return jsonify(sucess=True)
        
        return "ERROR: Duplicate MAC.\nDevice could not be created."

@app.route('/editDev', methods=['GET', 'POST'])
def editDev():
    if request.method == 'GET':
        return "This is the /editDev GET request!"
    
    if request.method == 'POST':
        data = request.json
        db.editDevice(data.get('MAC'), data.get('IP'), data.get('Product'), data.get('Vendor'), data.get('Type'), data.get('Status'), data.get('Notes'))
        return jsonify(success=True)

@app.route('/delDev', methods=['GET', 'POST'])
def delDev():
    if request.method == 'GET':
        return "This is the /delDev GET request!"
    
    if request.method == 'POST':
        data = request.json
        mac = data.get('MAC')
        db.delDevice(mac)
        return jsonify(success=True)

db.setupDevicesDB()
if __name__ == '__main__':
    app.run()