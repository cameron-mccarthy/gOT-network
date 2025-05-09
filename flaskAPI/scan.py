import sqlite3
import easysnmp
import dbmanager as db

class Device:
  def __init__(self):
    self._ip = ""
    self._mac = ""
    self._interface = ""

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

  def __repr__(self):
    return f"MAC: {self.mac} IP: {self.ip} Interface: {self.interface}"


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

def getData(scan_data):

    devices = []

    if_to_svi_data = snmpScan(scan_data, "1.3.6.1.2.1.4.20.1.2")
    ip_to_mac_data = snmpScan(scan_data, ".1.3.6.1.2.1.4.22.1.2")
    mac_to_bp_data = snmpScan(scan_data, ".1.3.6.1.2.1.17.7.1.2.2.1.2")
    bp_to_if_data = snmpScan(scan_data, ".1.3.6.1.2.1.17.1.4.1.2")
    if_to_name_data = snmpScan(scan_data, ".1.3.6.1.2.1.31.1.1.1.1")

    if not if_to_name_data:
        if_to_name_data = snmpScan(scan_data, ".1.3.6.1.2.1.2.2.1.2")

    if not mac_to_bp_data:
        mac_to_bp_data = snmpScan(scan_data, ".1.3.6.1.2.1.17.4.3.1.2")


    if mac_to_bp_data == None or if_to_name_data == None or bp_to_if_data == None or if_to_svi_data == None or ip_to_mac_data == None:
      return

    if_to_svi = {}
    bp_to_if = {}
    if_to_name = {}
    mac_to_ip = {}


    for entry in if_to_name_data:
        name = entry.value
        interface = entry.oid_index
        if_to_name[interface] = name

    for entry in bp_to_if_data:
        bridge_port = entry.oid.split(".")[-1]
        interface = entry.value
        bp_to_if[bridge_port] = interface

    for entry in if_to_svi_data:
        interface = entry.value
        ip = entry.oid_index
        if_to_svi[interface] = ip

    for entry in ip_to_mac_data:
        raw_mac = entry.value.encode('latin1')
        mac = ("-".join(f"{byte:02x}" for byte in raw_mac)).upper()
        ip = ".".join(entry.oid_index.split('.')[1:])
        if not mac_to_bp_data:
            device = Device()
            device.mac = mac
            device.ip = ip
            devices.append(device)
        mac_to_ip[mac] = ip
    if not mac_to_bp_data:
        print("Empty mac to bp")
        print(devices)
        return devices

    for entry in mac_to_bp_data:
        bridge_port = entry.value
        raw_mac = entry.oid.split(".")[-6:]
        mac = ("-".join(f"{int(byte):02x}" for byte in raw_mac)).upper()


        if bridge_port in bp_to_if:
            interface = bp_to_if[bridge_port]
            if interface in if_to_name:
                name = if_to_name[bp_to_if[bridge_port]]
            else:
                name = ""
        elif bridge_port in if_to_name:
            interface = bridge_port
            name = if_to_name[bridge_port]
        else:
            interface = None
            name = ""

        if interface in if_to_svi:
            ip = if_to_svi[interface]
        elif mac in mac_to_ip:
            ip = mac_to_ip[mac]
        else:
            ip = ""

        device = Device()
        device.mac = mac
        device.ip = ip
        device.interface = name
        devices.append(device)

    print(devices)
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
  devices = getData(scan_data)
  if devices is None:
    return
  for dev in devices:
    dbdev = db.dbSearch(value=dev.mac)
    if not dbdev:
      db.addDevice(dev.mac, ip=dev.ip, interface=dev.interface, status='Active')
    else:
      db.editDevice(dev.mac, ip=dev.ip, interface=dev.interface, status='Active')
  getVendor()




if __name__ == '__main__':
  test_2scan = 1
  data = {'IP': '10.10.10.254', 'Version': '2', 'CS': 'Password3', 'Username': '', 'EncryptionPassword': '', 'EncryptionProtocol': '', 'AuthenticationPassword': '', 'AuthenticationProtocol': ''}
  data2 = {'IP': '172.25.4.1', 'Version': '2', 'CS': 'Password3', 'Username': '', 'EncryptionPassword': '', 'EncryptionProtocol': '', 'AuthenticationPassword': '', 'AuthenticationProtocol': ''}
  devs = []
  if test_2scan:
    devs = scan(data)
