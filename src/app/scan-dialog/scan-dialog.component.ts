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
import { FormControl, Validators } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';

@Component({
  selector: 'app-scan-dialog',
  imports: [MatFormFieldModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatDialogTitle,
    MatDialogContent,
    MatDialogActions,
    MatSelectModule
  ],
  templateUrl: './scan-dialog.component.html',
  styleUrl: './scan-dialog.component.css'
})
export class ScanDialogComponent {
  readonly dialogRef = inject(MatDialogRef<ScanDialogComponent>);
  readonly data = inject(MAT_DIALOG_DATA);
  IP:string;
  Version:string;
  CS:string;
  constructor() {
    this.IP = this.data.IP
    this.Version = this.data.Version
    this.CS = this.data.CS
  }

  ngOnInit(){
  }

  ipAddressControl = new FormControl('', [
    Validators.pattern(
      /^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$/
    )
  ]);

  close() {
    this.dialogRef.close({IP: this.IP, Version: this.Version, CS: this.CS});
  }

  check() {
    return (this.ipAddressControl.hasError("pattern") || this.ipAddressControl.hasError("required") || this.Version == "" || this.CS == "" );
  }

}
