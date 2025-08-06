import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'candidates',
    pathMatch: 'full',
  },
  {
    path: 'candidates',
    loadChildren: () =>
      import('./candidate/candidate.module').then((m) => m.CandidateModule),
  },
];
