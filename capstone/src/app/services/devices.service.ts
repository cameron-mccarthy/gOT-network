import { Injectable } from '@angular/core';
import { Device } from '../interfaces/device';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Vulnerability } from '../interfaces/vulnerability';
import { VulnerabilityService } from './vulnerability.service';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  url: string = 'http://localhost:5000/'

  private devicesSubject = new BehaviorSubject<Device[]>([]);
  public deviceList: Observable<Device[]> = this.devicesSubject.asObservable();

  constructor(private http: HttpClient, private AlertService: VulnerabilityService) {
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
    const url = this.url + 'addDev';
    this.http.post(url, newDevice).subscribe(() => {this.loadDevices()}, error => {{this.addAlert(newDevice, error.error)}})
  }

  deleteDevice(deleteDev: Device) {
    const url = this.url + 'delDev';
    this.http.post(url, deleteDev).subscribe(() => {this.loadDevices()}, error => {alert(error.error)} )
  }

  editDevice(newDevice: Device) {
    const url = this.url + 'editDev';
    this.http.post(url, newDevice).subscribe(() => {this.loadDevices()}, error => {this.addAlert(newDevice, error.error)})
  }

  scan(scanData: {IP:string, Version:string, CS:string}){
    const url = this.url + 'scanDevs';
    this.http.post(url, scanData).subscribe(() => {this.loadDevices()}, error => {alert(error.error)})
  }

  addAlert(device: Device, error: string){
    alert(error)
    this.AlertService.addAlert({ID: 0,
      MAC: device.MAC,
      IP: device.IP,
      Severity: 5,
      Desc: error,
      URL: null,
      Notes: error})
  }
}
