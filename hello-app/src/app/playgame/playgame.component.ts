import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from 'src/environments/environment';
@Component({
  selector: 'app-playgame',
  templateUrl: './playgame.component.html',
  styleUrls: ['./playgame.component.css']
})
export class PlaygameComponent implements AfterViewInit {
  // constructor(){}
  // ngOnInit():void{}
  constructor(private http: HttpClient){}
  @ViewChild('canvasres') public canvasel?:ElementRef ;
  private ctx?: any;
  result = ''
  classes = ['Sun','Flower','Umbrella','Pencil','Spoon','Tree','Mug','House','Bird','Hand'];
  
  ngAfterViewInit():void{
    const canvas =this.canvasel?.nativeElement;
    // const canvas=document.getElementById('mycanvas');
    const ctx = canvas.getContext("2d");
    // ctx.fillStyle="transparent";
    // ctx.fillRect(0,0,
    //     canvas.width,canvas.height);
    this.ctx=ctx;


    let painting = false;
    function startposition(e:any){
        painting=true;
        draw(e);
    }
    function finishedposition(){
        painting=false;
        ctx.beginPath();
    }
    function draw(e:any){
        let rect=canvas.getBoundingClientRect();
        let x=e.clientX- rect.left;
        let y=e.clientY- rect.top;
        if (!painting) return;
        ctx.lineWidth = 5;
        ctx.lineCap="round";
        ctx.lineTo(x, y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(x, y);

    }
    canvas.addEventListener("mousedown",startposition);
    canvas.addEventListener("mouseup",finishedposition);
    canvas.addEventListener("mousemove",draw);

  }
  clr(){
    this.ctx.clearRect(0,0,384,384);
  }

  Save(){
    
  var canvas:HTMLCanvasElement=this.canvasel?.nativeElement;
  var image = canvas.toDataURL('image/png');

  this.http.post(environment.SERVER_URL+'/Quickdraw/test',{image:image},{responseType:"text"}).subscribe((res:any)=>{
    console.log(res);

    this.result = 'You have drawn ' + res;
  });
  
}

}