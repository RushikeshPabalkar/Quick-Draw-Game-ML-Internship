import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'hello-app';
  response = null;

  constructor(private http: HttpClient){
    this.http.get('http://3.135.174.112/api/hello').subscribe((res:any)=> {
      this.response = res;
    })
  }
}
