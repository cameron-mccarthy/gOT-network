import { Injectable } from '@angular/core';
import { Device } from './device';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  deviceList: Device [];

  constructor() { 
    this.deviceList = [{IP: "198.164.14.13", MAC: "00-B0-D0-63-C2-26", Vendor: "Dell INc", Product: "Product", Type: "PLC", Status: "Active"}];
  }

  getAllDevices(): Device[]{
    return this.deviceList;
  }

  getDeviceByIP(): Device {
    return this.deviceList[0]
  }
}
