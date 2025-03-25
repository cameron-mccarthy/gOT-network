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

  getAllDevices(): Observable<Device[]> {
    const url = this.url + 'pntDevs'
    let result; 
    fetch(url).then(x => result = x)
    return result!.json()
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
