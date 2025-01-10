import { Routes } from '@angular/router';
import { VulnerabilitiesComponent } from './vulnerabilities/vulnerabilities.component';
import { TutorialComponent } from './tutorial/tutorial.component';
import { DeviceTableComponent } from './device-table/device-table.component';

export const routes: Routes = [
    {
        path: "",
        component: DeviceTableComponent,
        title: "Home Page"
    },
    {
        path: "vulnerabilities",
        component: VulnerabilitiesComponent,
        title: "Vulnerabilities"
    },
    {
        path: "tutorial",
        component: TutorialComponent,
        title: "Tutorial"
    }
];
