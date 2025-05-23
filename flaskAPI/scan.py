import sqlite3
import easysnmp
import dbmanager as db

def snmpScan(snmp_target, oid, version=2,community_string="public"):
    if version == 2:
        session = easysnmp.Session(hostname=snmp_target, community=community_string, version=2)
    elif version == 3:
        #TODO: add support for v3
        return
    else:
        #TODO: do we want to support snmp v1? maybe just print error message
        return

    try:
        data = session.walk(oid)
        return data

    except Exception as e:
        print(f"SNMP Error: {e}")
        return None

def getSNMPPort(snmp_target, version=2, community_string="public"):
    mac_to_bp_data = snmpScan(snmp_target, ".1.3.6.1.2.1.17.4.3.1.2", version, community_string)
    bp_to_if_data = snmpScan(snmp_target, ".1.3.6.1.2.1.17.1.4.1.2", version, community_string)
    if_to_name_data = snmpScan(snmp_target, ".1.3.6.1.2.1.2.2.1.2", version, community_string)

    svi_to_if_data = snmpScan(snmp_target, "1.3.6.1.2.1.4.20.1.2", version, community_string)
    
    if not mac_to_bp_data:
        mac_to_bp_data = snmpScan(snmp_target, ".1.3.6.1.2.1.17.7.1.2.2.1.2", version, community_string)

    bp_to_if = {}
    if_to_name = {}
    if_to_ip = {}

    if mac_to_bp_data == None or bp_to_if_data == None or if_to_name_data == None or svi_to_if_data == None:
        return

    for entry in svi_to_if_data:
        interface = entry.value
        ip = entry.oid_index
        if_to_ip[interface] = ip

    for entry in if_to_name_data:
        name = entry.value
        interface = entry.oid_index
        if_to_name[interface] = name

    for entry in bp_to_if_data:
        bridge_port = entry.oid.split(".")[-1]
        interface = entry.value
        bp_to_if[bridge_port] = interface

    #print(f'{mac_to_bp_data} \n {bp_to_if} \n {if_to_name}')
    for entry in mac_to_bp_data:
        bridge_port = entry.value
        raw_mac = entry.oid.split(".")[-6:]
        mac = ("-".join(f"{int(byte):02x}" for byte in raw_mac)).upper()

        if bridge_port in bp_to_if:
            interface = bp_to_if[bridge_port]
            if interface in if_to_name:
                name = if_to_name[bp_to_if[bridge_port]]
        elif bridge_port in if_to_name:
            interface = bridge_port
            name = if_to_name[bridge_port]
        else:
            interface = None
            name = "Unknown"

        ip = None
        if interface in if_to_ip:
            ip = if_to_ip[interface]

        dev = db.dbSearch(value=mac)

        if not dev:
            if ip is None:
                db.addDevice(mac, interface=name, status="Active")
            else:
                db.addDevice(mac, ip=ip, interface=name, status="Active")

        else:
            if ip is None:
                db.editDevice(mac, interface=name, status="Active")
            else:
                db.editDevice(mac, ip=ip, interface=name, status="Active")

        print(f"MAC: {mac}, IP: {ip}, Interface: {interface}, Name: {name}")

def getSNMPMAC(snmp_target, version=2, community_string="public"):
    data = snmpScan(snmp_target,"1.3.6.1.2.1.17.7.1.2.2", version, community_string)
    if data == None:
        return
    data = data[:(len(data) // 2)]


    for entry in data:
        full_mac = entry.oid.split('.')[-6:]
        if len(full_mac) == 6:
            mac = ("-".join(f"{int(byte):02x}" for byte in full_mac)).upper()
            #TODO update device db with dev of this mac
            # this is just to print rn

            dev = db.dbSearch(value=mac)

            if not dev:
                db.addDevice(mac, status="Active")
            else:
                db.editDevice(mac, status="Active")
                
            print(f"MAC: {mac}")
    return

def getSNMPARP(snmp_target, version=2, community_string="public"):
    data = snmpScan(snmp_target,"1.3.6.1.2.1.4.22.1.2", version, community_string)
    
    # set all devices to inactive, then manually update the devices that are found
    db.setAllDev("status", "Inactive")
    if data == None:
        return
    for entry in data:
        ip = entry.oid_index[2:]

        mac = ("-".join(f"{ord(byte):02x}" for byte in entry.value)).upper()

        dev = db.dbSearch(value=mac)

        if not dev:
            db.addDevice(mac, ip=ip, status="Active")
        else:
            db.editDevice(mac, ip=ip, status="Active")

        print(f"IP: {ip}, MAC: {mac}")
        

def getVendor():
    # get devices with an mac and no vendor
    data = db.isNull(outputVar='MAC', filterVar='VENDOR')
    #print(f'Devices with no Vendor: {data}')
    for entry in data:
        mac_prefix = entry[0][0:8]
        print(mac_prefix)
        device_vendor = db.vendorLookup(mac_prefix)
        print(device_vendor)
        print(f'For {entry[0]}, vendor is {device_vendor}')
        db.editDevice(entry[0], vendor=device_vendor)

if __name__ == '__main__':
    test_vendor_lookup = 0
    test_mac_scan = 0
    print_devices = 0
    print_vendors = 0
    test_arp_scan = 0
    remake_db = 0
    test_port_map = 0
    if remake_db:
        db.setupDevicesDB()
    if test_port_map:
        getSNMPPort("172.25.4.42", community_string="Password3")
    if print_vendors:
        print(f"Vendor format:\n{'*'*40}")
        conn = sqlite3.connect("devices.db")
        cursor = conn.cursor()
        cursor = cursor.execute(f"SELECT macPrefix, vendorName FROM vendors")
        data = cursor.fetchall()
        print(data)
        for i in range(50):
            print(data[i])

        conn.close()
    if test_mac_scan:
        print(f"Devices:\n{'*'*40}")
        print(db.printDevices())
        print("\n")
        getSNMPMAC("10.10.10.254",community_string="Password3")
        print(f"Devices:\n{'*'*40}")
        print(db.printDevices())
        print("\n")
    if test_arp_scan:
        getSNMPARP("10.10.10.254",community_string="Password3")
    if print_devices:
        print(f"Devices:\n{'*'*40}")
        print(db.printDevices())
        print("\n")
    if test_vendor_lookup:
        getVendor()
