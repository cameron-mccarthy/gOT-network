import { Component, inject } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { RouterModule, Router} from '@angular/router';
import { FormsModule } from '@angular/forms';
import { DevicesService } from '../services/devices.service';
import { MatDialog } from '@angular/material/dialog';
import { AddDeviceDialogComponent } from '../add-device-dialog/add-device-dialog.component';
import { ScanDialogComponent } from '../scan-dialog/scan-dialog.component';
import { CommonModule } from '@angular/common';
import { VulnerabilityService } from '../services/vulnerability.service';
import {MatBadgeModule} from '@angular/material/badge';

@Component({
  selector: 'app-main',
  imports: [RouterModule, MatButtonModule, MatSidenavModule, MatIconModule, MatInputModule, MatFormFieldModule, CommonModule, FormsModule, MatBadgeModule],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {
  readonly dialog = inject(MatDialog);
  notifications: number = 0;
  constructor(public DevicesService: DevicesService, public router: Router, public AlertService: VulnerabilityService) {
  }

  ngOnInit() {
    this.AlertService.vulnList.subscribe(data => this.notifications = data.length)
  }

  scan() {
    const dialogRef = this.dialog.open(ScanDialogComponent,{data: {IP: "", Version: "", CS: ""}});
    dialogRef.afterClosed().subscribe(result => {
      if (result){
        this.DevicesService.scan(result)
      }
    })
  }

  add() {
    const dialogRef = this.dialog.open(AddDeviceDialogComponent,{data: {edit: false, device: {
            IP: "",
            MAC: "",
            Product: "",
            Type: "",
            Status: "Inactive",
            Vendor: "",
            }}});
    dialogRef.afterClosed().subscribe(result => {
      if (result){
        this.DevicesService.addDevice(result)
      }
    })
  }

}
