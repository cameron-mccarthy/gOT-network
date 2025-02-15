import { Component } from '@angular/core';
import { DevicesService } from '../devices.service';
import { MatTableModule } from '@angular/material/table';
import { Device } from '../interfaces/device';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-device-table',
  imports: [MatTableModule],
  templateUrl: './device-table.component.html',
  styleUrl: './device-table.component.css'
})


export class DeviceTableComponent {
  ngOnInit(){
    this.DeviceService.getAllDevices().subscribe(data => this.data = data)
  }
  displayColumns: string[] = ["IP", "MAC", "Vendor", "Product", "Type", "Status"];
  data!: Device[];
  constructor(public DeviceService: DevicesService){
  }
}
