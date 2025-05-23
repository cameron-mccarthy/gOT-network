import { Component, inject } from '@angular/core';
import { FormsModule, ReactiveFormsModule, FormGroup } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import {
  MAT_DIALOG_DATA,
  MatDialog,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
  MatDialogRef,
  MatDialogTitle,
} from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { Device } from '../interfaces/device';
import { FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-add-device-dialog',
  imports: [MatFormFieldModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatDialogTitle,
    MatDialogContent,
    MatDialogActions,
  ],
  templateUrl: './add-device-dialog.component.html',
  styleUrl: './add-device-dialog.component.css'
})
export class AddDeviceDialogComponent {
  readonly dialogRef = inject(MatDialogRef<AddDeviceDialogComponent>);
  readonly data = inject(MAT_DIALOG_DATA);
  newDevice = this.data.device
  type: string;
  constructor() {
    this.type = this.data.edit ? "Edit" : "Add"
  }

  ngOnInit(){
    if (this.data.edit) {
      this.macAddressControl.disable();
    }
  }

  ipAddressControl = new FormControl('', [
    Validators.pattern(
      /^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$/
    )
  ]);

  macAddressControl = new FormControl('', [
    Validators.pattern(
      /^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/
    )
  ]);

  close() {
    console.log(this.newDevice)
    this.dialogRef.close(this.newDevice);
  }

  check() {
    return (this.ipAddressControl.hasError("pattern") || this.macAddressControl.hasError("pattern") || this.ipAddressControl.hasError("required") || this.macAddressControl.hasError("required"));
  }

}