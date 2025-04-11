import sqlite3

#TODO
#   setup vuln crud ops


#@app.route('/')
def default():
    return 'Successful Connection'

def setupDevicesDB():
    '''Sets up the devices table in the database.'''
    # connect to/create the devices database
    db = sqlite3.connect('devices.db') #, check_same_thread=False)
    db.execute('''PRAGMA foreign_keys = ON;''')
    db.execute('''CREATE TABLE IF NOT EXISTS devices( 
                        ID INTEGER PRIMARY KEY,
                        MAC TEXT UNIQUE, 
                        IP TEXT, 
                        VENDOR TEXT, 
                        PRODUCT TEXT,
                        TYPE TEXT,
                        STATUS TEXT,
                        NOTES TEXT);''')
    
    db.execute('''CREATE TABLE IF NOT EXISTS vulns(
                    ID INTEGER PRIMARY KEY,
                    MAC TEXT,
                    SEVERITY INT
                    DESC TEXT,
                    URL TEXT,
                    NOTES TEXT,
                    FOREIGN KEY (MAC) REFERENCES devices(MAC));''')

#def addDevice(mac, ip, product=None, vendor=None, type=None, status='Inactive', notes=None):
def addDevice(mac, ip, product=None, vendor=None, type=None, status='Inactive', notes=None):
    '''Add a device to the database.  MAC, IP, and product are required inputs.'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''INSERT INTO devices (ID, MAC, IP, Vendor, Product, Type, Status, Notes) VALUES( 
                Null,?,?,?,?,?,?,?)''',(mac, ip, vendor, product, type, status, notes,))
        db.commit()

def delDevice(mac):
    '''Delete a device from the database based on its mac'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''delete from devices where mac=?;''',(mac,))
        db.commit()

def printDevices():
    '''Print all devices in database'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
    
        cursor = db.execute('''SELECT * FROM devices;''') 
        
        devices = jsonDevice(cursor)
        return devices
    
def jsonDevice(cursor):
    devices = []
    for entry in cursor:
        device = {'ID': entry[0], 'MAC': entry[1], 'IP': entry[2], 'Vendor': entry[3], 'Product': entry[4], 'Type': entry[5], 'Status': entry[6], 'Notes': entry[7]}
        devices.append(device)
    return devices
    
def printOrderedDevices(sortorder):
    '''Order the devices by some parameter'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute(f"SELECT * from devices ORDER BY {sortorder} NULLS LAST")
        devices = jsonDevice(cursor)
        return devices

    
def printDBRowIDs():
    '''Print all the id numbers of device entries'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute('''SELECT rowid FROM devices;''') 
        data = cursor.fetchall()
        print(data)

def extractDev(id):
    '''Extract row information of a device based on its id.  Returns as a dictionary'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
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

def editDevice(mac, ip=None, vendor=None, product=None, type=None, status=None, notes=None):
    '''Edit one or more values of a device, even its MAC address'''
    
    with sqlite3.connect('devices.db') as db:
        # Coalesce chooses the first non-null option, and requires at least two options.  The second value is the current, previous value.
        # tldr, this updates only the values that have specifically been changed.
        db.execute('''UPDATE devices SET ip = COALESCE(?, ip), vendor = COALESCE(?, vendor), product = COALESCE(?, product), type = COALESCE(?, type), status = COALESCE(?, status), notes = COALESCE(?, notes) WHERE mac = ?''', (ip, vendor, product, type, status, notes, mac))
        db.commit()

