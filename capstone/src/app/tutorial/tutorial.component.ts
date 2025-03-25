import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ElementRef } from '@angular/core';
import { ViewChildren } from '@angular/core';
import { QueryList } from '@angular/core';
import { AfterViewInit } from '@angular/core';


@Component({
  selector: 'app-tutorial',
  imports: [RouterModule],
  templateUrl: './tutorial.component.html',
  styleUrl: './tutorial.component.css'
})
export class TutorialComponent implements AfterViewInit{
  @ViewChildren('sections') sections!: QueryList<ElementRef>;

  private sectionMap = new Map<string, ElementRef>();

  ngAfterViewInit() {
    // Store each section reference in a map using its ID
    this.sections.forEach(section => {
      const id = section.nativeElement.id;
      this.sectionMap.set(id, section);
    });
  }

  scrollToSection(sectionId: string) {
    const section = this.sectionMap.get(sectionId);
    if (section) {
      section.nativeElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}
