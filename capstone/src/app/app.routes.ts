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
        path: "alerts",
        component: VulnerabilitiesComponent,
        title: "Alerts"
    },
    {
        path: "tutorial",
        component: TutorialComponent,
        title: "Tutorial"
    }
];