import { Injectable } from '@angular/core';
import { Device } from '../interfaces/device';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  url: string = 'http://localhost:5000/'

  deviceList: Device[] = []

  constructor(private http: HttpClient) {
  }

  getAllDevices(): Observable<Device[]> {
    const url = this.url + 'pntDevs'
    let result = this.http.get<Device[]>(url)
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
