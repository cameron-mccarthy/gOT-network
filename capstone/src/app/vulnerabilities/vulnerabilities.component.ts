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
  /*data: Vulnerability[];
  constructor(public VulnService: VulnerabilitiesService){
    this.data = this.VulnService.getAllVulns()
  }*/
 
  vulnList = [
      {description: "vuln2", link: "https://material.angular.io/components/card/overview"},
      {description: "vuln3", link: "vuln3.com"}
  ];

 constructor(){}
  
}