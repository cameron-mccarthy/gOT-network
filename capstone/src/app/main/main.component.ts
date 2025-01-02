import { Component } from '@angular/core';
import { MatSidenavModule} from '@angular/material/sidenav';
import { MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { DeviceTableComponent } from '../device-table/device-table.component';

@Component({
  selector: 'app-main',
  imports: [MatButtonModule, MatSidenavModule, MatIconModule, MatInputModule, MatFormFieldModule, DeviceTableComponent],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {

}
