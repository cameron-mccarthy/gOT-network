import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatCardModule} from '@angular/material/card';
import { Vulnerability } from '../interfaces/vulnerability';
import { VulnerabilityService } from '../services/vulnerability.service';
import { VulnerabilityCardComponent } from '../vulnerability-card/vulnerability-card.component';

@Component({
  selector: 'app-vulnerabilities',
  imports: [MatCardModule, VulnerabilityCardComponent, CommonModule],
  templateUrl: './vulnerabilities.component.html',
  styleUrl: './vulnerabilities.component.css'
})

export class VulnerabilitiesComponent {
  vulnList : Vulnerability[];
 constructor(public VulnerabilityService: VulnerabilityService){
  this.vulnList = this.VulnerabilityService.getAllVulns();
  console.log(this.vulnList)
 }
}