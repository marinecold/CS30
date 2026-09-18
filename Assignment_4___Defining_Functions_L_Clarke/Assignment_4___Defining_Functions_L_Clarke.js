//Lorenzo Clarke
//203245@gscs.ca
//Assignment 4 - Defining Functions

function setup() {
  
  createCanvas(1000,1000);
  //creates canvas to display shapes
  
  draw_fixed_square();
  //draws 4 lines to make a square at x50 y50
  
  draw_circle(125,125,50);
  //draws a circle at x125 y125 with a diameter of 50
  
  draw_concentric_circles(200,200);
  //draws 3 circles at x200 y200 with diameters of 90, 60, and 30
  
  function draw_fixed_square(){
    
   line(50,50,100,50);
   //draws the top line of the square
   
   line(100,50,100,100);
   //draws the left line of the square
   
   line(100,100,50,100);
   //draws the bottom line of the square
   
   line(50,100,50,50);
   //draws the right line of the square
   
  }
  
  function draw_circle(x,y,d){
    
   ellipse(x,y,d,d);
   //draws a circle at the given x and y coordinates with the given diameter
  
  }
  
  function draw_concentric_circles(x,y){
    
   ellipse(x,y,90,90);
   //draws a circle at the given x and y coordinates with a diameter of 90
   
   ellipse(x,y,60,60);
   //draws a circle at the given x and y coordinates with a diameter of 60
   
   ellipse(x,y,30,30);
   //draws a circle at the given x and y coordinates with a diameter of 30
    
  }

}


function draw() {

}
