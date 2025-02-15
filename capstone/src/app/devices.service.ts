import { Injectable } from '@angular/core';
import { Device } from './interfaces/device';
import { Vulnerability } from './interfaces/vulnerability';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DevicesService {
  deviceList:Device[] = [{IP: "198.164.14.13", MAC: "00-B0-D0-63-C2-26", Vendor: "Dell", Product: "Product", Type: "PLC", Status: "Active"}, 
    {IP: "198.164.14.12", MAC: "00-B0-D0-63-C2-16", Vendor: "Dell", Product: "Product2", Type: "PLC", Status: "Active"}];
  devicesSubject = new BehaviorSubject<Device[]>(this.deviceList);
  deviceObservable: Observable<Device[]> = this.devicesSubject.asObservable()
  constructor() { 
  }

  getAllDevices(): Observable<Device[]>{
    return this.deviceObservable
  }

  getDeviceByIP(ip: string): Device | null {
    for (let device of this.deviceList){
      if (device.IP === ip) return device;
    }
    return null;
  }
  addDevice(newDevice: Device){
    this.deviceList.push(newDevice)
    this.devicesSubject.next([...this.deviceList])
  }
}

@Injectable({
  providedIn: 'root'
})
export class VulnerabilitiesService{
  vulnList: Vulnerability[];
  constructor(){
    this.vulnList = [
      {device : {IP: "198.164.14.13", MAC: "00-B0-D0-63-C2-26", Vendor: "Dell", Product: "Product", Type: "PLC", Status: "Active"}, description: "vuln2", link: "https://material.angular.io/components/card/overview"},
      {device : {IP: "198.164.14.12", MAC: "00-B0-D0-63-C2-16", Vendor: "Dell", Product: "Product2", Type: "PLC", Status: "Active"}, description: "vuln3", link: "vuln3.com"}
    ];
  }

  getAllVulns(): Vulnerability[]{
    return this.vulnList;
  }
}
