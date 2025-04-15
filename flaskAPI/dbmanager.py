import sqlite3

#TODO
#   setup vuln crud ops

def setupDevicesDB():
    '''Sets up the devices table in the database.'''
    # connect to/create the devices database
    # try:
    db = sqlite3.connect('devices.db') #, check_same_thread=False)
    db.execute('''CREATE TABLE IF NOT EXISTS devices( 
                        MAC TEXT PRIMARY KEY, 
                        IP TEXT, 
                        VENDOR TEXT, 
                        PRODUCT TEXT,
                        TYPE TEXT,
                        STATUS TEXT,
                        NOTES TEXT);''')
    
    db.execute('''CREATE TABLE IF NOT EXISTS vulns(
                ID INTEGER PRIMARY KEY,
                MAC TEXT,
                SEVERITY INT,
                DESC TEXT,
                URL TEXT,
                NOTES TEXT,
                FOREIGN KEY (MAC) REFERENCES devices(MAC));''')
    #except:
    #    db = sqlite3.connect('devices.db', check_same_thread=False)

def addDevice(mac, ip=None, product=None, vendor=None, type=None, status='Inactive', notes=None):
    '''Add a device to the database.  MAC, IP, and product are required inputs.'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''INSERT INTO devices (MAC, IP, Vendor, Product, Type, Status, Notes) VALUES( 
                ?,?,?,?,?,?,?)''',(mac, ip, vendor, product, type, status, notes,))
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
        device = {'MAC': entry[0], 'IP': entry[1], 'Vendor': entry[2], 'Product': entry[3], 'Type': entry[4], 'Status': entry[5], 'Notes': entry[6]}
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

def extractDev(mac):
    '''Extract row information of a device based on its mac.  Returns as a dictionary'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute('''select * from devices where mac = ?;''', (mac,))
        data = cursor.fetchall()
        data = [{'MAC': entry[0], 'IP': entry[1], 'VENDOR': entry[2], 'PRODUCT': entry[3], 'TYPE': entry[4], 'STATUS': entry[5], 'NOTES': entry[6]} for entry in data]
        
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

def editDevice(mac, ip=None, product=None, vendor=None, type=None, status=None, notes=None):
    '''Edit one or more values of a device, even its MAC address'''
    
    with sqlite3.connect('devices.db') as db:
        # Coalesce chooses the first non-null option, and requires at least two options.  The second value is the current, previous value.
        # tldr, this updates only the values that have specifically been changed.
        db.execute('''UPDATE devices SET ip = COALESCE(?, ip), vendor = COALESCE(?, vendor), product = COALESCE(?, product), type = COALESCE(?, type), status = COALESCE(?, status), notes = COALESCE(?, notes) WHERE mac = ?''', (ip, vendor, product, type, status, notes, mac))
        db.commit()

# vuln ops

def addVuln(mac, sev, desc, url):
    '''Add a vulnerability to a device'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''INSERT INTO vulns (ID, MAC, severity, desc, url, Notes) VALUES( 
                Null,?,?,?,?,Null)''',(mac, sev, desc, url))
        db.commit()

def delVuln(id):
    '''Delete a vuln from the database based on its id'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''delete from vulns where id=?;''',(str(id)))
        db.commit()

def delVulns(mac):
    '''Delete a vuln from the database based on its mac'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''delete from vulns where mac=?;''',(mac))
        db.commit()

def printVulns(mac=None):
    '''Print all vulns in database'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
    
        if not mac:
            cursor = db.execute('''SELECT * FROM vulns;''') 
        else:
            cursor = db.execute('''SELECT * FROM vulns WHERE mac=?''',(mac))

        devices = jsonVuln(cursor)
        return devices

def jsonVuln(cursor):
    '''Create a list of vulnerability dicitonaries.  Takes in a sql select (cursor) as input'''
    vulns = []
    for entry in cursor:
        vuln = {'ID': entry[0], 'MAC': entry[1], 'Severity': entry[2], 'Desc': entry[3], 'URL': entry[4], 'Notes': entry[5]}
        vulns.append(vuln)
    return vulns

def editVuln(id, notes=None):
    '''Edit the note attribute of a vulnerability.  Must call by vuln id.'''
    
    with sqlite3.connect('devices.db') as db:
        # Coalesce chooses the first non-null option, and requires at least two options.  The second value is the current, previous value.
        # tldr, this updates only the values that have specifically been changed.
        db.execute('''UPDATE vulns SET notes = COALESCE(?, notes) WHERE id = ?''', (notes, id))
        db.commit()

