import { Injectable } from '@angular/core';
import { Device } from '../interfaces/device';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  url: string = 'http://localhost:5000/'

  deviceList: Device[] = []

  constructor() {
  }

  getAllDevices() {
    const url = this.url + ''
    return null;
  }

  getDeviceByIP(ip: string): Device | null {
      for (let device of this.deviceList!) {
        if (device.IP === ip) return device;
      }
    return null;
  }

  addDevice(newDevice: Device) {
    this.deviceList.push(newDevice)
  }
}
