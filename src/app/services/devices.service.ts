import { Injectable } from '@angular/core';
import { Device } from '../interfaces/device';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
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

  loadDevices() {
    const url = this.url + 'pntDevs';
    this.http.get<Device[]>(url)
      .subscribe(devices => this.devicesSubject.next(devices));
      this.AlertService.loadAlerts();
  }

  addDevice(newDevice: Device) {
    const url = this.url + 'addDev';
    this.http.post(url, newDevice).subscribe(() => {this.loadDevices()}, error => {{this.addAlert(error)}})
  }

  deleteDevice(deleteDev: Device) {
    const url = this.url + 'delDev';
    this.http.post(url, deleteDev).subscribe(() => {this.loadDevices()}, error => {this.addAlert(error.error)} )
  }

  editDevice(newDevice: Device) {
    const url = this.url + 'editDev';
    this.http.post(url, newDevice).subscribe(() => {this.loadDevices()}, error => {this.addAlert(error)})
  }

  scan(scanData: object){
    const url = this.url + 'scanDevs';
    this.http.post(url, scanData).subscribe(() => {this.loadDevices()}, error => {this.addAlert(error.error)})
  }

  addAlert(error: any){
    if (error.status == 409){
      alert(error.error);
    }
    this.loadDevices();
  }
}
