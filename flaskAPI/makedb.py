
import sqlite3
import requests
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
URL = "https://maclookup.app/downloads/json-database/get-db"
response = requests.get(url = URL)
data = response.json()
with sqlite3.connect('devices.db') as db:
    for entry in data:
        entry["macPrefix"] = entry["macPrefix"].replace(":", "-")
        db.execute('''REPLACE INTO vendors (macPrefix, vendorName) VALUES (?, ?)''', (entry["macPrefix"], entry["vendorName"]))
