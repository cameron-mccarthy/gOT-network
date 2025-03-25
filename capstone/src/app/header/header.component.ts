import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { inject } from '@angular/core';
import { AddDeviceDialogComponent } from '../add-device-dialog/add-device-dialog.component';
import { DevicesService } from '../services/devices.service';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-header',
  imports: [MatButtonModule, MatIconModule, MatInputModule, MatFormFieldModule, FormsModule, CommonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  readonly dialog = inject(MatDialog);
    searchText!: string;
    constructor(public DevicesService: DevicesService, public router: Router) {
    }

  scan() {
    console.log("scan");
    this.DevicesService.test().then(x => console.log(x));
  }

  add() {
    const dialogRef = this.dialog.open(AddDeviceDialogComponent);
    dialogRef.afterClosed().subscribe(result => {
      if (result){
        this.DevicesService.addDevice(result);
      }
    })
  }

  refresh() {
    console.log("refresh")
  }

  searchDevices() {
    console.log(this.searchText)
  }

  searchVuln() {
    console.log(this.searchText)
  }

}
