import { Component, inject } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { DevicesService } from '../devices.service';
import { MatDialog } from '@angular/material/dialog';
import { AddDeviceDialogComponent } from '../add-device-dialog/add-device-dialog.component';
import { Device } from '../interfaces/device';

@Component({
  selector: 'app-main',
  imports: [RouterModule, MatButtonModule, MatSidenavModule, MatIconModule, MatInputModule, MatFormFieldModule, FormsModule],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {
  readonly dialog = inject(MatDialog);
  searchText!: string;
  constructor(public DevicesService: DevicesService) {
  }
  scan() {
    console.log("scan");
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

  search() {
    console.log(this.searchText)
  }

}
