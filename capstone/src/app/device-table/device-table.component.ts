import { Component } from '@angular/core';
import { DevicesService } from '../services/devices.service';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { Device } from '../interfaces/device';
import { ActivatedRoute } from '@angular/router';
import { ViewChild, AfterViewInit } from '@angular/core';
import { MatSort, MatSortModule } from '@angular/material/sort';

@Component({
  selector: 'app-device-table',
  imports: [MatTableModule, MatSortModule],
  templateUrl: './device-table.component.html',
  styleUrl: './device-table.component.css'
})


export class DeviceTableComponent {
  ngOnInit(){
    this.DeviceService.getAllDevices().subscribe(data => this.dataSource.data = data)
  }

  @ViewChild(MatSort) sort!: MatSort;

  displayColumns: string[] = ["IP", "MAC", "Vendor", "Product", "Type", "Status"];
  data!: Device[];
  constructor(public DeviceService: DevicesService){
  }
  dataSource = new MatTableDataSource<Device>();

  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
  }

}
