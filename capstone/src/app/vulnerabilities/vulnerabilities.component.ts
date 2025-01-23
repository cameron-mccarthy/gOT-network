import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatCardModule} from '@angular/material/card';
import { Vulnerability } from '../interfaces/vulnerability';
import { VulnerabilitiesService } from '../devices.service';
import { VulnerabilityCardComponent } from '../vulnerability-card/vulnerability-card.component';

@Component({
  selector: 'app-vulnerabilities',
  imports: [MatCardModule, VulnerabilityCardComponent, CommonModule],
  templateUrl: './vulnerabilities.component.html',
  styleUrl: './vulnerabilities.component.css'
})

export class VulnerabilitiesComponent {
  vulnList : Vulnerability[];
 constructor(public VulnService: VulnerabilitiesService){
  this.vulnList = this.VulnService.getAllVulns();
  console.log(this.vulnList)
 }
}