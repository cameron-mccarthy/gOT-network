import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { Vulnerability } from '../interfaces/vulnerability';
import { VulnerabilityService } from '../services/vulnerability.service';
import { VulnerabilityCardComponent } from '../vulnerability-card/vulnerability-card.component';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-vulnerabilities',
  imports: [MatCardModule, VulnerabilityCardComponent, CommonModule, MatInputModule, MatFormFieldModule, FormsModule, MatIconModule],
  templateUrl: './vulnerabilities.component.html',
  styleUrl: './vulnerabilities.component.css'
})

export class VulnerabilitiesComponent {
  vulnList!: Vulnerability[];
  searchText!: string;
  filteredVulns!: Vulnerability[];
  
  constructor(public VulnerabilityService: VulnerabilityService) {
    this.VulnerabilityService.vulnList.subscribe(x => {this.filteredVulns = x; this.vulnList = x});
  }
  
  searchVuln() {
    console.log(this.searchText); 
    this.filteredVulns = this.vulnList.filter(item =>
      item.IP.toLowerCase().includes(this.searchText.toLowerCase()) ||
      item.MAC.toLowerCase().includes(this.searchText.toLowerCase()) ||
      item.Desc.toLowerCase().includes(this.searchText.toLowerCase())
    );
  }


}