import { Injectable } from '@angular/core';
import { Device } from '../interfaces/device';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  url: string = 'http://localhost:5000/'

  private devicesSubject = new BehaviorSubject<Device[]>([]);
  public deviceList: Observable<Device[]> = this.devicesSubject.asObservable();

  constructor(private http: HttpClient) {
    this.loadDevices();
  }

  
  refresh() {
    this.loadDevices();
  } 
    

  private loadDevices() {
    const url = this.url + 'pntDevs';
    this.http.get<Device[]>(url)
      .subscribe(devices => this.devicesSubject.next(devices));
  }

  /*
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
    */

  addDevice(newDevice: Device) {
    console.log("adding device")
    const url = this.url + 'addDev';
    this.http.post(url, newDevice).subscribe(() => {this.loadDevices()}, error => {alert(error.error)})
  }

  deleteDevice(deleteDev: Device) {
    console.log("deleting device")
    const url = this.url + 'delDev';
    this.http.post(url, deleteDev).subscribe(() => {this.loadDevices()}, error => {alert(error.error)} )
  }

  editDevice(newDevice: Device) {
    console.log("adding device")
    const url = this.url + 'editDev';
    this.http.post(url, newDevice).subscribe(() => {this.loadDevices()}, error => {alert(error.error)})
  }

}
