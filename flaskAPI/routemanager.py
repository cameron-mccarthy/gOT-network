from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import dbmanager as db
#import scan as scanner

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
        sort = data.get('sortby')
        direction = data.get('direction')
        return jsonify(db.printOrderedDevices(sort, direction))

@app.route('/addDev', methods=['GET', 'POST'])
def addDev():
    if request.method == 'GET':
        return "This is the /addDev GET request!"
    
    if request.method == 'POST':
        data = request.json
        ip = data.get('IP')
        mac = data.get('MAC').upper()
        print(mac)

        # if the mac entry already exists
        if (db.devExists(mac)):

            # if they have the same ip address, don't create the device at all
            devIP = db.dbSearch('IP', 'MAC', 'devices', mac)
            if (ip == devIP[0][0]):
                return "ALERT: Duplicate shared MAC and IP address.\nDevice entry was not created.", 409
            else:
                # add proper alerts.
                db.addVuln(mac, ip, 5, "Duplicate MAC address.  Potential MAC spoofing.", None)
                
                # check if any device has that ip address
                if (db.dbSearch('MAC', 'IP', 'devices', ip)):
                    db.addDevice(mac, ip, data.get('Product'), data.get('Vendor'), data.get('Type'), data.get('Status'), data.get('Notes'))
                    db.addVuln(mac, ip, 3, "Duplicate IP address.", None)
                    return "ALERT: Duplicate MAC.\nALERT: Duplicate IP.\nConflicting device created.", 409
                
                else:
                    db.addDevice(mac, ip, data.get('Product'), data.get('Vendor'), data.get('Type'), data.get('Status'), data.get('Notes'))
                    return "ALERT: Duplicate MAC.\nConflicting device created.", 409
        
        # that ip address is already used
        elif (db.dbSearch('MAC', 'IP', 'devices', ip)):
            db.addVuln(mac, ip, 3, "Duplicate IP address.", None)
            db.addDevice(mac, ip, data.get('Product'), data.get('Vendor'), data.get('Type'), data.get('Status'), data.get('Notes'))
            return "ALERT: Duplicate IP.\nConflicting device created", 409
        
        # No duplicate mac or ip addresses
        else:
            db.addDevice(mac, ip, data.get('Product'), data.get('Vendor'), data.get('Type'), data.get('Status'), data.get('Notes'))
            return jsonify(success=True)

        # try to look up the device
        # if the lookup fails (device doesn't exist), then add the device
        #try:
        #    db.extractDev(data.get('MAC'))
        #except:
        #    db.addDevice(data.get('MAC'), data.get('IP'), data.get('Product'), data.get('Vendor'), data.get('Type'), data.get('Status'), data.get('Notes'))
        #    return jsonify(success=True)
        
        #return "ERROR: Duplicate MAC.\nDevice could not be created."

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
        db.delVulns(mac)
        return jsonify(success=True)

@app.route('/pntVulns', methods=['GET', 'POST'])
def printVulns():
    if request.method == 'GET':
        return jsonify(db.printVulns())
    
    if request.method == 'POST':
        data = request.json
        # find only vulnerabilities on a specific device
        return jsonify(db.printVulns(data.get('MAC')))

@app.route('/addVuln', methods=['GET','POST'])
def addVuln():
    if request.method == 'GET':
        return "This is /addVuln GET request"
    if request.method == 'POST':
        data = request.json
        db.addVuln(data.get('MAC'), data.get('IP'), data.get('Severity'), data.get('Desc'), data.get('URL'))
        return jsonify(success=True)

@app.route('/editVuln', methods=['GET', 'POST'])
def editVuln():
    if request.method == 'GET':
        return "This is the /editVuln GET request!"
    
    if request.method == 'POST':
        data = request.json
        db.editVuln(data.get('ID'), data.get('Notes'))
        return jsonify(success=True)

@app.route('/delVuln', methods=['GET', 'POST'])
def delVuln():
    if request.method == 'GET':
        return "This is the /delVuln GET request!"
    
    if request.method == 'POST':
        data = request.json
        db.delVuln(data.get('ID'))
        return jsonify(success=True)

@app.route('/scanDevs', methods=['GET'])
def scanDevs():
    if request.method == 'GET':
        ip = "10.10.10.254"
        community_string = "Password3"
       # scanner.getSNMPMAC(ip, community_string)
       # scanner.getSNMPARP(ip, community_string)
       # scanner.getVendor(ip, community_string)
        return jsonify(success=True)


db.setupDevicesDB()
if __name__ == '__main__':
    app.run()