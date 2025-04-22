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
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-main',
  imports: [RouterModule, MatButtonModule, MatSidenavModule, MatIconModule, MatInputModule, MatFormFieldModule, CommonModule, FormsModule],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {
  readonly dialog = inject(MatDialog);
  searchText!: string;
  constructor(public DevicesService: DevicesService, public router: Router) {
  }
  
  scan() {
    console.log("scan");
    this.DevicesService.getAllDevices().subscribe(x => console.log(x[0]))
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
