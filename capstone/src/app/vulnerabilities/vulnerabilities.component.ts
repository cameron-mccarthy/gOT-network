import { Component } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import { Vulnerability } from '../interfaces/vulnerability';
import { VulnerabilitiesService } from '../devices.service';

@Component({
  selector: 'app-vulnerabilities',
  imports: [MatCardModule],
  templateUrl: './vulnerabilities.component.html',
  styleUrl: './vulnerabilities.component.css'
})
export class VulnerabilitiesComponent {
  /*data: Vulnerability[];
  constructor(public VulnService: VulnerabilitiesService){
    this.data = this.VulnService.getAllVulns()
  }*/
  vulnList = [{description: "vuln1", link: "vuln1.com"},
    {description: "vuln2", link: "vuln2.com"}
  ];
}