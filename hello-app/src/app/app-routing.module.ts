import { Component, NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreatedatasetComponent } from './createdataset/createdataset.component';
import { HomeComponent } from './home/home.component';
import { PlaygameComponent } from './playgame/playgame.component';
const routes: Routes = [
{path :'createdataset', component:CreatedatasetComponent},
{path:'playgame',component:PlaygameComponent},
{path:'home',component:HomeComponent},
{path:'',redirectTo:"/home",pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
