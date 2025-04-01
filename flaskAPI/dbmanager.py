from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

#TODO
# fetch data
# select by type (sorted)
# setup flask routes


app = Flask(__name__)
CORS(app)

#@app.route('/')
def default():
    return 'Successful Connection'

def setupDevicesDB():
    '''Sets up the devices table in the database.'''
    # connect to/create the devices database
   # try: 
    db = sqlite3.connect('devices.db', check_same_thread=False)
    db.execute('''CREATE TABLE IF NOT EXISTS devices( 
                        ID INTEGER PRIMARY KEY,
                        MAC TEXT, 
                        IP TEXT, 
                        VENDOR TEXT, 
                        PRODUCT TEXT,
                        TYPE TEXT,
                        STATUS TEXT,
                        NOTES TEXT);''')
    #except:
    #    db = sqlite3.connect('devices.db', check_same_thread=False)
    cursor = db.cursor()
    return db, cursor

@app.route('/addDev', methods=['POST'])
def addDevice(mac, ip, product=None, vendor=None, type=None, status='Inactive', notes=None):
    '''Add a device to the database.  MAC, IP, and product are required inputs.'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''INSERT INTO devices (ID, MAC, IP, VENDOR, PRODUCT, TYPE, STATUS, NOTES) VALUES( 
                Null,?,?,?,?,?,?,?)''',(mac, ip, vendor, product, type, status, notes,))
        db.commit()

@app.route('/delDev', methods=['POST'])
def delDevice(mac):
    '''Delete a device from the database based on its mac'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''delete from devices where mac=?;''',(mac,))
        db.commit()

#@app.route('/pntDevs', methods=['GET'])
def printDevices():
    '''Print all devices in database'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
    
        cursor = db.execute('''SELECT * FROM devices;''') 
        data = cursor.fetchall()
        
        devices = []
        for i in range(len(data)):
            item = extractDev(i+1)
            devices.append(item)
    
        #print(data)
        #text = jsonify(devices)
        return devices
    
def printDBRowIDs():
    '''Print all the id numbers of device entries'''
    cursor = db.execute('''SELECT rowid FROM devices;''') 
    data = cursor.fetchall()
    print(data)

def extractDev(id):
    '''Extract row information of a device based on its id.  Returns as a dictionary'''
    cursor = db.execute('''select * from devices where ID = ?;''', (id,))
    data = cursor.fetchall()
    data = [{'ID': entry[0], 'MAC': entry[1], 'IP': entry[2], 'VENDOR': entry[3], 'PRODUCT': entry[4], 'TYPE': entry[5], 'STATUS': entry[6], 'NOTES': entry[7]} for entry in data]
    
    # rewrite as a dictionary
    edit = {'ID': data[0]['ID'],
            'MAC': data[0]['MAC'],
            'IP': data[0]['IP'],
            'Vendor': data[0]['VENDOR'],
            'Product': data[0]["PRODUCT"],
            'Type': data[0]["TYPE"],
            'Status': data[0]["STATUS"],
            'Notes': data[0]["NOTES"]}
    return edit

@app.route('/editDev', methods=['POST'])
def editDevice(id, mac=None, ip=None, vendor=None, product=None, type=None, status=None, notes=None):
    '''Edit one or more values of a device, even its MAC address'''
    
    with sqlite3.connect('devices.db') as db:
        # Coalesce chooses the first non-null option, and requires at least two options.  The second value is the current, previous value.
        # tldr, this updates only the values that have specifically been changed.
        db.execute('''UPDATE devices SET mac = COALESCE(?, mac), ip = COALESCE(?, ip), vendor = COALESCE(?, vendor), product = COALESCE(?, product), type = COALESCE(?, type), status = COALESCE(?, status), notes = COALESCE(?, notes) WHERE id = ?''', (mac, ip, vendor, product, type, status, notes, id))
        db.commit()

db, cursor = setupDevicesDB()
#addDevice('aa','168', 'product1', 'vendor1', 'type1', 'Active', "Have some notes!")
#addDevice('bb','255','no')
#device = extractDev(1)
#print(device)

#if __name__ == '__main__':
#    app.run()