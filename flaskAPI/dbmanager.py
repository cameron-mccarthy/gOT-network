import sqlite3
import requests

#TODO
#   Functionality to status column (active/inactive)
#   Button on frontend to call script                   ==COMPLETE==
#   Alerts page with duplicate MAC alert, IP alert      ==COMPLETE==

def setupDevicesDB():
    '''Sets up the devices table in the database.'''
    # connect to/create the devices database
    # try:
    db = sqlite3.connect('devices.db') #, check_same_thread=False)
    db.execute('''CREATE TABLE IF NOT EXISTS devices( 
                        MAC TEXT, 
                        IP TEXT, 
                        INTERFACE TEXT,
                        VENDOR TEXT, 
                        PRODUCT TEXT,
                        TYPE TEXT,
                        STATUS TEXT,
                        NOTES TEXT,
                        UNIQUE(MAC, IP));''')
    
    db.execute('''CREATE TABLE IF NOT EXISTS vulns(
                ID INTEGER PRIMARY KEY,
                MAC TEXT,
                IP TEXT,
                SEVERITY INT,
                DESC TEXT,
                URL TEXT,
                NOTES TEXT,
                FOREIGN KEY (MAC) REFERENCES devices(MAC));''')
    db.execute('''CREATE TABLE IF NOT EXISTS vendors (
                macPrefix TEXT PRIMARY KEY NOT NULL,
                vendorName TEXT NOT NULL)''')
    #updateVendor()
    #except:
    #    db = sqlite3.connect('devices.db', check_same_thread=False)

def addDevice(mac, ip=None, interface=None, product=None, vendor=None, type=None, status='Inactive', notes=None):
    '''Add a device to the database.  MAC, IP, and product are required inputs.'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''INSERT INTO devices (MAC, IP, Interface, Vendor, Product, Type, Status, Notes) VALUES( 
                ?,?,?,?,?,?,?,?)''',(mac, ip, interface,vendor, product, type, status, notes,))
        db.commit()

def delDevice(mac,ip):
    '''Delete a device from the database based on its mac'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''delete from devices where (mac=? and ip=?);''',(mac,ip))
        db.commit()

# function that adds device if it doesn't exist, edits device if it does
def importDevice(mac, ip=None, interface=None, product=None, vendor=None, type=None, status='Inactive', notes=None):
    '''Imports a device from the backend program.  If the device exists already, it is updated with new info.  Otherwise it is added.'''
    if (devExists(mac)):
        editDevice(mac, ip, product, interface, vendor, type, status, notes)
        return f"Device '{mac}' updated."
    else:
        addDevice(mac, ip, product, interface, vendor, type, status, notes)
        return f"Device '{mac}' added."

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
        device = {'MAC': entry[0], 'IP': entry[1], 'Interface': entry[2], 'Vendor': entry[3], 'Product': entry[4], 'Type': entry[5], 'Status': entry[6], 'Notes': entry[7]}
        devices.append(device)
    return devices

def printOrderedDevices(sortorder, direction=None):
    '''Order the devices by some parameter'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        if (direction.upper() == "DESC"):
            cursor = db.execute(f"SELECT * from devices ORDER BY {sortorder} DESC NULLS LAST")
        else:
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

# check if device exists
def devExists(mac):
    '''Uses mac address to determine if a device exists.  Returns as a boolean.'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute('''SELECT rowid FROM devices WHERE mac=?;''',(mac,))
        data = cursor.fetchall()

        # if device doesn't exist
        if not data:
            return False
        else:
            return True

def extractDev(mac):
    '''Extract row information of a device based on its mac.  Returns as a dictionary'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute('''select * from devices where mac = ?;''', (mac,))
        data = cursor.fetchall()
        data = [{'MAC': entry[0], 'IP': entry[1],'INTERFACE': entry[2], 'VENDOR': entry[3], 'PRODUCT': entry[4], 'TYPE': entry[5], 'STATUS': entry[6], 'NOTES': entry[7]} for entry in data]
        
        # rewrite as a dictionary
        edit = {'ID': data[0]['ID'],
                'MAC': data[0]['MAC'],
                'IP': data[0]['IP'],
                'INTERFACE' : data[0]['INTERFACE'],
                'Vendor': data[0]['VENDOR'],
                'Product': data[0]["PRODUCT"],
                'Type': data[0]["TYPE"],
                'Status': data[0]["STATUS"],
                'Notes': data[0]["NOTES"]}
        return edit

def editDevice(mac, ip=None, interface=None, product=None, vendor=None, type=None, status=None, notes=None):
    '''Edit one or more values of a device, even its MAC address'''
    
    with sqlite3.connect('devices.db') as db:
        # Coalesce chooses the first non-null option, and requires at least two options.  The second value is the current, previous value.
        # tldr, this updates only the values that have specifically been changed.
        db.execute('''UPDATE devices SET ip = COALESCE(?, ip), interface = COALESCE(?, interface), vendor = COALESCE(?, vendor), product = COALESCE(?, product), type = COALESCE(?, type), status = COALESCE(?, status), notes = COALESCE(?, notes) WHERE mac = ?''', (ip, interface, vendor, product, type, status, notes, mac))
        db.commit()

def setAllDev(column, value):
    with sqlite3.connect('devices.db') as db:
        db.execute(f"UPDATE devices set {column} = ?", (value,))
        db.commit()

def updateStatus(mac, status):
    with sqlite3.connect('devices.db') as db:
        editDevice(mac, status=status)
        db.commit()

# vuln ops

def addVuln(mac, ip, sev, desc, url):
    '''Add a vulnerability to a device'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''INSERT INTO vulns (ID, MAC, IP, severity, desc, url, Notes) VALUES( 
                Null,?,?,?,?,?,Null)''',(mac, ip, sev, desc, url))
        db.commit()

def delVuln(id):
    '''Delete a vuln from the database based on its id'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''delete from vulns where id=?;''',(str(id)))
        db.commit()

def delVulns(mac,ip):
    '''Delete a vuln from the database based on its mac'''
    with sqlite3.connect('devices.db') as db:
        db.execute('''delete from vulns where (mac=? AND ip=?);''',(mac,ip,))
        db.commit()

def printVulns(mac=None):
    '''Print all vulns in database'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
    
        if not mac:
            cursor = db.execute('''SELECT * FROM vulns;''') 
        else:
            cursor = db.execute('''SELECT * FROM vulns WHERE mac=?''',(mac,))

        devices = jsonVuln(cursor)
        return devices

def jsonVuln(cursor):
    '''Create a list of vulnerability dicitonaries.  Takes in a sql select (cursor) as input'''
    vulns = []
    for entry in cursor:
        vuln = {'ID': entry[0], 'MAC': entry[1], 'IP': entry[2], 'Severity': entry[3], 'Desc': entry[4], 'URL': entry[5], 'Notes': entry[6]}
        vulns.append(vuln)
    return vulns

def editVuln(id, notes=None):
    '''Edit the note attribute of a vulnerability.  Must call by vuln id.'''
    
    with sqlite3.connect('devices.db') as db:
        # Coalesce chooses the first non-null option, and requires at least two options.  The second value is the current, previous value.
        # tldr, this updates only the values that have specifically been changed.
        db.execute('''UPDATE vulns SET notes = COALESCE(?, notes) WHERE id = ?''', (notes, id))
        db.commit()

def countEntries(table):
    '''Count number of entries in a table.  Takes table name.  Returns an int.'''
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute(f"SELECT COUNT(*) FROM {table}")
        num = cursor.fetchone()
        return num[0]

def dbSearch(outputVar='MAC', filterVar='MAC', table='devices', value=''):
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute(f"SELECT {outputVar} FROM {table} WHERE {filterVar} == ? ;", (value,))
        return cursor.fetchall()

def isNull(outputVar='MAC', filterVar='MAC', table='devices'):
    with sqlite3.connect('devices.db') as db:
        cursor = db.cursor()
        cursor = db.execute(f"SELECT {outputVar} FROM {table} WHERE {filterVar} IS NULL;")
        return cursor.fetchall()

def vendorLookup(macPrefix):
        device_vendor = dbSearch(outputVar="vendorName", filterVar="macPrefix", table="vendors", value=macPrefix)
        if not device_vendor:
            return 'Unknown'
        return device_vendor[0][0]

def updateVendor():
    
    URL = "https://maclookup.app/downloads/json-database/get-db"
    response = requests.get(url = URL)
    data = response.json()
    with sqlite3.connect('devices.db') as db:
        for entry in data:
            entry["macPrefix"] = entry["macPrefix"].replace(":", "-")
            db.execute('''REPLACE INTO vendors (macPrefix, vendorName) VALUES (?, ?)''', (entry["macPrefix"], entry["vendorName"]))
