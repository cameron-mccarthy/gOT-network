import sqlite3
import easysnmp
import dbmanager as db

class Device:
  def __init__(self):
    self._ip = ""
    self._mac = ""
    self._interface = ""
    self._vendor = ""

  @property
  def ip(self):
    return self._ip

  @ip.setter
  def ip(self, new_ip):
    self._ip = new_ip

  @property
  def mac(self):
    return self._mac

  @mac.setter
  def mac(self, new_mac):
    self._mac = new_mac

  @property
  def interface(self):
    return self._interface

  @interface.setter
  def interface(self, new_interface):
    self._interface = new_interface

  @property
  def vendor(self):
    return self._vendor

  @vendor.setter
  def vendor(self, new_vendor):
    self._vendor = new_vendor

  def __repr__(self):
    return f"MAC: {self.mac} IP: {self.ip} Interface: {self.interface} Vendor: {self.vendor}"


def snmpScan(scan_data, oid):
    snmp_target = scan_data.get('IP')
    version = scan_data.get('Version')
    if version == '2':
        community_string = scan_data.get('CS')
        session = easysnmp.Session(hostname=snmp_target, community=community_string, version=2)
    elif version == '3':
        username = scan_data.get('Username')
        encryption_protocol = scan_data.get('EncryptionProtocol')
        encryption_password = scan_data.get('EncryptionPassword')
        auth_protocol = scan_data.get('AuthenticationProtocol')
        auth_password = scan_data.get('AuthenticationPassword')
        session = easysnmp.Session(hostname=snmp_target, security_username=username, privacy_protocol=encryption_protocol, privacy_password=encryption_password, auth_protocol=auth_protocol, auth_password=auth_password, version=3)
    elif version == '1':
        community_string = scan_data.get('CS')
        session = easysnmp.Session(hostname=snmp_target, community=community_string, version=1)
    else:
        print("Error: Incorrect version")
        return

    try:
        data = session.walk(oid)
        return data

    except Exception as e:
        print(f"SNMP Error: {e}")
        return None

def getSNMPPort(scan_data):
    devices = []

    mac_to_bp_data = snmpScan(scan_data, ".1.3.6.1.2.1.17.4.3.1.2")
    bp_to_if_data = snmpScan(scan_data, ".1.3.6.1.2.1.17.1.4.1.2")
    if_to_name_data = snmpScan(scan_data, ".1.3.6.1.2.1.2.2.1.2")

    svi_to_if_data = snmpScan(scan_data, "1.3.6.1.2.1.4.20.1.2")

    if not mac_to_bp_data:
        mac_to_bp_data = snmpScan(scan_data, ".1.3.6.1.2.1.17.7.1.2.2.1.2")

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
        device = Device()
        device.mac = mac
        device.ip = ip
        device.interface = name
        devices.append(device)

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
    return devices

def getSNMPMAC(scan_data):
    devices = []
    data = snmpScan(scan_data,"1.3.6.1.2.1.17.7.1.2.2")
    if data == None:
        return
    data = data[:(len(data) // 2)]
    for entry in data:
        full_mac = entry.oid.split('.')[-6:]
        if len(full_mac) == 6:
            mac = ("-".join(f"{int(byte):02x}" for byte in full_mac)).upper()
            device = Device()
            device.mac = mac
            devices.append(device)
            dev = db.dbSearch(value=mac)
            if not dev:
                db.addDevice(mac, status="Active")
            else:
                db.editDevice(mac, status="Active")
            print(f"MAC: {mac}")
    return devices

def getSNMPARP(scan_data):
    devices = []
    data = snmpScan(scan_data,"1.3.6.1.2.1.4.22.1.2")

    if data == None:
        return
    for entry in data:
        ip = entry.oid_index[2:]

        mac = ("-".join(f"{ord(byte):02x}" for byte in entry.value)).upper()

        device = Device()
        device.mac = mac
        device.ip = ip

        devices.append(device)

        dev = db.dbSearch(value=mac)

        if not dev:
            db.addDevice(mac, ip=ip, status="Active")
        else:
            db.editDevice(mac, ip=ip, status="Active")

        print(f"IP: {ip}, MAC: {mac}")
    return devices


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

def scan(scan_data):
  db.setAllDev("status", "Inactive")
  devices = {}
  mac_data = getSNMPMAC(scan_data)

  print(mac_data)
  for dev in mac_data:
    devices.setdefault((dev.mac, dev.ip, dev.interface), []).append(dev)

  port_data = getSNMPPort(scan_data)
  for dev in port_data:
    if (dev.mac, "", "") in devices:
      if len(devices[dev.mac,"",""]) == 1:



  print(port_data)
  arp_data = getSNMPARP(scan_data)
  print(arp_data)


if __name__ == '__main__':
    test_vendor_lookup = 0
    test_mac_scan = 0
    print_devices = 0
    print_vendors = 0
    test_arp_scan = 0
    remake_db = 1
    test_port_map = 0
    if remake_db:
        db.setupDevicesDB()
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
    if print_devices:
        print(f"Devices:\n{'*'*40}")
        print(db.printDevices())
        print("\n")
    if test_vendor_lookup:
        getVendor()
