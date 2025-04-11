from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import dbmanager as db

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return "Sucessful Connection"

@app.route('/pntDevs', methods=['GET'])
def printDevs():
<<<<<<< Updated upstream
    return jsonify(db.printDevices())
=======
    if request.method == 'GET':
        return jsonify(db.printDevices())
    
    if request.method == 'POST':
        data = request.json
        # the value to sort by, whatever that is
        param = data.get('sortby')
        return jsonify(db.printOrderedDevices(param))
>>>>>>> Stashed changes

@app.route('/addDev', methods=['GET', 'POST'])
def addDev():
    if request.method == 'GET':
        return "This is the /addDev GET request!"
    
    if request.method == 'POST':
        data = request.json
        params = [data.get('MAC'), data.get('IP'), data.get('Product')]
        db.addDevice(params[0],params[1],params[2])
<<<<<<< Updated upstream
    #return "Figure out post requests"
=======
        return jsonify(sucess=True)
>>>>>>> Stashed changes

@app.route('/editDev', methods=['GET', 'POST'])
def editDev():
    if request.method == 'GET':
        return "This is the /editDev GET request!"
    
    if request.method == 'POST':
        data = request.json
        db.editDevice(data.get('MAC'), data.get('IP'), data.get('Vendor'), data.get('Product'), data.get('Type'), data.get('Status'), data.get('Notes'))

@app.route('/delDev', methods=['GET', 'POST'])
def delDev():
    if request.method == 'GET':
        return "This is the /delDev GET request!"
    
    if request.method == 'POST':
        data = request.json
        mac = data.get('MAC')
        db.delDevice(mac)

db.setupDevicesDB()
if __name__ == '__main__':
    app.run()