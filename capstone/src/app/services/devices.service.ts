import { Injectable } from '@angular/core';
import { Device } from '../interfaces/device';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  url: string = 'http://localhost:5000/'

  deviceList: Device[] = []

  constructor() {
  }

  async getAllDevices(): Promise<any> {
    const url = this.url + 'pntDevs'
    let result = await fetch(url)
    console.log(result)
    return result
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
