//Lorenzo Clarke
//203245@gscs.ca
//Assignment 5 - Chessboard

function setup() {
  
  createCanvas(200,200);
  //Creates the canvas
  
  noStroke();
  //Removes the balck outline around the rectangles
  
  DrawBlackSquares();
  //Draws all of the black squares on the canvas
  
  DrawWhiteSquares();
  //Draws all of the white squares on the canvas
  
  
  function DrawBlackSquares(){
    
    fill(0);
    //Sets the infill colour of the rectangles to black
  
    rect(0,0,50,50);
    rect(50,50,50,50);
    rect(100,100,50,50);
    rect(150,150,50,50);
    rect(100,0,50,50);
    rect(150,50,50,50);
    rect(0,100,50,50);
    rect(50,150,50,50);
    //Creates all of the black squares based on their specific coordinates
    
  }
  
  function DrawWhiteSquares(){
    
    fill(255);
    //Sets the infill colour of the rectangles to black
  
    rect(50,0,50,50);
    rect(150,0,50,50);
    rect(0,50,50,50);
    rect(100,50,50,50);
    rect(50,100,50,50);
    rect(150,100,50,50);
    rect(150,100,50,50);
    rect(150,0,50,50);
    //Creates all of the white squares based on their specific coordinates
    
  }

}


function draw() {

}
