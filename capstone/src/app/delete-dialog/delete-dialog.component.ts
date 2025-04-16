import { Component, inject } from '@angular/core';
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
import { Device } from '../interfaces/device';

@Component({
  selector: 'app-delete-dialog',
  imports: [MatDialogTitle, MatDialogActions, MatDialogContent],
  templateUrl: './delete-dialog.component.html',
  styleUrl: './delete-dialog.component.css'
})
export class DeleteDialogComponent {
  readonly dialogRef = inject(MatDialogRef<DeleteDialogComponent>);
  readonly data = inject(MAT_DIALOG_DATA);
  MAC: string;
  constructor(){
    this.MAC = this.data.MAC
  }

  close() {
    this.dialogRef.close(true);
  }
}
