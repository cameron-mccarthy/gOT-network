import { Component } from '@angular/core';
import { MatSidenavModule} from '@angular/material/sidenav';
import { MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-main',
  imports: [RouterModule, MatButtonModule, MatSidenavModule, MatIconModule, MatInputModule, MatFormFieldModule, FormsModule],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {
  searchText!: string;

  scan(){
    console.log("scan")
  }

  add(){
    console.log("add")
  }

  refresh(){
    console.log("refresh")
  }

  search(){
    console.log(this.searchText)
  }

}
