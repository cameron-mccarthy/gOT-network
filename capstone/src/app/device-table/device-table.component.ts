import { Component, Input } from '@angular/core';
import { DevicesService } from '../services/devices.service';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { Device } from '../interfaces/device';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatMenuModule} from '@angular/material/menu';
import { AddDeviceDialogComponent } from '../add-device-dialog/add-device-dialog.component';
import { inject } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { DeleteDialogComponent } from '../delete-dialog/delete-dialog.component';
import { NotesDialogComponent } from '../notes-dialog/notes-dialog.component';
import { ViewChild, AfterViewInit } from '@angular/core';
import { MatSort, MatSortModule } from '@angular/material/sort';

@Component({
  selector: 'app-device-table',
  imports: [MatTableModule, MatButtonModule, MatIconModule, MatMenuModule, MatSortModule],
  templateUrl: './device-table.component.html',
  styleUrl: './device-table.component.css'
})


export class DeviceTableComponent {
  readonly dialog = inject(MatDialog);
  ngOnInit(){
    this.DeviceService.getAllDevices().subscribe(data => this.dataSource.data = data)
  }

  @ViewChild(MatSort) sort!: MatSort;

  displayColumns: string[] = ["IP", "MAC", "Vendor", "Product", "Type", "Status"];
  constructor(public DeviceService: DevicesService){
  }
  dataSource = new MatTableDataSource<Device>();

  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
  }

  edit(device:Device){
    const dialogRef = this.dialog.open(AddDeviceDialogComponent, {data: {edit: true, device: device}});
        dialogRef.afterClosed().subscribe(result => {
          if (result){
            this.DeviceService.addDevice(result)
            //add error message
          }
        })
  }

  delete(MAC:string){
    const dialogRef = this.dialog.open(DeleteDialogComponent, {data: {MAC:MAC}});
        dialogRef.afterClosed().subscribe(result => {
          if (result){
            console.log("Deleted")
          }
        })
  }

  notes(device: Device){
    const dialogRef = this.dialog.open(NotesDialogComponent, {data: {device: device}});
        dialogRef.afterClosed().subscribe(result => {
        })
  }
}
