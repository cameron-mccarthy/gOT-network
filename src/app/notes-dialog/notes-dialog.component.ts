import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import {
  MAT_DIALOG_DATA,
  MatDialog,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
  MatDialogRef,
  MatDialogTitle,
} from '@angular/material/dialog';
import { Device } from '../interfaces/device';

@Component({
  selector: 'app-notes-dialog',
  imports: [MatDialogContent, MatDialogTitle, MatDialogActions, MatButtonModule ],
  templateUrl: './notes-dialog.component.html',
  styleUrl: './notes-dialog.component.css'
})
export class NotesDialogComponent {
  readonly dialogRef = inject(MatDialogRef<NotesDialogComponent>);
    readonly data = inject(MAT_DIALOG_DATA);
    device: Device;
    constructor(){
      this.device = this.data.device
    }
  
    close() {
      this.dialogRef.close();
    }
}
