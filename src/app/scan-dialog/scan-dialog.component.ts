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
import { CommonModule } from '@angular/common';

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
    MatSelectModule,
    CommonModule
  ],
  templateUrl: './scan-dialog.component.html',
  styleUrl: './scan-dialog.component.css'
})
export class ScanDialogComponent {
  readonly dialogRef = inject(MatDialogRef<ScanDialogComponent>);
  IP: string = "";
  Version: string = "";
  CS: string = "";
  Username: string = "";
  EncryptionProtocol: string = "";
  EncryptionPassword: string = "";
  AuthenticationProtocol: string = "";
  AuthenticationPassword: string = "";
  constructor() {
  }

  ngOnInit(){
  }

  ipAddressControl = new FormControl('', [
    Validators.pattern(
      /^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$/
    )
  ]);

  close() {
    this.dialogRef.close({IP: this.IP, Version: this.Version, CS: this.CS, Username: this.Username, EncryptionPassword: this.EncryptionPassword, EncryptionProtocol: this.EncryptionProtocol, AuthenticationPassword: this.AuthenticationPassword, AuthenticationProtocol: this.AuthenticationProtocol});
  }

  check() {
    return (this.ipAddressControl.hasError("pattern") || this.ipAddressControl.hasError("required") || this.Version == "" ||  ((this.Version == "1" || this.Version =="2") && this.CS == "" )
   || (this.Version == "3" && (this.AuthenticationPassword == "" || this.AuthenticationProtocol == "" || this.EncryptionPassword == "" || this.Username == "" || this.EncryptionProtocol == "")));
  }

}
