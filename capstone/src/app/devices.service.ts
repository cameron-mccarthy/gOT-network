import { Injectable } from '@angular/core';
import { Device } from './interfaces/device';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  deviceList: Device [];

  constructor() { 
    this.deviceList = [{IP: "198.164.14.13", MAC: "00-B0-D0-63-C2-26", Vendor: "Dell", Product: "Product", Type: "PLC", Status: "Active"}, 
      {IP: "198.164.14.12", MAC: "00-B0-D0-63-C2-16", Vendor: "Dell", Product: "Product2", Type: "PLC", Status: "Active"}];
  }

  getAllDevices(): Device[]{
    return this.deviceList;
  }

  getDeviceByIP(ip: string): Device | null {
    for (let device of this.deviceList){
      if (device.IP === ip) return device;
    }
    return null;
  }
}
