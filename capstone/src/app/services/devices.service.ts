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
    const url = this.url + 'pntDevs';
    let result = this.http.get<Device[]>(url);
    if (!result) console.log("error getting devices");
    return result
  }

  // currently only does IP and MAC
  getDeviceByMethod(method: string, target: string): Device | null {
    if (method.toLowerCase() == "mac"){
      for (let device of this.deviceList!) {
        if (device.MAC === target) return device;
      }
    }
    else if (method.toLowerCase() == "ip"){
      for (let device of this.deviceList!) {
        if (device.IP === target) return device;
      }
    }
    return null;
  }

  addDevice(newDevice: Device) {
    console.log("adding device")
    const url = this.url + 'addDev';
    let result = this.http.post(url, newDevice);
    if (!result) console.log("error adding device");
  }

  deleteDevice(deleteDev: Device) {
    console.log("deleting device")
    const url = this.url + 'delDev';
    let result = this.http.post(url, deleteDev.MAC);
    if (!result) console.log("error deleting device");
  }

}
